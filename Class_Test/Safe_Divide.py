def safe_divide(a,b):
    try:
        return float(a)/float(b)
    except ZeroDivisionError as e:
        return f"Cannot divide by zero : {e}"
    except ValueError as e:
        return f"Invalid input : {e}"

print(safe_divide((input("Enter you 1st value : ")),((input("Enter you 2nd value : ")))))
