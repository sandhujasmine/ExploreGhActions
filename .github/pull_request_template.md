
Please go to the `Preview` tab and select the appropriate sub-template:

* [fix](?title=fix%3A%20%5BJIRA%3AXXX%5D%20%3Cadd-PR-title%3E&expand=1&template=bug_fix.md) - Bug fixes (PATCH version)
* [feat](?title=feat%3A%20%5BJIRA%3AXXX%5D%20%3Cadd-PR-title%3E&expand=1&template=feature.md) - New features (MINOR version)
* [chore](?title=chore%3A%20%5BJIRA%3AXXX%5D%20%3Cadd-PR-title%3E&expand=1&template=other.md) - Build/maintenance tasks/catch all if you cant find a type for the change
* [docs](?title=docs%3A%20%5BJIRA%3AXXX%5D%20%3Cadd-PR-title%3E&expand=1&template=other.md) - Documentation changes
* [style](?title=style%3A%20%5BJIRA%3AXXX%5D%20%3Cadd-PR-title%3E&expand=1&template=other.md) - Code formatting/style
* [refactor](?title=refactor%3A%20%5BJIRA%3AXXX%5D%20%3Cadd-PR-title%3E&expand=1&template=other.md) - Code refactoring
* [perf](?title=perf%3A%20%5BJIRA%3AXXX%5D%20%3Cadd-PR-title%3E&expand=1&template=other.md) - Performance improvements
* [test](?title=test%3A%20%5BJIRA%3AXXX%5D%20%3Cadd-PR-title%3E&expand=1&template=other.md) - Test changes

## PR guidelines ##
We use conventional commits spec: https://www.conventionalcommits.org/en/v1.0.0/
And commitizen to manage version bumps & changelog:
- PRs must follow coventional commit messages.
- Scope is optional

PR TITLE should be in following format, default scope is feat above:
```
    type(scope): [JIRA-ticket-number] Concise PR title
```

Example of a feature that introduces a breaking change.
```
feat(auth): [JIRA-123] switch to new login system

BREAKING CHANGE: This removes support for legacy login.
```

## Commit Types Reference

| Change Type | Description | Version Impact | Changelog |
|------|-------------|----------------|-----------|
| `fix` | Patches a bug in your codebase | PATCH | ✅ Included |
| `feat` | Introduces a new feature to the codebase | MINOR | ✅ Included |
| `chore` | Changes to build process or auxiliary tools | None | ❌ Excluded |
| `docs` | Documentation only changes | None | ❌ Excluded |
| `style` | Changes that do not affect the meaning of the code | None | ❌ Excluded |
| `refactor` | Code change that neither fixes a bug nor adds a feature | None | ❌ Excluded |
| `perf` | Code change that improves performance | None | ❌ Excluded |
| `test` | Adding missing tests or correcting existing tests | None | ❌ Excluded |
| `BREAKING CHANGE` | Introduces a breaking API change | MAJOR | ✅ Included |

