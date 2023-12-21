import csv
import datetime

# Load distance data into a 2D list and address dictionary
distances = []
address_dict = {}
with open('./WGUPS-Distances.csv') as csv_1:
    for row in csv.reader(csv_1, delimiter=','):
        distances.append([int(dist) if dist else 0 for dist in row])

with open('./WGUPS-DistanceNames.csv') as csv_2:
    names_distance_csv = list(csv.reader(csv_2, delimiter=","))
    for i, row in enumerate(names_distance_csv):
        for address in row:
            address_dict[address] = i

# Define the Package class
class Package:
    def __init__(self, id, address, priority, has_partner, delivery_deadline):
        self.id = id
        self.address = address
        self.priority = priority
        self.has_partner = has_partner
        self.delivery_deadline = delivery_deadline
        self.delivery_time = None

# Load package data (replace with your actual data loading)
#!TODO: custom package loading onto trucks?

# ...

# Delivery algorithm
def deliver_packages():
    truck_lists = [
        list(load_packages_onto_truck(1)),  # Implement loading logic for each truck
        list(load_packages_onto_truck(2)),
        list(load_packages_onto_truck(3)),
    ]
    current_locations = [0, 0, 0]  # All trucks start at the hub
    current_times = [
        datetime.datetime.strptime("8:00:00", "%H:%M:%S"),
        datetime.datetime.strptime("9:05:00", "%H:%M:%S"),
        datetime.datetime.strptime("11:00:00", "%H:%M:%S"),
    ]

    while any(truck_list for truck_list in truck_lists):
        for truck_index, (truck_list, current_location, current_time) in enumerate(
            zip(truck_lists, current_locations, current_times)
        ):
            if truck_list:
                closest_package = find_closest_package(truck_list, current_location)
                travel_time = calculate_travel_time(current_location, closest_package.address)
                current_time += datetime.timedelta(minutes=travel_time)
                closest_package.delivery_time = current_time
                print(f"Delivered package {closest_package.id} at {current_time}")
                truck_list.remove(closest_package)
                current_locations[truck_index] = closest_package.address
