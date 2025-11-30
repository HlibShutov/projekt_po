from abc import ABC, abstractmethod
from typing import List

class StatisticsLogger(ABC):
    @abstractmethod
    def display_statistics(self) -> None: pass

    @abstractmethod
    def get_execution_times(self) -> List[float]: pass
