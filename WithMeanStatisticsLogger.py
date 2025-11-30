from typing import List

def WithMeanStatistics(func):
    def wrapper(self) -> None:
        execution_times: List[float] = self.get_execution_times()
        print("Mean:", sum(execution_times) / float(len(execution_times)))
        func(self)
    return wrapper
