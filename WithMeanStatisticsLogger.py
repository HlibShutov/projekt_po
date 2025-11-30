from ExecutionTimesBaseStatistics import ExecutionTimesBaseStatistics


def WithMeanStatistics(func):
    def wrapper(self: ExecutionTimesBaseStatistics) -> None:
        execution_times = self.get_execution_times()
        print("Mean:", sum(execution_times) / float(len(execution_times)))
        func()
    return wrapper
