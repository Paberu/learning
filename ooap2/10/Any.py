from General import General


class Any(General):

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
    object = Any()
    # print(getattr(object, '__final__'))
    print(object.print())
    print(object.serialize())
