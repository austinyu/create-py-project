"""The `version` module holds the version information for ujson5."""

from scaffoldpy._version import __version__

__all__ = ["VERSION"]

VERSION: str = __version__
"""The version of ujson5."""


def version_short() -> str:  # pragma: no cover
    """Return the `major.minor` part of ujson5 version.

    It returns '2.1' if scaffoldpy version is '2.1.1'.
    """
    return ".".join(VERSION.split(".")[:2])


def version_info() -> str:
    """Return complete version information for scaffoldpy and its dependencies."""
    import platform  # pylint: disable=C0415
    import sys  # pylint: disable=C0415

    info = {
        "scaffoldpy version": VERSION,
        "python version": sys.version,
        "platform": platform.platform(),
    }
    info = {k: str(v).replace("\n", " ") for k, v in info.items()}
    return "\n".join(f"{k}: {v}" for k, v in info.items())
