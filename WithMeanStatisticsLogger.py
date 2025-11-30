from ExecutionTimesBaseStatistics import ExecutionTimesBaseStatistics

class WithMeanStatisticsLogger(ExecutionTimesBaseStatistics):
    def __init__(self, statistics_logger: ExecutionTimesBaseStatistics):
        self.statistics_logger: ExecutionTimesBaseStatistics = statistics_logger

    def display_statistics(self) -> None:
        execution_times = self.statistics_logger.get_execution_times()
        print(sum(execution_times) / float(len(execution_times)))
        self.statistics_logger.display_statistics()
