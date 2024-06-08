import pytest

from docker_ready import Project, get_project_by_name, run_project
from docker_ready.utils.tools import docker


@pytest.mark.usefixtures("clear_config_fixture", "remove_postgres_project_fixture")
def test_run_project() -> None:
    project = get_project_by_name(name="postgres")
    assert isinstance(project, Project)

    run_project(project=project)

    containers = docker.containers.list()
    assert len(containers) == len(project.compose.services)
