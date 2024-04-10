from RationalNumber import RationalNumber


class Void(RationalNumber):

    def __init__(self):
        pass


if __name__ == '__main__':
    check_object = RationalNumber
    check_finals = Void

    if hasattr(check_object, '__final__'):
        print(True)