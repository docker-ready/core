from docker_ready import Project, get_all_projects, get_project_by_name


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
