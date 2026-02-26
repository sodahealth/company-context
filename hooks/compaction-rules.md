# Compaction Rules — Company-Wide Safety Reminders

These rules are re-injected after context compaction to maintain safety
awareness throughout long sessions.

1. **Never commit secrets or credentials.** API keys, tokens, passwords, and
   private keys must not appear in committed code. Use environment variables
   or secret managers.

2. **Never force-push.** Force-pushing rewrites shared branch history and can
   destroy teammates' work. Use regular pushes and new branches instead.

3. **Never send PHI/PII to unapproved services.** Patient health information
   and personally identifiable information may only be transmitted to services
   on the approved list (`knowledge/approved-services.md`). When in doubt, ask.

4. **Follow your department's conventions.** If your department has its own
   CLAUDE.md or coding standards, follow those conventions. Company-wide rules
   apply as a baseline.

5. **Don't disable hooks.** Session transcript capture and safety guards run
   automatically. These support security compliance and incident investigation.
   Do not modify or disable hook configurations.
