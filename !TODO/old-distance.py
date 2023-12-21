import csv
import datetime

with open('./WGUPS-Distances.csv') as csv_1:
    distance_csv = list(csv.reader(csv_1, delimiter=','))
with open('./WGUPS-DistanceNames.csv') as csv_2:
    names_distance_csv = list(csv.reader(csv_2, delimiter=","))

    def get_address():
        return names_distance_csv

    def get_distance(row_value, col_value, distance_sum):
        distance = distance_csv[row_value][col_value]
        if distance == '':
            distance = distance_csv[col_value][row_value]
        distance_sum += float(distance)
        return distance_sum

    def get_current_distance(row_value, col_value, distance_sum):
        distance = distance_csv[row_value][col_value]
        if distance == '':
            distance = distance_csv[col_value][row_value]
        return float(distance)


    first_time_list = ['8:00:00']
    second_time_list = ['9:05:00']
    third_time_list = ['11:00:00']


    def get_time(distance, truck_list):
        new_time = distance / 18
        distance_in_minutes = '{0:02.0f}:{1:02.0f}'.format(
            *divmod(new_time * 60, 60))
        final_time = distance_in_minutes + ':00'
        truck_list.append(final_time)
        total = datetime.timedelta()
        for i in truck_list:
            (hrs, mins, secs) = i.split(':'
)            total += datetime.timedelta(hours=int(hrs),
                                        minutes=int(mins),
                                        seconds=int(secs))
        return total

    first_truck = []
    first_truck_indices = []
    second_truck = []
    second_truck_indices = []
    third_truck = []
    third_truck_indices = []

        def get_shortest_distance(truck_distance_list, truck_number, current_location):
            shortest_distance = 100
            shortest_distance_index = 0
            for i in range(len(truck_distance_list)):
                if truck_distance_list[i] < shortest_distance and i not in truck_number:
                    shortest_distance = truck_distance_list[i]
                    shortest_distance_index = i
            truck_number.append(shortest_distance_index)
            current_location = shortest_distance_index
            return current_location
