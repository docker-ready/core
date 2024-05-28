import shutil

from docker import from_env
from dotenv import dotenv_values

from docker_ready.project import Project, Service

docker = from_env()


def run_project(project: Project) -> None:
    _setup_project_dir(project=project)
    for name, service in project.compose.services.items():
        _run_service(service_name=name, service=service, project=project)


def _setup_project_dir(project: Project) -> None:
    _create_project_dir(project=project)
    _create_env_files(project=project)


def _create_project_dir(project: Project) -> None:
    if not project.user_dir.exists():
        project.user_dir.mkdir(parents=True)

        shutil.copyfile(
            project.project_yaml_file.absolute(),
            project.user_dir.joinpath(project.project_yaml_file.name),
        )
        shutil.copyfile(
            project.compose_yaml_file.absolute(),
            project.user_dir.joinpath(project.compose_yaml_file.name),
        )


def _create_env_files(project: Project) -> None:
    for file_name, envs in project.env_files.items():
        with open(project.user_dir.joinpath(f"{file_name}.env"), "w") as f:
            for env_name, env_value in envs.items():
                f.write(f"{env_name}={env_value}\n")


def _run_service(service_name: str, service: Service, project: Project) -> None:
    if service.env_file:
        environment = dotenv_values(project.user_dir.joinpath(service.env_file[0]))
    else:
        environment = None
    name = f"{project.compose.name}-{service_name}"
    docker.containers.run(image=service.image, environment=environment, name=name, detach=True)


__all__ = ["run_project"]
