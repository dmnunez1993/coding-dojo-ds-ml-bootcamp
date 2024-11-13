"""
Herramientas de utilidades Git.
"""
import subprocess


def get_repo_root():
    return subprocess.check_output(
        'git rev-parse --show-toplevel'.split(), encoding='utf-8'
    ).strip()


def get_repo_file_path(rel_path):
    repo_root = get_repo_root()
    return f"{repo_root}/{rel_path}"
