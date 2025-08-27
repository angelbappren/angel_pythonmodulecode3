import sys, os
import logging.config
from pathlib import Path
import pytest

# project_root = angel_jpcode3
project_root = Path(__file__).resolve().parents[1]

# add src/ to sys.path
src_path = project_root / "src"
sys.path.insert(0, str(src_path))

@pytest.fixture(autouse=True, scope="session")
def configure_logging_for_tests():
    """Load logging.ini once for all tests, ensure logs folder exists."""
    logs_dir = project_root / "logs"
    logs_dir.mkdir(parents=True, exist_ok=True)

    

    ini_path = project_root / "logging.ini"
    
    #log_file = str((logs_dir / "app.log")).replace("\\", "\\\\")
    log_file = (logs_dir / "app.log").as_posix()


    logging.config.fileConfig(str(ini_path), disable_existing_loggers=False, defaults={"logfilename": log_file},)
