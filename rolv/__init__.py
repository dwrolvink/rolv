from . import rc, executables


def version():
    print("0.0.1")


def install():
    print("\n")
    rc.set_rc_files()
    executables.sync_executables()

    print("\nTo make sure the ENV is up to date, be sure to open a new terminal window, or run (one of) the following command(s):")
    for path in rc.get_rc_file_paths():
        print(f"  source {path.as_posix()}")
    print("\nDone.")
    print("\n")
