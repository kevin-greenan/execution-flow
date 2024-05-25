from flask import Flask, render_template
import requests
import json
import os


app = Flask(__name__)


def get_registered_executions(p):
    registered_execs = {}
    if os.path.exists(p):
        with open(p, 'r') as fh:
            registered_execs = json.load(fh)
    return registered_execs


def format_execution_table(execs):
    table = [["Execution name", "Image name", "Configuration path", "Platform", "Volumes"]]
    for exec_name in execs.keys():
        exec = execs[exec_name]
        image = exec["name"]
        path = exec["dockerfile"]
        platform = exec["platform"]
        volumes = "0"
        if "volumes" in exec.keys():
            volumes = str(len(exec["volumes"].keys()))
        row = [exec_name, image, path, platform, volumes]
        table.append(row)
    return table


registered_executions_path = "~/Projects/Docker/execution-flow/controller/registered-executions.json"
registered_executions = get_registered_executions(registered_executions_path)


@app.route("/")
def index():
    data = format_execution_table(registered_executions)
    return render_template("index.html", data=data)


@app.route("/<exec_name>")
def execution(exec_name):
    execution_config = registered_executions[exec_name]
    dockerfile_path = os.path.join(execution_config["dockerfile"], "Dockerfile")
    dockerfile = ""
    if os.path.exists(dockerfile_path):
        with open(dockerfile_path, 'r') as fh:
            dockerfile = fh.read()
    return render_template("execution.html", execution_name=exec_name, execution_config=json.dumps(execution_config, indent=2), dockerfile=dockerfile)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
