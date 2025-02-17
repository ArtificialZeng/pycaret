from threading import RLock
from typing import Any, Optional

import pandas as pd

# Onw modules
from pycaret.internal.display import CommonDisplay


def _append_display_container(df: pd.DataFrame) -> None:
    global display_container
    display_container.append(df)


def _create_display(progress: int, verbose: bool, monitor_rows: Any) -> CommonDisplay:
    progress_args = {"max": progress}
    return CommonDisplay(
        verbose=verbose,
        html_param=html_param,
        progress_args=progress_args,
        monitor_rows=monitor_rows,
    )


def _get_setup_signature() -> Optional[str]:
    return globals().get("_setup_signature", None)


def _get_global(key: str, value: Any) -> Any:
    return globals().get(key, value)


def _set_global(key: str, value: Any) -> None:
    globals()[key] = value


def _get_context_lock() -> RLock:
    return globals()["_context_lock"]


def pull(pop=False) -> pd.DataFrame:  # added in pycaret==2.2.0
    """
    Returns latest displayed table.
    Parameters
    ----------
    pop : bool, default = False
        If true, will pop (remove) the returned dataframe from the
        display container.
    Returns
    -------
    pandas.DataFrame
        Equivalent to get_config('display_container')[-1]
    """
    if not display_container:
        return None
    return display_container.pop(-1) if pop else display_container[-1]
