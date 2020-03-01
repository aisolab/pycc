def test_generator(start=0):
    while True:
        yield start
        start += 1


a = test_generator()
next(a)
b = a.close()
