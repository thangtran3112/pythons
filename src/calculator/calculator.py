from addition import Addition


class Calculator:
    @classmethod
    def add(cls, num1, num2):
        return Addition.add(num1, num2)

    @classmethod
    def subtract(cls, num1, num2):
        return cls.add(num1, -num2)

    @classmethod
    def multiply(cls, num1, num2):
        res = 0
        for x in range(0, num2):
            res = cls.add(res, num1)
        return res
