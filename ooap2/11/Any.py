from General import General


class Any(General):

    def print_errors(self):
        print(self.errors)


if __name__ == '__main__':
    obj = Any()
    print(obj.print())
    print(obj.serialize())
