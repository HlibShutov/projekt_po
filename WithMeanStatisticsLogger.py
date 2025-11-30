from typing import List

def WithMeanStatistics(func):
    def wrapper(self) -> None:
        execution_times: List[float] = self.get_execution_times()
        if (len(execution_times) != 0): print("Mean:", sum(execution_times) / float(len(execution_times)))
        else: print("Mean: 0")
        func(self)
    return wrapper
