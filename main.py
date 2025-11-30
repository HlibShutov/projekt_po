from ExecutionTimesBaseStatistics import ExecutionTimesBaseStatistics
from StatisicsLogger import StatisticsLogger

execution_times = [1.0, 1.5, 2.0]
execution_times_base_statistics: StatisticsLogger = ExecutionTimesBaseStatistics(execution_times)
execution_times_base_statistics.display_statistics()
