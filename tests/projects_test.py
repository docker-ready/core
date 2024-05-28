from pathlib import Path

PROJECTS_DIR = Path(__file__).parent.parent.joinpath("docker_ready").joinpath("projects")


def test_projects() -> None:
    for child in PROJECTS_DIR.iterdir():
        assert child.is_dir()
        for sub_child in child.iterdir():
            assert sub_child.is_file()
            assert sub_child.name in ["compose.yaml", "project.yaml"]
