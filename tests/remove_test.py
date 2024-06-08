import pytest

from docker_ready import Project, get_project_by_name, remove_project
from docker_ready.utils.constants import Labels
from docker_ready.utils.tools import docker


@pytest.mark.usefixtures(
    "clear_config_fixture", "remove_postgres_project_fixture", "run_postgres_project_fixture"
)
def test_remove_project() -> None:
    project = get_project_by_name(name="postgres")
    assert isinstance(project, Project)
    assert isinstance(project.containers, list)

    remove_project(project=project)

    containers = docker.containers.list(
        filters={"label": f"{Labels.project}={project.compose.name}"}
    )
    assert not containers
