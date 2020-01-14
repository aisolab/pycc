"""
예외의 type을 변경할 때는 항상 raise <e> from <o> 구문을 사용
"""
class InternalDataError(Exception):
    """An exception with the data of our domain problem."""


def process(data_dictionary, record_id):
    try:
        return data_dictionary[record_id]
    except KeyError as e:
        raise InternalDataError("Record not present") from e
