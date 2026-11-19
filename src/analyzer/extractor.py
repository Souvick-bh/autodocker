import json


def extract_package_json(path):

    with open(path) as f:
        data = json.load(f)


    return {
        "name": data.get("name"),

        "scripts":
            data.get("scripts", {}),

        "dependencies":
            list(
                data.get(
                    "dependencies",
                    {}
                ).keys()
            )
    }