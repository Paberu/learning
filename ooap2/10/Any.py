from General import General


class Any(General):

    def __init__(self):
        super().__init__()
        self.errors = 'None errors here'

    # можно переопределять, системе всё равно
    def print(self):
        print('str from Any')
        super().print()

    # всё, что даёт декоратор @final - это предупреждение от IDE:
    # 'General.serialize' is marked as '@final' and should not be overridden
    # гарантированной защиты от несанкционированного переопределения в Python нет
    def serialize(self):
        print('Overriding General method.')
        super().serialize()


if __name__ == '__main__':
    obj = Any()
    print(obj.check_type(General))
    print(obj.get_real_type())
    print(str(obj))
    print(obj.serialize())
