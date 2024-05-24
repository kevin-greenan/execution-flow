import requests
import os


def main():
    # input/output mounts to host
    in_p = "/home/executor/inputs/name.txt"
    out_p = "/home/executor/outputs/output.txt"

    name = "world"
    if os.path.exists(in_p):
        with open(in_p, 'r') as fh:
            name = fh.readlines()[0].strip()
        with open(out_p, 'w') as fh:
            fh.write(f"Hello, {name}!\n")
    else:
        print("file not found")


if __name__ == "__main__":
    main()
