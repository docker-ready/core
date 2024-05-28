from pathlib import Path

from pydantic.main import BaseModel
from pydantic.networks import HttpUrl
from pydantic_yaml import parse_yaml_file_as


class Info(BaseModel):
    full_name: str
    description: str
    site_url: HttpUrl
    repo_url: HttpUrl
    container_registry_url: HttpUrl


class ProjectYaml(BaseModel):
    info: Info
    env_files: dict[str, dict[str, str]]


class Service(BaseModel):
    image: str

    env_file: list


class ComposeYaml(BaseModel):
    name: str
    services: dict[str, Service]


class Project:
    def __init__(self, directory: Path) -> None:
        self.root_dir = directory
        self.user_dir = (
            Path("~")
            .expanduser()
            .joinpath(".config")
            .joinpath("docker-ready")
            .joinpath(directory.name)
        )

        if self.user_dir.exists():
            directory = self.user_dir

        self._project(directory=directory)
        self._compose(directory=directory)

    def _project(self, directory: Path) -> None:
        self.project_yaml_file = directory.joinpath("project.yaml")
        project = parse_yaml_file_as(ProjectYaml, self.project_yaml_file)
        self.info = project.info
        self.env_files = project.env_files

    def _compose(self, directory: Path) -> None:
        self.compose_yaml_file = directory.joinpath("compose.yaml")
        self.compose = parse_yaml_file_as(ComposeYaml, self.compose_yaml_file)


__all__ = ["Project"]
