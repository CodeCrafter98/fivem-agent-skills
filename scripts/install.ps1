<#
.SYNOPSIS
Safely install FiveM Agent Skills into a project or globally.

.DESCRIPTION
Copies skill directories and core instructions to a target project or global agent directory.
Never deletes unrelated existing skills, even with -Force.

.PARAMETER Scope
Install scope: 'Project' (into -Dest) or 'Global' (~/.agents/skills).

.PARAMETER Dest
Target project root (required if Scope is 'Project').

.PARAMETER AntigravityCompat
Also install to ~/.gemini/config/skills for Antigravity global discovery.

.PARAMETER Force
Replace existing FiveM skill directories (never deletes unrelated skills).

.PARAMETER DryRun
Show what would be installed without making changes.

.PARAMETER Verify
Run post-install validation to ensure files were written.

.PARAMETER Version
Show script version.
#>

[CmdletBinding(DefaultParameterSetName="Default")]
param (
    [Parameter(Mandatory=$true, ParameterSetName="Default")]
    [ValidateSet('Project', 'Global')]
    [string]$Scope,

    [Parameter(Mandatory=$false, ParameterSetName="Default")]
    [string]$Dest,

    [Parameter(Mandatory=$false, ParameterSetName="Default")]
    [switch]$AntigravityCompat,

    [Parameter(Mandatory=$false, ParameterSetName="Default")]
    [switch]$Force,

    [Parameter(Mandatory=$false, ParameterSetName="Default")]
    [switch]$DryRun,

    [Parameter(Mandatory=$false, ParameterSetName="Default")]
    [switch]$Verify,

    [Parameter(Mandatory=$true, ParameterSetName="Version")]
    [switch]$Version
)

$ErrorActionPreference = "Stop"
$ScriptRoot = Split-Path -Parent $MyInvocation.MyCommand.Definition
$RepoRoot = Split-Path -Parent $ScriptRoot
$SrcSkills = Join-Path $RepoRoot ".agents\skills"

$VersionFile = Join-Path $RepoRoot "VERSION"
$VerStr = "unknown"
if (Test-Path $VersionFile) {
    $VerStr = (Get-Content $VersionFile).Trim()
}

if ($Version) {
    Write-Host "FiveM Agent Skills v$VerStr"
    exit 0
}

Write-Host "FiveM Agent Skills v$VerStr"
Write-Host "Source: $RepoRoot`n"

function Install-Skills {
    param([string]$TargetRoot)
    
    if (-not $DryRun -and -not (Test-Path $TargetRoot)) {
        New-Item -ItemType Directory -Force -Path $TargetRoot | Out-Null
    }

    $SkillDirs = Get-ChildItem -Path $SrcSkills -Directory -Recurse | Where-Object { Test-Path (Join-Path $_.FullName "SKILL.md") }
    $Installed = 0
    $Skipped = 0
    $SkillNames = @()

    foreach ($Dir in $SkillDirs) {
        $Dst = Join-Path $TargetRoot $Dir.Name
        $SkillNames += $Dir.Name

        if (Test-Path $Dst) {
            if (-not $Force) {
                if (-not $DryRun) { Write-Host "  SKIP  $($Dir.Name)" }
                $Skipped++
                continue
            }
            if (-not $DryRun) { Remove-Item -Recurse -Force $Dst }
        }

        if ($DryRun) {
            Write-Host "  WOULD INSTALL  $($Dir.Name) -> $Dst"
        } else {
            Copy-Item -Recurse -Force $Dir.FullName $Dst
        }
        $Installed++
    }

    $Action = if ($DryRun) { "Would install" } else { "Installed" }
    Write-Host "`n  $Action $Installed skills into $TargetRoot; skipped $Skipped."
    
    return @{ Installed = $Installed; Skipped = $Skipped; Names = $SkillNames }
}

