import os


def abspath(path):
    """Return an absolute path."""
    if not os.path.isabs(path):
        cwd = os.getcwdu()
        path = os.path.join(cwd, path)
    return os.path.normpath(path)


abspath("C:\\Users\\avenneman\\Documents\\ArcGIS\\Projects\\Python")
