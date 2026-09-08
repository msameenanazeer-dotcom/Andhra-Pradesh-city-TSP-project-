import heapq

# Andhra Pradesh cities
cities = [
    "Visakhapatnam",
    "Vijayawada",
    "Guntur",
    "Tirupati",
    "Nellore",
    "Kurnool",
    "Kadapa",
    "Rajahmundry"
]

# Approximate distances in km
distance = {
    ("Visakhapatnam", "Vijayawada"): 350,
    ("Visakhapatnam", "Guntur"): 400,
    ("Visakhapatnam", "Tirupati"): 760,
    ("Visakhapatnam", "Nellore"): 670,
    ("Visakhapatnam", "Kurnool"): 650,
    ("Visakhapatnam", "Kadapa"): 650,
    ("Visakhapatnam", "Rajahmundry"): 190,

    ("Vijayawada", "Guntur"): 35,
    ("Vijayawada", "Tirupati"): 410,
    ("Vijayawada", "Nellore"): 280,
    ("Vijayawada", "Kurnool"): 350,
    ("Vijayawada", "Kadapa"): 430,
    ("Vijayawada", "Rajahmundry"): 160,

    ("Guntur", "Tirupati"): 390,
    ("Guntur", "Nellore"): 260,
    ("Guntur", "Kurnool"): 330,
    ("Guntur", "Kadapa"): 410,
    ("Guntur", "Rajahmundry"): 190,

    ("Tirupati", "Nellore"): 130,
    ("Tirupati", "Kurnool"): 360,
    ("Tirupati", "Kadapa"): 220,
    ("Tirupati", "Rajahmundry"): 500,

    ("Nellore", "Kurnool"): 390,
    ("Nellore", "Kadapa"): 290,
    ("Nellore", "Rajahmundry"): 410,

    ("Kurnool", "Kadapa"): 210,
    ("Kurnool", "Rajahmundry"): 500,

    ("Kadapa", "Rajahmundry"): 430
}


def get_distance(a, b):

    if a == b:
        return 0

    if (a, b) in distance:
        return distance[(a, b)]

    if (b, a) in distance:
        return distance[(b, a)]

    return 999999


# Heuristic:
# Minimum distance from current city
# to any unvisited city.
def heuristic(current, unvisited):

    if not unvisited:
        return get_distance(current, start_city)

    return min(
        get_distance(current, city)
        for city in unvisited
    )


def a_star(start, selected_cities):

    global start_city
    start_city = start

    # Priority queue
    queue = []

    # state:
    # (f, g, current_city, visited, route)

    initial_state = (
        heuristic(start, set(selected_cities) - {start}),
        0,
        start,
        frozenset([start]),
        [start]
    )

    heapq.heappush(queue, initial_state)

    while queue:

        f, g, current, visited, route = heapq.heappop(queue)

        # All cities visited
        if len(visited) == len(selected_cities):

            total = g + get_distance(
                current,
                start
            )

            return route + [start], total

        unvisited = set(selected_cities) - set(visited)

        for city in unvisited:

            new_g = g + get_distance(
                current,
                city
            )

            new_visited = visited | {city}

            new_h = heuristic(
                city,
                unvisited - {city}
            )

            new_f = new_g + new_h

            heapq.heappush(
                queue,
                (
                    new_f,
                    new_g,
                    city,
                    frozenset(new_visited),
                    route + [city]
                )
            )

    return None, None


# -----------------------------
# Main program
# -----------------------------

print("\nANDHRA PRADESH TSP")
print("===================")

print("\nSelect cities:\n")

for i, city in enumerate(cities, 1):
    print(i, "-", city)


choice = input(
    "\nEnter city numbers "
    "(example: 1 2 3 4): "
)

numbers = list(
    map(int, choice.split())
)

selected_cities = [
    cities[i - 1]
    for i in numbers
]


start_city = selected_cities[0]

route, total_distance = a_star(
    start_city,
    selected_cities
)


print("\nSelected Cities:")
print("----------------")

for city in selected_cities:
    print(city)


print("\nA* Best Route:")
print("--------------")

print(" -> ".join(route))

print(
    "\nTotal Distance:",
    total_distance,
    "km"
)
