"""
contextmanger는 __enter__와 __exit__ 두 개의 magic method로 구성된다. with문은 __enter__ method를 호출하고,
이 method가 무엇을 반환하든 as 이후에 지정된 변수에 할당된다. 사실 __enter__ method가 특정한 값을 반환할 필요는 없다.
설사 값을 반환한다 하더라도 필요하지않으면 변수에 할당하지 않아도 된다.
"""
import contextlib


run = print


def stop_database():
    run("systemctl stop postgresql.service")


def start_database():
    run("systemctl start postgresql.service")


class DBHandler:
    def __enter__(self):
        stop_database()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        start_database()


def db_backup():
    run("pg_dump database")


@contextlib.contextmanager
def db_handler():
    stop_database()
    yield
    start_database()


class dbhandler_decorator(contextlib.ContextDecorator):
    def __enter__(self):
        stop_database()

    def __exit__(self, exc_type, exc_val, exc_tb):
        start_database()


@dbhandler_decorator()
def offline_backup():
    run("pg_dump database")


def main():
    with DBHandler():
        db_backup()

    with db_handler():
        db_backup()

    offline_backup()


if __name__ == "__main__":
    main()