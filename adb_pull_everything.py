from ppadb.client import Client
import subprocess
import json
import os


def make_searchstring(exclude):
    param = ""
    if not exclude:
        return param
    for i, name in enumerate(exclude):
        if i > 0:
            param += " "
        param += f"! -name '{name}'"
    param += " "
    return param


def filter_for_paths(filters, paths):
    if not filters:
        return paths

    def filter_in_path(name):
        for filter in filters:
            if filter in name:
                return True
        return False

    paths = [path for path in paths if not filter_in_path(path)]

    return paths


def main():
    with open("config.json") as f:
        config = json.load(f)

    subprocess.call("adb start-server")

    adb = Client(host="127.0.0.1", port=5037)
    devices = adb.devices()

    if len(devices) == 0:
        print("no device attached")
        quit()

    device = devices[0]

    target = input("Please input target path: ")
    try:
        if target[-1] != '"' and target[0] != '"':
            target = '"' + target + '"'
    except:
        target = os.getcwd()

    excludestring = make_searchstring(config["exclude"])
    md = str(config["maxdepth"])

    names = device.shell(f"find /sdcard/ {excludestring}-maxdepth {md} -mindepth 1")
    names = [name for name in names.split("\n") if name != ""]
    names = filter_for_paths(config["paths"], names)

    for name in names:
        if name[-1] != '"' and name[0] != '"':
            name = '"' + name + '"'
        print(f"{name}")
    if input(
        f"Press Enter to pull the listed files to your specified directory. {target}"
    ):
        subprocess.call(f"adb pull -p {name} {target}")
    input("Done, press any key to exit.")


if __name__ == "__main__":
    main()
