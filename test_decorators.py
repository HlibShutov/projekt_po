from ExecutionTimesBaseStatistics import ExecutionTimesBaseStatistics
from StatisicsLogger import StatisticsLogger

def test_display_statistics(capsys):
    execution_times = [1.0, 1.5, 2.0]
    execution_times_base_statistics: StatisticsLogger = ExecutionTimesBaseStatistics(execution_times)
    execution_times_base_statistics.display_statistics()
    captured = capsys.readouterr()
    assert captured.out == "Mean: 1.5\nRecords count: 3 Sum: 4.5 Min: 1.0 Max: 2.0\n1.0, 1.5, 2.0\n"

def test_display_statistics_empty(capsys):
    execution_times = []
    execution_times_base_statistics: StatisticsLogger = ExecutionTimesBaseStatistics(execution_times)
    execution_times_base_statistics.display_statistics()
    captured = capsys.readouterr()
    assert captured.out == "Mean: 0\nRecords count: 0 Sum: 0 Min: 0 Max: 0\n\n"
