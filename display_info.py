def __init__(car_instance, make, model, year):
     # Initialize car information
    car_instance.make = make
    car_instance.model = model
    car_instance.year = year

def display_info(car_instance):
    # Print car information
    print(f"Make: {car_instance.make}, Model: {car_instance.model}, Year: {car_instance.year}")
