import pytest
from docker.models.containers import Container

from docker_ready import Project, get_all_projects, get_project_by_name, get_running_projects


def test_get_all_projects() -> None:
    projects = get_all_projects()
    assert isinstance(projects, list)
    assert len(projects) > 0
    for project in projects:
        assert isinstance(project, Project)


def test_get_project_by_name() -> None:
    project = get_project_by_name(name="postgres")
    assert isinstance(project, Project)
    assert project.info.full_name == "PostgreSQL"


@pytest.mark.usefixtures("clear_config_fixture", "run_postgres_project_fixture")
def test_get_running_projects() -> None:
    projects = get_running_projects()
    assert isinstance(projects, list)
    assert len(projects) == 1
    for project in projects:
        assert isinstance(project, Project)
        assert isinstance(project.containers, list)
        assert len(project.containers) == 1
        for container in project.containers:
            assert isinstance(container, Container)
