class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def plant_error() -> None:
    print("Testing PlantError...")

    tomato_quality = 50

    if tomato_quality < 100:
        raise PlantError("The tomato plant is wilting!")
    else:
        print("The tomato is fine")


def water_error() -> None:
    print("Testing WaterError...")

    liters = 50

    if liters < 100:
        raise WaterError("Not enough water in the tank!")
    else:
        print("The water is fine")


def garden_errors() -> None:
    print("Testing catching all garden errors...")

    messages = []

    tomato_quality = 50
    liters = 50

    if tomato_quality < 100:
        messages.append("The tomato plant is wilting!")

    if liters < 100:
        messages.append("Not enough water in the tank!")

    if len(messages) == 0:
        print("The garden is fine")
    else:
        raise GardenError(*messages)


def main() -> None:
    print("=== Custom Garden Errors Demo ===\n")

    try:
        plant_error()
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print()

    try:
        water_error()
    except WaterError as e:
        print(f"Caught WaterError: {e}")
        print()

    try:
        garden_errors()
    except GardenError as e:
        for error_message in e.args:
            print(f"Caught a garden error: {error_message}")
        print()

    print("All custom error types work correctly")


if __name__ == "__main__":
    main()
