from pydantic import BaseModel


class ProjectProfile(BaseModel):

    language: list[str]

    framework: list[str]

    package_manager: str | None

    build_command: str | None

    start_command: str | None

    dependencies: list[str]