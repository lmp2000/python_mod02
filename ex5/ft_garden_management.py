class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class InvalidPlant(GardenError):
    pass


class Plant:
    def __init__(
        self, name: str, water_level: int, sunlight_hours: int
    ) -> None:
        self.name = name
        self.water_level = water_level
        self.sunlight_hours = sunlight_hours


class GardenManager:
    def __init__(self, water_tank: int = 10) -> None:
        self.plants: list[Plant] = []
        self.water_tank = water_tank

    def add_plant(
        self, name: str, water_level: int, sunlight_hours: int
    ) -> None:
        if not name.strip():
            raise PlantError("Plant name cannot be empty!")
        self.plants.append(Plant(name, water_level, sunlight_hours))

    def water_plants(self) -> None:
        print("Watering plants...")
        print("Opening watering system")
        try:
            for plant in self.plants:
                if (
                    plant is None
                    or not isinstance(plant, Plant)
                    or not plant.name
                ):
                    raise InvalidPlant(
                        f"Cannot water {plant} - Invalid plant!"
                    )
                if self.water_tank <= 0:
                    raise WaterError("Not enough water in tank")
                print(f"Watering {plant.name} - success")
        except (InvalidPlant, WaterError) as e:
            print(f"Error watering plants: {e}")
        finally:
            print("Closing watering system (cleanup)")
            print()

    def check_plant_health(self) -> None:
        print("Checking plant health...")
        for plant in self.plants:
            try:
                self._validate_plant_data(plant)
                print(
                    f"{plant.name}: healthy (water: {plant.water_level}, "
                    f"sun: {plant.sunlight_hours})"
                )
            except PlantError as e:
                print(f"Error checking {plant.name}: {e}")

    @staticmethod
    def _validate_non_negative(value: int) -> bool:
        return value >= 0

    def _validate_plant_data(self, plant: Plant) -> None:
        if not plant.name.strip():
            raise PlantError("Plant name cannot be empty!")
        if not (1 <= plant.water_level <= 10):
            if plant.water_level < 1:
                raise PlantError(
                    f"Water level {plant.water_level} is too low (min 1)"
                )
            raise PlantError(
                f"Water level {plant.water_level} is too high (max 10)"
            )
        if not (2 <= plant.sunlight_hours <= 12):
            if plant.sunlight_hours < 2:
                raise PlantError(
                    f"Sunlight hours {plant.sunlight_hours} is too low (min 2)"
                )
            raise PlantError(
                f"Sunlight hours {plant.sunlight_hours} is too high (max 12)"
            )


def test_garden_management() -> None:
    print("=== Garden Management System ===\n")

    manager = GardenManager(10)

    print("Adding plants to garden...")
    try:
        manager.add_plant("tomato", 5, 8)
        print("Added tomato successfully")
    except PlantError as e:
        print(f"Error adding plant: {e}")

    try:
        manager.add_plant("lettuce", 15, 6)
        print("Added lettuce successfully")
    except PlantError as e:
        print(f"Error adding plant: {e}")

    try:
        manager.add_plant("", 3, 6)
        print("Added  successfully")
    except PlantError as e:
        print(f"Error adding plant: {e}")
        print()

    manager.water_plants()

    manager.check_plant_health()

    print("\nTesting error recovery...")
    try:
        raise WaterError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")
        print()

    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
