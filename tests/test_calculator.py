from calculator.calculator import Calculator


class TestCalculator:
    def test_add(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 5555
        assert result == expected

    def test_subtract(self):
        # arrange
        a = 3333
        b = 2222
        cal = Calculator()

        # act
        result = cal.subtract(a, b)

        # assert
        expected = 1111
        assert result == expected

    def test_multiply(self):
        # arrange
        a = 2222
        b = 3
        cal = Calculator()

        # act
        result = cal.multiply(a, b)

        # assert
        expected = 6666
        assert result == expected

    def test_divide(self):
        # arrange
        a = 6666
        b = 3
        cal = Calculator()

        # act
        result = cal.divide(a, b)

        # assert
        expected = 2222
        assert result == expected

    def test_divide_by_zero(self):
        # arrange
        a = 6666
        b = 0
        cal = Calculator()

        # act and assert
        try:
            cal.divide(a, b)
            assert False  # if exception is not raised, test fails
        except ZeroDivisionError:
            assert True
