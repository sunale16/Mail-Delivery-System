import csv
from hashtable import HashMap, Item

csv_file_path = '/WGUPS Package File.csv'

with open ("WGUPS-PackageFile-Data.csv") as packagefile:

    read_csv = csv.reader(packagefile, delimiter=',')

    hash_map = HashMap()
    first_delivery = []
    second_delivery = []
    third_delivery = []

    for row in read_csv:
        package_id = row[0]
        address = row[1]
        city = row[2]
        state = row[3]
        zip = row[4]
        delivery = row[5]
        size = row[6]
        note = row[7]
        delivery_start = ''
        address_location = ''
        delivery_status = 'At hub'

        package_data = [id, address_location, address, city, state, zip, delivery, size,
            note, delivery_start, delivery_status]

        key = int(package_id)
        value = package_data

        item = Item(key, value)
        hash_map.put(item)



    def get_first_delivery():
        return first_delivery

    def get_second_delivery():
        return second_delivery

    def get_third_delivery():
        return third_delivery

    def get_hash_map():
        return hash_map

