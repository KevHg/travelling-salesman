from math import sin, cos, atan2, sqrt, pi
from itertools import permutations
from sys import float_info


class Clinic:
    name = ""
    lat = 0
    long = 0

    def __init__(self, name, lat, long):
        self.name = name
        self.lat = lat
        self.long = long


def calc_dist(lat1, long1, lat2, long2):
    rad = pi / 180.0
    d_long = (long2 - long1) * rad
    d_lat = (lat2 - lat1) * rad
    a = pow(sin(d_lat / 2.0), 2) + cos(lat1 * rad) * cos(lat2 * rad) * pow(sin(d_long / 2.0), 2)
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = 6371 * c
    return distance


queen_mary = Clinic("Queen Mary Hospital", 22.243243, 114.153765)
hku_clinic = Clinic("HKU Clinic", 30, 80)
central_clinic = Clinic("Central Clinic", 40, 120)
kowloon_clinic = Clinic("Kowloon Clinic", 80, 60)
airport_clinic = Clinic("Airport Clinic", 110, 150)
clinic_list = [hku_clinic, central_clinic, kowloon_clinic, airport_clinic]

all_routes = list(permutations(clinic_list))
best_route = ()
best_dist = float_info.max
for route in all_routes:
    route_name = []
    distance = 0
    for i in range(len(route)):
        route_name.append(route[i].name)
        if i == 0:
            distance += calc_dist(queen_mary.lat, queen_mary.long, route[i].lat, route[i].long)
        else:
            distance += calc_dist(route[i - 1].lat, route[i - 1].long, route[i].lat, route[i].long)
    distance += calc_dist(route[len(route) - 1].lat, route[len(route) - 1].long, route[i].lat, route[i].long)
    print(route_name, distance)
    if distance < best_dist:
        best_dist = distance
        best_route = route

for clinic in best_route:
    print(clinic.name, end=', ')
print(best_dist)
