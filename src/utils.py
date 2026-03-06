import logging
import warnings

from rich.logging import RichHandler
from tqdm import TqdmExperimentalWarning


def setup_logging() -> None:
    """Set up logging configuration."""
    warnings.filterwarnings("ignore", category=TqdmExperimentalWarning)

    logging.basicConfig(
        level=logging.INFO,
        format="%(message)s",
        handlers=[
            RichHandler(
                rich_tracebacks=True,
                log_time_format="[%Y-%m-%d %H:%M:%S]",
            )
        ],
    )
