param(
  [ValidateSet("Project","Global")][string]$Scope = "Project",
  [string]$Dest = ".",
  [switch]$AntigravityCompat,
  [switch]$Force
)
$Root = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$Source = Join-Path $Root ".agents\skills"
function Install-Skills($TargetRoot) {
  New-Item $TargetRoot -ItemType Directory -Force | Out-Null
  $Installed = 0; $Skipped = 0
  Get-ChildItem $Source -Recurse -Filter SKILL.md | ForEach-Object {
    $SkillDir = $_.Directory
    $Target = Join-Path $TargetRoot $SkillDir.Name
    if (Test-Path $Target) {
      if (-not $Force) { Write-Host "SKIP existing: $Target"; $Skipped++; return }
      Remove-Item $Target -Recurse -Force
    }
    Copy-Item $SkillDir.FullName $Target -Recurse
    $Installed++
  }
  Write-Host "Installed $Installed skills into $TargetRoot; skipped $Skipped."
}
if ($Scope -eq "Project") {
  $TargetRoot = (Resolve-Path $Dest).Path
  Install-Skills (Join-Path $TargetRoot ".agents\skills")
  $AgentsDir = Join-Path $TargetRoot ".agents"; New-Item $AgentsDir -ItemType Directory -Force | Out-Null
  $AgTarget = Join-Path $AgentsDir "AGENTS.md"
  if ((-not (Test-Path $AgTarget)) -or $Force) { Copy-Item (Join-Path $Root ".agents\AGENTS.md") $AgTarget -Force } else { Write-Host "SKIP existing: $AgTarget" }
  $RootTarget = Join-Path $TargetRoot "AGENTS.md"
  if (-not (Test-Path $RootTarget)) { Copy-Item (Join-Path $Root "AGENTS.md") $RootTarget } else { Write-Host "SKIP existing: $RootTarget" }
} else {
  Install-Skills (Join-Path $HOME ".agents\skills")
  if ($AntigravityCompat) { Install-Skills (Join-Path $HOME ".gemini\config\skills") }
}
