import csv
from itertools import permutations


def graph_create():
    graph = {}

    with open("route_data.csv", 'r') as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            start, end, duration_str, price = row
            hours, minutes = map(int, duration_str.split(":"))
            duration = hours * 60 + minutes
            price = float(price)

            if start not in graph:
                graph[start] = []
            graph[start].append((end, duration, price))

    return graph


def get_route(graph, locations):
    total_duration = 0
    total_price = 0.0

    for i in range(len(locations) - 1):
        start, end = locations[i], locations[i + 1]
        for next_stop, next_duration, next_price in graph.get(start, []):
            if next_stop == end:
                total_duration += next_duration
                total_price += next_price
                break
        else:
            return None, None

    return total_duration, total_price


def main():
    graph = graph_create()

    start_location = "Singapore (SIN)"
    
    # List of locations to visit
    desired_locations = [
        "Sydney (SYD)",
        "Cairns (CNS)",
        "Melbourne (MEL)",
    ]

    all_permutations = permutations(desired_locations)
    route_id = 1

    for perm in all_permutations:
        full_route = [start_location] + list(perm) + [start_location]
        total_duration, total_price = get_route(graph, full_route)
        
        if total_duration is not None:
            hours = total_duration // 60
            minutes = total_duration % 60

            print(f"Route ID: {route_id}")
            print(f"Route: {' -> '.join(full_route)}")
            print(f"Total Duration: {hours} hours {minutes} minutes")
            print(f"Total Price: {total_price:.2f}")
            print("-"*60)

        route_id += 1

if __name__ == "__main__":
    main()
