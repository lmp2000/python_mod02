class InvalidPlant(Exception):
    pass


def water_plants(plant_list: list) -> None:
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant:
                print(f"Watering {plant}")
            else:
                raise InvalidPlant(f"Cannot water {plant} - Invalid plant!")
    except InvalidPlant as e:
        print("Error:", e)
        return
    finally:
        print("Closing watering system (cleanup)")

    print("Watering completed successfully!")


def test_watering_system() -> None:
    print("=== Garden Watering System ===\n")

    glist = ["tomato", "lettuce", "carrots"]
    blist = ["tomato", None, "carrots"]

    print("Testin normal watering...")
    water_plants(glist)
    print()

    print("Testing with error...")
    water_plants(blist)
    print()

    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
