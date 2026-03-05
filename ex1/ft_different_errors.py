def test_error_types():
    try:
        print("Testing ValueError...")
        int("abc")
    except ValueError as e:
        print(f"Caught ValueError: {e}")
        print()

    try:
        print("Testing ZeroDivisionError...")
        _ = 50 / 0
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")
        print()

    try:
        print("Testing FileNotFoundError...")
        file_test = "missing.txt"
        open(file_test, "r")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")
        print()

    try:
        print("Testing KeyError...")
        dict_test = {}
        a = dict_test["missing_plant"]
        print(a)
    except KeyError as e:
        print(f"Caught KeyError: {e}")
        print()

    try:
        print("Testing multiple errors together...")
        raise KeyError("a")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")
        print()


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===\n")
    test_error_types()
    print("All error types tested successfully!")
