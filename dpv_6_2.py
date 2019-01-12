import numpy as np


def hotel_cost(hotel_list):
    n = len(hotel_list)
    total_cost = [0] * n
    hotel_stops = []
    for i in range(1, n):
        min_j = np.inf
        for j in range(i):
            temp = (200 - (hotel_list[i] - hotel_list[j]))**2 + total_cost[j]
            if temp < min_j:
                min_j = temp
        total_cost[i] = min_j
    return total_cost[-1]


if __name__ == '__main__':
    hotels = [100, 210, 250, 540, 699]
    print(hotel_cost(hotels))
