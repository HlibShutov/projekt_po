from ExecutionTimesBaseStatistics import ExecutionTimesBaseStatistics


class WithSummaryStatisticsLogger(ExecutionTimesBaseStatistics):
    def __init__(self, statistics_logger: ExecutionTimesBaseStatistics):
        self.statistics_logger: ExecutionTimesBaseStatistics = statistics_logger

    def display_statistics(self) -> None:
        execution_times = self.statistics_logger.get_execution_times()
        print(
            "Records count:", len(execution_times),
            "Sum:", sum(execution_times),
            "Min:", min(execution_times),
            "Max:", max(execution_times),
        )
        self.statistics_logger.display_statistics()
