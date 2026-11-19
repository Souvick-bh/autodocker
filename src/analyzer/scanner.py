from pathlib import Path


IMPORTANT_FILES = [
    "package.json",
    "package-lock.json",
    "pnpm-lock.yaml",
    "yarn.lock",
    "requirements.txt",
    "pyproject.toml",
    "go.mod",
    "Cargo.toml",
    "pom.xml",
    "Dockerfile",
]


def scan_project(path: str):

    root = Path(path)

    found = []

    for filename in IMPORTANT_FILES:
        matches = root.rglob(filename)

        for match in matches:
            found.append(match)

    return found