class Calculator:
    last_result = 0

    @classmethod
    def update_last_result(cls, result):
        cls.last_result = result

    @classmethod
    def multiply(cls, a, b):
        res = a * b
        cls.update_last_result(res)
        return res

    @classmethod
    def add(cls, a, b):
        res = a + b
        cls.update_last_result(res)
        return res

    @classmethod
    def divide(cls, a, b):
        res = a // b
        cls.update_last_result(res)
        return res

    @classmethod
    def subtract(cls, a, b):
        res = a - b
        cls.update_last_result(res)
        return res