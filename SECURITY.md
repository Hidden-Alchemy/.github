# Security

## Reporting a vulnerability

Hidden Alchemy uses GitHub's built-in **private vulnerability reporting**:
security vulnerabilities in any Hidden Alchemy repository should be reported
through the **Security → Report a vulnerability** feature on the affected
repository's GitHub page.

This is the only reporting channel. We do not maintain a public email address
or external form for security reports.

### What happens next

- **Acknowledgement:** we aim to acknowledge receipt within **7 days** of a
  report.
- **Triage and fix:** we aim to respond with an assessment and, where
  appropriate, a fix plan within a reasonable timeframe. Hidden Alchemy does
  not currently have a dedicated, funded security response team; the Core Team
  handles reports on a best-effort basis alongside regular maintainer work. We
  state this plainly so expectations are honest.
- **Disclosure:** we coordinate disclosure responsibly after a fix is
  released. We ask that you refrain from public disclosure until we have had
  the opportunity to respond.

## Scope

This policy applies to software and infrastructure maintained under the Hidden
Alchemy organization. Reports about the organization's configuration (`.github`
repository) are handled through the same channel.

## Security expectations for contributors

- Never commit secrets, tokens, or credentials to any repository.
- Never log secret material in workflow output, issue bodies, or comments.
- Report supply-chain or permission issues even if you are unsure whether they
  are in scope — we would rather triage an unnecessary report than miss a
  real one.