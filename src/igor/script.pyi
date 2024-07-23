from __future__ import annotations
from . import LOG as LOG
from _typeshed import Incomplete


class Script:
    log_levels: Incomplete
    parser: Incomplete

    def __init__(
        self, description: Incomplete | None = ..., filetype: str = ...
    ) -> None:
        ...

    def run(self, *args, **kwargs) -> None:
        ...

    def plot_wave(self, args, wave, title: Incomplete | None = ...) -> None:
        ...

    def display_plots(self) -> None:
        ...
