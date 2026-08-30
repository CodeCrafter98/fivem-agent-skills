# Security Policy

## Supported Versions

Currently, only the latest release of FiveM Agent Skills receives security updates.

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability

If you discover a vulnerability in the *guidance* provided by these skills (e.g., a skill instructs an agent to use an insecure pattern that allows SQL injection, event forging, or economy abuse), please report it.

**Do not open a public issue.**

Instead, please email the details to the maintainer or send a direct message on the relevant community platforms (Discord/GitHub). 

We take security guidance seriously. Since these skills are used to generate server code, bad security advice in a skill propagates to live servers. We will issue a patch release as quickly as possible to correct the guidance.

When reporting, please include:
- The name of the skill(s) providing the insecure advice
- A brief description of the vulnerability pattern
- A prompt that reliably causes the agent to generate the insecure code
- (Optional) The official FiveM/framework documentation proving the pattern is insecure
