def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    return temp


def test_temperature() -> None:
    print("=== Garden Temperature ===")
    print("\n")

    valid_str = "25"
    invalid_str = "abc"

    print(f"Input data is '{valid_str}'")
    try:
        input_temperature(valid_str)
    except ValueError as e:
        print(f"{e}")
    else:
        print(f"Temperature is now {valid_str}°C")

    print("\n")
    print(f"Input data is '{invalid_str}'")
    try:
        input_temperature(invalid_str)
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    else:
        print(f"Temperature is now {valid_str}°C")
    finally:
        print("\n")
        print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
