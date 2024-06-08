import shutil

import pytest

from docker_ready.get import get_project_by_name
from docker_ready.project import Project
from docker_ready.remove import remove_project
from docker_ready.run import run_project
from docker_ready.utils.constants import Dirs


@pytest.fixture
def clear_config_fixture() -> None:
    if Dirs.config.exists():
        shutil.rmtree(path=Dirs.config)


@pytest.fixture
def run_postgres_project_fixture() -> Project:
    project = get_project_by_name(name="postgres")
    assert isinstance(project, Project)
    run_project(project=project)
    return project


@pytest.fixture
def remove_postgres_project_fixture() -> None:
    project = get_project_by_name(name="postgres")
    assert isinstance(project, Project)
    remove_project(project=project)
