from pathlib import Path

import pytest

from docker_ready.project import ComposeYaml, Info, Project

POSTGRES_PROJECT_DIR = (
    Path(__file__).parent.parent.joinpath("docker_ready").joinpath("projects").joinpath("postgres")
)


@pytest.mark.usefixtures("clear_config_fixture")
def test_project():
    project = Project(directory=POSTGRES_PROJECT_DIR)
    assert isinstance(project, Project)

    assert isinstance(project.root_dir, Path)
    assert isinstance(project.user_dir, Path)
    assert project.root_dir == POSTGRES_PROJECT_DIR
    assert project.root_dir.exists()
    assert not project.user_dir.exists()

    assert isinstance(project.info, Info)
    assert isinstance(project.compose, ComposeYaml)
    for name, service in project.compose.services.items():
        assert name == "postgres"
        assert service.image == "postgres:latest"
        assert service.env_file == ["./postgres.env"]
