import argparse
import docker
import json
import os


class Executor:
    def __init__(self):
        self.docker_host = docker.from_env()

    def docker_image_exists(self, name):
        exists = True
        try:
            self.docker_host.images.get(name)
            print("[~] Image exists")
        except docker.errors.ImageNotFound:
            exists = False
            print("[!] Image does not exist")
        return exists

    def docker_build(self, dockerfile, platform, tag):
        print("[*] Building image")
        data = self.docker_host.images.build(path=dockerfile, platform=platform, tag=tag)
        return data

    def docker_run(self, name, platform, volumes):
        print("[*] Running container")
        data = self.docker_host.containers.run(image=name, platform=platform, volumes=volumes, remove=True)
        return data

    def execute(self, r_exec, force_build=False):
        name = r_exec["name"]
        dockerfile = r_exec["dockerfile"]
        platform = r_exec["platform"]
        tag = r_exec["tag"]
        volumes = r_exec["volumes"]
        if not self.docker_image_exists(name) or force_build:
            self.docker_build(dockerfile, platform, tag)
        data = self.docker_run(name, platform, volumes)
        return data


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--execution-name", help="Named target for execution")
    parser.add_argument("-r", "--registered-executions", help="/path/to/registered-executions.json")
    args = parser.parse_args()

    registered_execs = {}
    if os.path.exists(args.registered_executions):
        with open(args.registered_executions, 'r') as fh:
            registered_execs = json.load(fh)

    registered_exec = {}
    if args.execution_name in registered_execs.keys():
        registered_exec = registered_execs[args.execution_name]

    exec = Executor()
    exec.execute(registered_exec)


if __name__ == "__main__":
    main()