function Write-Receipt {
    param([string]$TargetDir, [string[]]$Names)
    
    if ($DryRun) { return }

    $ReceiptPath = Join-Path $TargetDir ".agents\fivem-agent-skills.json"
    $ReceiptDir = Split-Path -Parent $ReceiptPath
    if (-not (Test-Path $ReceiptDir)) {
        New-Item -ItemType Directory -Force -Path $ReceiptDir | Out-Null
    }

    $Receipt = @{
        package = "fivem-agent-skills"
        version = $VerStr
        source = "https://github.com/CodeCrafter98/fivem-agent-skills"
        installed_at = (Get-Date).ToUniversalTime().ToString("yyyy-MM-ddTHH:mm:ssZ")
        skill_count = $Names.Count
        skills = $Names | Sort-Object
    }

    $Receipt | ConvertTo-Json -Depth 3 | Set-Content $ReceiptPath -Encoding UTF8
    Write-Host "  Receipt -> $ReceiptPath"
}

function Verify-Installation {
    param([string]$TargetRoot, [int]$ExpectedCount)
    
    if (-not (Test-Path $TargetRoot)) { return }
    $Found = @(Get-ChildItem -Path $TargetRoot -Recurse -Filter "SKILL.md")
    $FiveMSkills = $Found | Where-Object { $_.Directory.Name -like "fivem-*" }
    
    Write-Host "`n  Verify: $($FiveMSkills.Count) FiveM skills found in $TargetRoot"
    if ($FiveMSkills.Count -lt $ExpectedCount) {
        Write-Host "  WARNING: expected at least $ExpectedCount FiveM skills" -ForegroundColor Yellow
    }
}

if ($Scope -eq 'Project') {
    if (-not $Dest) {
        Write-Error "Error: -Dest is required for project scope"
        exit 1
    }

    $DestPath = (Resolve-Path $Dest -ErrorAction Ignore).ProviderPath
    if (-not $DestPath) { $DestPath = $Dest }
    Write-Host "Installing to project: $DestPath"

    $TargetSkills = Join-Path $DestPath ".agents\skills"
    $Result = Install-Skills -TargetRoot $TargetSkills
    Write-Receipt -TargetDir $DestPath -Names $Result.Names

    $AgDir = Join-Path $DestPath ".agents"
    if (-not $DryRun -and -not (Test-Path $AgDir)) {
        New-Item -ItemType Directory -Force -Path $AgDir | Out-Null
    }

    $AgTarget = Join-Path $AgDir "AGENTS.md"
    $AgSrc = Join-Path $RepoRoot ".agents\AGENTS.md"
    if (-not (Test-Path $AgTarget) -or $Force) {
        if (-not $DryRun) {
            Copy-Item $AgSrc $AgTarget -Force
            Write-Host "  Installed FiveM instructions -> $AgTarget"
        } else {
            Write-Host "  WOULD INSTALL  .agents\AGENTS.md -> $AgTarget"
        }
    } else {
        Write-Host "  SKIP  $AgTarget (merge manually if desired)"
    }

    $RootTarget = Join-Path $DestPath "AGENTS.md"
    $RootSrc = Join-Path $RepoRoot "AGENTS.md"
    if (-not (Test-Path $RootTarget)) {
        if (-not $DryRun) {
            Copy-Item $RootSrc $RootTarget
            Write-Host "  Installed root instructions -> $RootTarget"
        } else {
            Write-Host "  WOULD INSTALL  AGENTS.md -> $RootTarget"
        }
    } else {
        Write-Host "  SKIP  $RootTarget (will not overwrite project AGENTS.md)"
    }

    if ($Verify -and -not $DryRun) {
        Verify-Installation -TargetRoot $TargetSkills -ExpectedCount $Result.Installed
    }

} else {
    $HomeDir = [System.Environment]::GetFolderPath('UserProfile')
    Write-Host "Installing globally for user: $HomeDir"

    $GlobalSkills = Join-Path $HomeDir ".agents\skills"
    $Result = Install-Skills -TargetRoot $GlobalSkills

    if ($AntigravityCompat) {
        Write-Host "`nAntigravity compatibility:"
        $AgSkills = Join-Path $HomeDir ".gemini\config\skills"
        Install-Skills -TargetRoot $AgSkills | Out-Null
    }

    if ($Verify -and -not $DryRun) {
        Verify-Installation -TargetRoot $GlobalSkills -ExpectedCount $Result.Installed
    }
}

Write-Host "`nDone."
