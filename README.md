# Execution Flow

Execution Flow is centralized Docker orchestration. Create containers and then "register" them in a `registered-executions.json` manifest, with a pointer to the Docker configuration on your filesystem. With very little modification, you can take any container and run it with Execution Flow.

## Usage

```
usage: exec.py [-h] [-e EXECUTION_NAME] [-r REGISTERED_EXECUTIONS]

options:
  -h, --help            show this help message and exit
  -e EXECUTION_NAME, --execution-name EXECUTION_NAME
                        Named target for execution
  -r REGISTERED_EXECUTIONS, --registered-executions REGISTERED_EXECUTIONS
                        /path/to/registered-executions.json
```

See the container defined in `sample/` to get a feel for how the process works. Execution Flow will expect containers to have `inputs` and `outputs` volumes mounted for getting data in and out of your execution environment. The pointer for the container defined in `sample/` may be found in `controller/registered-executions.json`.

## Future

The future of Execution Flow will have a web UI and backend database for managing registered executions and executing jobs on arbitrary data.
