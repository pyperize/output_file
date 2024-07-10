from __future__ import annotations
from typing import TYPE_CHECKING
import src.pipe as pipe
from packages.output_file.config import OutputFileConfig, OutputFileConfigUI
from packages.output_file.function import OutputFileFunction
if TYPE_CHECKING:
    from src.manager import Manager
    from src.ui.common import ConfigPage

class OutputFilePipe(pipe.Pipe):
    cls_name: str = "Output File"
    cls_config: type[OutputFileConfig] = OutputFileConfig
    cls_function: type[OutputFileFunction] = OutputFileFunction

    def __init__(self, name: str, manager: Manager, config: OutputFileConfig) -> None:
        super().__init__(name, manager, config)
        self.config: OutputFileConfig = config

    def config_ui(self, manager: Manager, config_page: ConfigPage) -> OutputFileConfigUI:
        return OutputFileConfigUI(self, manager, config_page)

    def play(self, manager: Manager) -> None:
        if self.playing:
            return
        self.playing = True

    def stop(self, manager: Manager, result) -> None:
        if not self.playing:
            return
        self.playing = False
