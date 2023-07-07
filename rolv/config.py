"""
    Provides content for rc.compile_config_block() based on content under
    src/config

    (Mostly hardcoded aliases/bash helper functions)
"""

import os
import stat
from pathlib import Path

from . import package
from .lib import insert, trim_newlines


# Module methods
# ====================================================================


def get_rc_config(path):
    """provide config to be put in the rc files. Called by rc.compile_config_block()"""
    src_dir = Path(package.get_src_path())

    block = ""

    shell = "bash"
    print(path)
    if "zsh" in path.name:
        shell = "zsh"

    for config_path in ["config/default_aliases_and_functions", "config/run"]:
        # read config file
        abs_path = src_dir.joinpath(config_path)
        with open(abs_path, "r") as f:
            content = f.read()

        # inject variables
        content = content.replace('__SHELL__', shell)

        # add to output
        block += insert(trim_newlines(content))

    return block


# ====================================================================
