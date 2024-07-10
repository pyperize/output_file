from __future__ import annotations
from packages.output_file.config import OutputFileConfig
from src.pipe.function import IO, Function

class OutputFileInput(IO):
    data: bytes # = b""

class OutputFileFunction(Function):
    cls_input: type[OutputFileInput] = OutputFileInput
    cls_output: type[IO] = IO

    def __init__(self, config: OutputFileConfig) -> None:
        self.config: OutputFileConfig = config

    def __call__(self, input: OutputFileInput) -> IO:
        with open(self.config.filename, "ab") as of:
            of.write(input.data)
        return IO()
