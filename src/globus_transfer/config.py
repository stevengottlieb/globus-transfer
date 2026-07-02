"""Application configuration locations."""

from dataclasses import dataclass
from pathlib import Path

from platformdirs import PlatformDirs

APP_NAME = "gtransfer"
APP_AUTHOR = "globus-transfer"


@dataclass(frozen=True)
class AppPaths:
    """Filesystem locations used by the application."""

    config_dir: Path
    cache_dir: Path
    data_dir: Path


def get_app_paths() -> AppPaths:
    """Return platform-appropriate application directories."""
    dirs = PlatformDirs(appname=APP_NAME, appauthor=APP_AUTHOR)
    return AppPaths(
        config_dir=Path(dirs.user_config_dir),
        cache_dir=Path(dirs.user_cache_dir),
        data_dir=Path(dirs.user_data_dir),
    )
