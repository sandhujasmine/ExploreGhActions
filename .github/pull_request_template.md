
Please go to the `Preview` tab and select the appropriate sub-template:

> [!NOTE]
> By default PRs with title `fix/feat` included in the changelog. Check the project's pyproject.toml to see what PRs are included during changelog generation.

* [fix](?title=fix%3A%20%5BJIRA%3AXXX%5D%20%3Cadd-PR-title%3E&expand=1&template=bug_fix.md)
* [feat](?title=feat%3A%20%5BJIRA%3AXXX%5D%20%3Cadd-PR-title%3E&expand=1&template=feature.md)
* [chore/docs/style/refactor/perf](?title=%3Cchore%2Fdocs%2Fstyle%2Frefactor%2Fperf%3E%3A%20%5BJIRA%3A%20XXX%5D&expand=1&template=feature.md)

<!-- 
TITLE should be in following format, default scope is feat above:

    scope: [JIRA-ticket-number] Concise PR title

Scopes with definitions:

  fix:  a commit of the type fix patches a bug in your codebase
        (this correlates with PATCH in semantic versioning).

  feat: a commit of the type feat introduces a new feature to the codebase
        (this correlates with MINOR in semantic versioning).

  BREAKING CHANGE: a commit that has the text BREAKING CHANGE: at the beginning of
                   its optional body or footer section introduces a breaking API change
                   (correlating with MAJOR in semantic versioning).

  Others: commit types other than fix: and feat: are allowed,
          like chore:, docs:, style:, refactor:, perf:, test:, and others.
          Notice these types are not mandated by the conventional commits specification,
          and have no implicit effect in semantic versioning (unless they include a BREAKING CHANGE).

We use conventional commits spec: https://www.conventionalcommits.org/en/v1.0.0/
And commitizen to manage version bumps & changelog
-->