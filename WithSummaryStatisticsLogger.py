from typing import List

def WithSummaryStatistics(func):
    def wrapper(self) -> None:
        execution_times: List[float] = self.get_execution_times()
        print(
            "Records count:", len(execution_times),
            "Sum:", sum(execution_times),
            "Min:", 0 if len(execution_times) == 0 else min(execution_times),
            "Max:", 0 if len(execution_times) == 0 else max(execution_times),
        )
        func(self)
    return wrapper
