"""
    개방/폐쇄 원칙(Open/Close Principle)은 모듈이 개방되어 있으면서도 폐쇄되어야 한다는 원칙이며,
    클래스를 디자인할 때는 유지보수가 쉽도록 로직을 캡슐화하여 확장에는 개방되고 수정에는 폐쇄되도록 해야한다.
    새로운 기능을 추가하다가 기존 코드를 수정했다면 그것은 기존 로직이 잘못 디자인되었다는 것을 뜻하며,
     이상적으로는 요구사항이 변경되면 새로운 기능을 구현하기 위한 모듈만 확장을 하고 기존 코드는 수정을 하면 안 된다.
"""
class Event:
    def __init__(self, raw_data):
        self.raw_data = raw_data

    @staticmethod
    def meets_condition(event_data: dict):
        return False


class UnknownEvent(Event):
    """A type of event that cannot be identified from its data"""


class LoginEvent(Event):
    @staticmethod
    def meets_condition(event_data: dict):
        return (event_data["before"]["session"] == 0 and event_data["after"]["session"] == 1)


class LogoutEvent(Event):
    @staticmethod
    def meets_condition(event_data: dict):
        return (event_data["before"]["session"] == 1 and event_data["after"]["session"] == 0)


class SystemMonitor:
    """Identify events that occurred in the system
        >>> l1 = SystemMonitor({"before": {"session": 0}, "after": {"session": 1}})
        >>> l1.identify_event().__class__.__name__
        'LoginEvent'
        >>> l2 = SystemMonitor({"before": {"session": 1}, "after": {"session": 0}})
        >>> l2.identify_event().__class__.__name__
        'LogoutEvent'
        >>> l3 = SystemMonitor({"before": {"session": 1}, "after": {"session": 1}})
        >>> l3.identify_event().__class__.__name__
        'UnknownEvent'
    """
    def __init__(self, event_data):
        self.event_data = event_data

    def identify_event(self):
        for event_cls in Event.__subclasses__():
            try:
                if event_cls.meets_condition(self.event_data):
                    return event_cls(self.event_data)
            except KeyError:
                continue
        return UnknownEvent(self.event_data)
