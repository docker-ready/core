from docker import from_env

from docker_ready import run_project
from docker_ready.get import get_project_by_name
from docker_ready.project import Project

docker = from_env()


def test_run_project(clear_config_fixture: None) -> None:
    project = get_project_by_name(name="postgres")
    assert isinstance(project, Project)

    run_project(project=project)

    containers = docker.containers.list()
    assert len(containers) == len(project.compose.services)
