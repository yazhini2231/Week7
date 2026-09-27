def is_vehicle_available(vehicle):
    return bool(vehicle.get("available", False))


def test_vehicle_available():
    vehicle = {"id": 1, "name": "Toyota Innova", "available": True}
    assert is_vehicle_available(vehicle) is True


def test_vehicle_unavailable():
    vehicle = {"id": 2, "name": "Honda City", "available": False}
    assert is_vehicle_available(vehicle) is False
