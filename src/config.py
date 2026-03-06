import os
from pathlib import Path

# ---- Path Settings ----
_CONFIG_FILEPATH = Path(__file__).resolve()
SRC_ROOT = _CONFIG_FILEPATH.parent
PROJECT_ROOT = SRC_ROOT.parent

DATA_DIR = PROJECT_ROOT / "data"
MJLOG_DIR = DATA_DIR / "mjlogs"
JSON_LOGS_DIR = DATA_DIR / "json_logs"

# ---- Execution Settings ----
NUM_PROCESSES = os.cpu_count()
SUBPROCESS_TIMEOUT = 60
