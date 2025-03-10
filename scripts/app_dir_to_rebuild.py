import os
import re
from pathlib import Path

"""
Given a space separated list of files that have changes; it determines the app directory
which needs to be built and uploaded.

# Can be tested locally as follows:

CHANGED_FILES="/Users/jasmine/projects/ExploreGhActions/agents/agent1/CHANGELOG.md /Users/jasmine/projects/ExploreGhActions/agents/agent1/pyproject.toml" python app_dir_to_rebuild.py
src_dirs={'/Users/jasmine/projects/agents-service/agents/assistant-agent'}
"""

GITHUB_OUTPUT = os.getenv("GITHUB_OUTPUT")
changed_files= os.getenv("ALL_CHANGED_FILES").split()
match_regex=os.getenv(r"MATCH_REGEX", r"^(.*?/src)/")

src_dirs = set()

for file in changed_files:
    match = re.search(match_regex, file)
    if match:
        src_dir = Path(match.group(1)).resolve()
        parent_dir = src_dir.parent
        src_dirs.add(str(parent_dir))

# expect to find at least 1 package; but if more than 1, then raise error
# if more than 1 packages, then there is a dependency between them so building is more
# challenging; let's not handle this till we have a clean way to do it. For now,
# PR should only result in changes to 1 package
if len(src_dirs) > 1:
  raise ValueError("expect changes to only 1 package per PR; ERRORING OUT..")

print(f'{src_dirs=}')
if GITHUB_OUTPUT:
    if src_dirs:
      with open(GITHUB_OUTPUT, 'w') as fp:
        app_dir = src_dirs.pop()
        fp.write(f'APP_DIR={app_dir}')
    else:
       print(f"No packages found: {changed_files=}")
