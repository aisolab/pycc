"""
엄밀히 말하면 iterable은 __iter__ magic method를 구현한 객체
iterator는 __next__ magic method를 구현한 객체
sequence는 __len__과 __getitem__을 구현되어있고, 첫 번째 index 0부터 시작하여 포함된 요소를
한 번에 하나씩 차례로 가져올 수 있는 object
iter() function은 object에 __iter__가 정의되어 있지 않으면 __getitem_을 찾고 없으면, TypeError를 발생시킨다.
"""
from datetime import timedelta, date


class DateRangeIterable:
    """An iterable that contains its own iterator object."""
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self._present_day = start_date

    def __iter__(self):
        return self

    def __next__(self):
        if self._present_day >= self.end_date:
            raise StopIteration
        today = self._present_day
        self._present_day += timedelta(days=1)
        return today


class DateRangeContainerIterable:
    """An range that builds its iteration through a generator."""
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date

    def __iter__(self):
        current_day = self.start_date
        while current_day < self.end_date:
            yield current_day
            current_day += timedelta(days=1)


class DateRangeSequence:
    """An range created by wrapping a sequence."""
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self._range = self._create_range()

    def _create_range(self):
        days = []
        current_day = self.start_date
        while current_day < self.end_date:
            days.append(current_day)
            current_day += timedelta(days=1)
        return days

    def __getitem__(self, day_no):
        return self._range[day_no]

    def __len__(self):
        return len(self._ragne)