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
    dist = 0
    for i in range(len(route)):
        route_name.append(route[i].name)
        if i == 0:
            dist += calc_dist(queen_mary.lat, queen_mary.long, route[i].lat, route[i].long)
        else:
            dist += calc_dist(route[i - 1].lat, route[i - 1].long, route[i].lat, route[i].long)
    dist += calc_dist(route[len(route) - 1].lat, route[len(route) - 1].long, queen_mary.lat, queen_mary.long)
    # print(route_name, dist)
    if dist < best_dist:
        best_dist = dist
        best_route = route

leg_list = []
for i in range(len(best_route)):
    if i == 0:
        leg = "Leg " + str(i) + ": Queen Mary Hospital -> " + best_route[i].name
    else:
        leg = "Leg " + str(i) + ": " + best_route[i-1].name + " -> " + best_route[i].name
    leg_list.append(leg)
leg_list.append("Leg " + str(len(best_route)) + ": " + best_route[len(best_route) - 1].name + " -> Queen Mary Hospital")

# For print purposes only
print(leg_list)
print(best_dist)
