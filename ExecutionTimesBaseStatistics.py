from typing import List
from StatisicsLogger import StatisticsLogger
from WithMeanStatisticsLogger import WithMeanStatistics
from WithSummaryStatisticsLogger import WithSummaryStatistics

class ExecutionTimesBaseStatistics(StatisticsLogger):
    def __init__(self, execution_times: List[float]):
        self.execution_times: List[float] = execution_times

    @WithMeanStatistics
    @WithSummaryStatistics
    def display_statistics(self) -> None:
        print(*self.execution_times, sep =', ')

    def get_execution_times(self) -> List[float]:
        return self.execution_times
