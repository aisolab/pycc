"""
sequence는 __getitem__과 __len__을 모두 구현하는 object
예시로는 list, tuple, str
"""
class Items:
    def __init__(self, *values):
        self._values = list(values)

    def __len__(self):
        return len(self._values)

    def __getitem__(self, item):
        return self._values.__getitem__(item)
