from StatisicsLogger import StatisticsLogger
from ExecutionTimesBaseStatistics import ExecutionTimesBaseStatistics
from WithMeanStatisticsLogger import WithMeanStatisticsLogger

def test_display_statistics_mean(capsys):
    execution_times = [1.0, 1.5, 2.0]
    execution_times_base_statistics: StatisticsLogger = WithMeanStatisticsLogger(ExecutionTimesBaseStatistics(execution_times))
    execution_times_base_statistics.display_statistics()
    captured = capsys.readouterr()
    assert captured.out == "Mean: 1.5\n1.0, 1.5, 2.0\n"

def test_display_statistics_mean_empty(capsys):
    execution_times = []
    execution_times_base_statistics: StatisticsLogger = WithMeanStatisticsLogger(ExecutionTimesBaseStatistics(execution_times))
    execution_times_base_statistics.display_statistics()
    captured = capsys.readouterr()
    assert captured.out == "Mean: 0\n\n"
