from typing import List

def WithSummaryStatistics(func):
    def wrapper(self) -> None:
        execution_times: List[float] = self.get_execution_times()
        print(
            "Records count:", len(execution_times),
            "Sum:", sum(execution_times),
            "Min:", min(execution_times),
            "Max:", max(execution_times),
        )
        func(self)
    return wrapper
