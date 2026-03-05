def check_temperature(temp_str: str) -> int:
    try:
        temp = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
        return None

    if temp > 40:
        print(f"Error: {temp}ºC is too hot for plants (max 40ºC)")
        return None
    elif temp < 0:
        print(f"Error: {temp}ºC is too cold for plants (min 0ºC)")
        return None
    else:
        print(f"Temperature {temp}ºC is perfect for plants!")
        return temp


def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===\n")
    inputs = ["25", "abc", "100", "-50"]
    for str in inputs:
        print(f"Testing temperature: {str}")
        check_temperature(str)
        print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
