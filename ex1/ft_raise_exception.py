def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if temp > 41:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    elif temp < -1:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    else:
        return temp


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===")
    print("\n")

    valid_str = "25"
    invalid_str = "abc"
    hot_val = "100"
    cold_val = "-50"

    print(f"Input data is '{valid_str}'")
    try:
        input_temperature(valid_str)
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
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

    print("\n")
    print(f"Input data is '{hot_val}'")
    try:
        input_temperature(hot_val)
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")

    print("\n")
    print(f"Input data is '{cold_val}'")
    try:
        input_temperature(cold_val)
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")

    print("\n")
    print("All tests completed - program didn't crash")


if __name__ == "__main__":
    test_temperature()
