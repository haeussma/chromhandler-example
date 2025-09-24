import os
import subprocess as sp
import sys


def setup_colab(repo="chromhandler/chromhandler-example"):
    # install uv
    sp.run([sys.executable, "-m", "pip", "install", "-q", "uv"])

    # clone idempotent
    name = repo.split("/")[-1]
    if not os.path.exists(name):
        sp.run(["git", "clone", f"https://github.com/{repo}.git"])

    # cd into repo, if not already there
    if os.getcwd() != name:
        os.chdir(name)

    # sync deps
    sp.run(["uv", "sync", "--all-groups"])
