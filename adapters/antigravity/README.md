# Google Antigravity

Antigravity natively supports Agent Skills discovery.

**Installation via skills.sh (Recommended):**
```bash
npx skills add CodeCrafter98/fivem-agent-skills --agent antigravity
```

**Project workspace skills:** 
`.agents/skills/<skill>/SKILL.md`

**Global user skills:** 
`~/.gemini/config/skills/<skill>/SKILL.md`

Antigravity uses the `skills-manifest.json` and SKILL.md frontmatter to progressively load only the necessary engineering context when a FiveM task is detected.
