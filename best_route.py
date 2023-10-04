import csv


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


def main():
    graph = graph_create()
    print(graph)


if __name__ == "__main__":
    main()
