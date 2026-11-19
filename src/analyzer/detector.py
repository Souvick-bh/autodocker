def detect_language(files):

    names = [
        file.name
        for file in files
    ]

    languages = []


    if "package.json" in names:
        languages.append("JavaScript/TypeScript")


    if "requirements.txt" in names:
        languages.append("Python")


    if "go.mod" in names:
        languages.append("Go")


    if "Cargo.toml" in names:
        languages.append("Rust")


    if "pom.xml" in names:
        languages.append("Java")


    return languages