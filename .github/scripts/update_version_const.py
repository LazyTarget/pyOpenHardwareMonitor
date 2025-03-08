"""Update the manifest file."""

import os
import sys
import re


def update_version_const():
    """Update the version variable in const.py."""
    version = "0.0.0"
    for index, value in enumerate(sys.argv):
        if value in ["--version", "-V"]:
            version = sys.argv[index + 1]
            print("Passed version: ", version)

    with open(
        f"{os.getcwd()}/pyopenhardwaremonitor/const.py",
    ) as file:
        content = file.read()

    version = version.replace("refs/tags/", "").lstrip("v")
    print("Modified version: ", version)
    content = re.sub(
        pattern='__version__ = "(.+)"',
        string=content,
        repl='__version__ = "' + version + '"',
    )

    with open(
        f"{os.getcwd()}/pyopenhardwaremonitor/const.py",
        "w",
    ) as file:
        file.write(content)


update_version_const()
