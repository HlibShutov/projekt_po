from StatisicsLogger import StatisticsLogger
from ExecutionTimesBaseStatistics import ExecutionTimesBaseStatistics
from WithSummaryStatisticsLogger import WithSummaryStatisticsLogger

def test_display_statistics_summary(capsys):
    execution_times = [1.0, 1.5, 2.0]
    execution_times_base_statistics: StatisticsLogger = WithSummaryStatisticsLogger(ExecutionTimesBaseStatistics(execution_times))
    execution_times_base_statistics.display_statistics()
    captured = capsys.readouterr()
    assert captured.out == "Records count: 3 Sum: 4.5 Min: 1.0 Max: 2.0\n1.0, 1.5, 2.0\n"

def test_display_statistics_summary_empty(capsys):
    execution_times = []
    execution_times_base_statistics: StatisticsLogger = WithSummaryStatisticsLogger(ExecutionTimesBaseStatistics(execution_times))
    execution_times_base_statistics.display_statistics()
    captured = capsys.readouterr()
    assert captured.out == "Records count: 0 Sum: 0 Min: 0 Max: 0\n\n"
