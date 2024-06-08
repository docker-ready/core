import shutil
from pathlib import Path

import pytest

from docker_ready.get import get_project_by_name
from docker_ready.project import Project
from docker_ready.run import run_project

CONFIG_DIR = Path("~").expanduser().joinpath(".config").joinpath("docker-ready")


@pytest.fixture
def clear_config_fixture() -> None:
    if CONFIG_DIR.exists():
        shutil.rmtree(CONFIG_DIR)


@pytest.fixture
def run_postgres_project_fixture() -> Project:
    project = get_project_by_name(name="postgres")
    assert isinstance(project, Project)
    run_project(project=project)
    return project
