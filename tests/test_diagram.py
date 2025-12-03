from abc import ABC
from StatisicsLogger import StatisticsLogger
from ExecutionTimesBaseStatistics import ExecutionTimesBaseStatistics

def test_inherits():
    assert issubclass(ExecutionTimesBaseStatistics, StatisticsLogger)

def test_is_abstract():
    assert issubclass(StatisticsLogger, ABC)

def test_display_statistics(capsys):
    execution_times = [1.0, 1.5, 2.0]
    execution_times_base_statistics: StatisticsLogger = ExecutionTimesBaseStatistics(execution_times)
    execution_times_base_statistics.display_statistics()
    captured = capsys.readouterr()
    assert captured.out == "1.0, 1.5, 2.0\n"

def test_get_execution_times():
    execution_times = [1.0, 1.5, 2.0]
    execution_times_base_statistics: StatisticsLogger = ExecutionTimesBaseStatistics(execution_times)
    test_execution_times = execution_times_base_statistics.get_execution_times()
    assert test_execution_times == execution_times
