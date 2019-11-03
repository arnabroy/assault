from typing import List, Dict


class Results:
    """
    Results handles calculating statistics based on a list of requests that were made.
    Here's an example of what the information will look like:

    Successful requests     3000
    Slowest                 0.010s
    Fastest                 0.001s
    Average                 0.003s
    Total time              2.400s
    Requests Per Minute     90000
    Requests Per Second     125
    """

    def __init__(self, total_time: float, requests: List[Dict]):
        self.total_time = total_time
        self.requests = requests

    def slowest(self) -> float:
        pass

    def fastest(self) -> float:
        pass

    def average_time(self) -> float:
        pass

    def total_time(self) -> float:
        pass

    def successful_requests(self) -> int:
        pass