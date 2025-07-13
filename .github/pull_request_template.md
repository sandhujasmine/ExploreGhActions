
Please go to the `Preview` tab and select the appropriate sub-template:

> [!NOTE]
> Not all change types are included in the changelog. Check the project's pyproject.toml to see available changes types and their inclusion status in changelog. Default behavior: [Commit Types section](#commit-types)

* [fix](?title=fix%3A%20%5BJIRA%3AXXX%5D%20%3Cadd-PR-title%3E&expand=1&template=bug_fix.md)
* [feat](?title=feat%3A%20%5BJIRA%3AXXX%5D%20%3Cadd-PR-title%3E&expand=1&template=feature.md)
* [chore](?title=chore%3A%20%5BJIRA%3AXXX%5D%20%3Cadd-PR-title%3E&expand=1&template=other.md)
* [docs](?title=docs%3A%20%5BJIRA%3AXXX%5D%20%3Cadd-PR-title%3E&expand=1&template=other.md)
* [style](?title=style%3A%20%5BJIRA%3AXXX%5D%20%3Cadd-PR-title%3E&expand=1&template=other.md)
* [refactor](?title=refactor%3A%20%5BJIRA%3AXXX%5D%20%3Cadd-PR-title%3E&expand=1&template=other.md)
* [perf](?title=perf%3A%20%5BJIRA%3AXXX%5D%20%3Cadd-PR-title%3E&expand=1&template=other.md)
* [test](?title=test%3A%20%5BJIRA%3AXXX%5D%20%3Cadd-PR-title%3E&expand=1&template=other.md)

## PR guidelines ##
We use conventional commits spec: https://www.conventionalcommits.org/en/v1.0.0/
And commitizen to manage version bumps & changelog
- PRs must follow coventional commit messages.
- Scope is optional

PR TITLE should be in following format, default scope is feat above:
```
    type(scope): [JIRA-ticket-number] Concise PR title
```

Here's an example of a feature that introduces a breaking change.
```
feat(auth): [JIRA-123] switch to new login system

BREAKING CHANGE: This removes support for legacy login.
```

## Commit Types

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

We use conventional commits spec: https://www.conventionalcommits.org/en/v1.0.0/
And commitizen to manage version bumps & changelog