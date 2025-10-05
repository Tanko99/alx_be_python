def safe_divide(numerator, denomenator):
    try:
        num = float(numerator)
        den = float(denomenator)
        result = num / den
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        return f"Error: Cannot divide by zero"
    except ValueError:
        return f"Error: Please enter numeric values"
        

