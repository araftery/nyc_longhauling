import numpy as np
import math

# get lat and lng grid nums
min_lat, max_lat = 40.477399, 40.917577
min_lng, max_lng = -74.25909, -73.700009

lat_ticks = 150
lng_ticks = 150

lat_coords = np.arange(min_lat, max_lat, (max_lat - min_lat) / lat_ticks)
lng_coords = np.arange(min_lng, max_lng, (max_lng - min_lng) / lng_ticks)

lat_chunk_size = (max_lat - min_lat) / lat_ticks
lng_chunk_size = (max_lng - min_lng) / lng_ticks

def get_lat_grid(lat):
    return int(math.floor ((lat - min_lat) / lat_chunk_size))


def get_lng_grid(lng):
    return int(math.floor ((lng - min_lng) / lng_chunk_size))
