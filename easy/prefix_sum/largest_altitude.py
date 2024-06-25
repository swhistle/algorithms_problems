def largest_altitude(gain: list) -> int:
    current_altitude = 0
    max_altitude = current_altitude

    for point_altitude in gain:
        current_altitude += point_altitude

        if current_altitude > max_altitude:
            max_altitude = current_altitude

    print(max_altitude)
    return max_altitude


example_1 = [-5,1,5,0,-7]
result_1 = largest_altitude(example_1)


example_2 = [-4,-3,-2,-1,4,3,2]
result_2 = largest_altitude(example_2)