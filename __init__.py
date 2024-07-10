from __future__ import annotations
from packages.output_file.config import OutputFileConfig, OutputFileConfigUI
from packages.output_file.function import OutputFileFunction
from packages.output_file.pipe import OutputFilePipe

from src.package.package import Package
from typing import TYPE_CHECKING, Iterable
if TYPE_CHECKING:
    from src.pipe import Pipe

class OutputFilePackage(Package):
    name: str = "Output File"
    _pipes: Iterable[type[Pipe]] = [OutputFilePipe]
    dependencies: dict[str, Package] = {}
