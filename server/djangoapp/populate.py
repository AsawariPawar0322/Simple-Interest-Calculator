from .models import CarMake, CarModel


def initiate():
    car_make_data = [
        {"name": "NISSAN", "description": "Great cars. Japanese technology"},
        {"name": "Mercedes", "description": "Luxury performance and prestige"},
        {"name": "Audi", "description": "Vorsprung durch Technik"},
        {"name": "Kia", "description": "Movement that inspires"},
        {"name": "Toyota", "description": "Reliable and efficient vehicles"},
    ]

    car_make_instances = []
    for data in car_make_data:
        car_make_instances.append(
            CarMake.objects.create(name=data['name'], description=data['description'])
        )

    # Create CarModel instances with the corresponding CarMake
    car_model_data = [
        {"name": "Pathfinder", "type": "SUV", "year": 2023, "car_make": car_make_instances[0], "dealer_id": 1},
        {"name": "Qashqai", "type": "SUV", "year": 2023, "car_make": car_make_instances[0], "dealer_id": 1},
        {"name": "X-Trail", "type": "SUV", "year": 2023, "car_make": car_make_instances[0], "dealer_id": 1},
        {"name": "A-Class", "type": "SUV", "year": 2023, "car_make": car_make_instances[1], "dealer_id": 1},
        {"name": "C-Class", "type": "Sedan", "year": 2023, "car_make": car_make_instances[1], "dealer_id": 1},
        {"name": "E-Class", "type": "Sedan", "year": 2023, "car_make": car_make_instances[1], "dealer_id": 1},
        {"name": "A4", "type": "Sedan", "year": 2023, "car_make": car_make_instances[2], "dealer_id": 1},
        {"name": "A5", "type": "Sedan", "year": 2023, "car_make": car_make_instances[2], "dealer_id": 1},
        {"name": "A6", "type": "Sedan", "year": 2023, "car_make": car_make_instances[2], "dealer_id": 1},
        {"name": "Sorrento", "type": "SUV", "year": 2023, "car_make": car_make_instances[3], "dealer_id": 1},
        {"name": "Carnival", "type": "SUV", "year": 2023, "car_make": car_make_instances[3], "dealer_id": 1},
        {"name": "Cerato", "type": "Sedan", "year": 2023, "car_make": car_make_instances[3], "dealer_id": 1},
        {"name": "Corolla", "type": "Sedan", "year": 2023, "car_make": car_make_instances[4], "dealer_id": 1},
        {"name": "Camry", "type": "Sedan", "year": 2023, "car_make": car_make_instances[4], "dealer_id": 1},
        {"name": "Kluger", "type": "SUV", "year": 2023, "car_make": car_make_instances[4], "dealer_id": 1},
    ]

    for data in car_model_data:
        CarModel.objects.create(
            name=data['name'],
            car_make=data['car_make'],
            type=data['type'],
            year=data['year'],
            dealer_id=data['dealer_id']
        )
