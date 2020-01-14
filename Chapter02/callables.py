"""
magic method __call__을 이용하면 object를 function처럼 call 할 수 있다.
"""
from collections import defaultdict


class CallCount:
    """
    >>> cc = CallCount()
    >>> cc(1)
    1
    >>> cc(2)
    1
    >>> cc(1)
    2
    >>> cc(1)
    3
    >>> cc("something")
    1
    >>> callable(cc)
    True
    """
    def __init__(self):
        self._counts = defaultdict(int)

    def __call__(self, argument):
        self._counts[argument] += 1
        return self._counts[argument]
