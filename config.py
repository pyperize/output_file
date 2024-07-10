from __future__ import annotations
import flet as ft
import src.pipe as pipe
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.manager import Manager
    from src.ui.common import ConfigPage
    from packages.output_file.pipe import OutputFilePipe

class OutputFileConfig(pipe.Config):
    filename: str = "./../../output.txt"

class OutputFileConfigUI(pipe.ConfigUI):
    def __init__(self, instance: OutputFilePipe, manager: Manager, config_page: ConfigPage) -> None:
        super().__init__(instance, manager, config_page)
        self.instance: OutputFilePipe = instance
        self.content: ft.Column = ft.Column([
            ft.TextField(self.instance.config.filename, label="File name and path", border_color="grey"),
        ])

    def dismiss(self) -> None:
        self.instance.config.filename = self.content.controls[0].value
