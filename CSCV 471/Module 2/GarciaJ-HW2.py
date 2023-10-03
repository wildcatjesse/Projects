import time

# Dictionary representing the adjacency list of USA map
graph = {
    "Alabama": ["Florida", "Georgia", "Tennessee", "Mississippi"],
    "Alaska": [],
    "Arizona": ["California", "Nevada", "Utah", "Colorado", "New Mexico"],
    "Arkansas": ["Missouri", "Tennessee", "Mississippi", "Louisiana", "Texas", "Oklahoma"],
    "California": ["Oregon", "Nevada", "Arizona"],
    "Colorado": ["Wyoming", "Nebraska", "Kansas", "Oklahoma", "New Mexico", "Arizona", "Utah"],
    "Connecticut": ["New York", "Massachusetts", "Rhode Island"],
    "Delaware": ["Maryland", "Pennsylvania", "New Jersey"],
    "Florida": ["Alabama", "Georgia"],
    "Georgia": ["Florida", "Alabama", "Tennessee", "North Carolina", "South Carolina"],
    "Hawaii": [],
    "Idaho": ["Montana", "Wyoming", "Utah", "Nevada", "Oregon", "Washington"],
    "Illinois": ["Indiana", "Kentucky", "Missouri", "Iowa", "Wisconsin"],
    "Indiana": ["Michigan", "Ohio", "Kentucky", "Illinois"],
    "Iowa": ["Minnesota", "Wisconsin", "Illinois", "Missouri", "Nebraska", "South Dakota"],
    "Kansas": ["Nebraska", "Missouri", "Oklahoma", "Colorado"],
    "Kentucky": ["Indiana", "Ohio", "West Virginia", "Virginia", "Tennessee", "Missouri", "Illinois"],
    "Louisiana": ["Arkansas", "Mississippi", "Texas"],
    "Maine": ["New Hampshire"],
    "Maryland": ["Delaware", "Virginia", "West Virginia", "Pennsylvania"],
    "Massachusetts": ["Rhode Island", "Connecticut", "New York", "New Hampshire", "Vermont"],
    "Michigan": ["Ohio", "Indiana", "Wisconsin"],
    "Minnesota": ["Iowa", "South Dakota", "North Dakota", "Wisconsin"],
    "Mississippi": ["Louisiana", "Arkansas", "Tennessee", "Alabama"],
    "Missouri": ["Iowa", "Illinois", "Kentucky", "Tennessee", "Arkansas", "Oklahoma", "Kansas", "Nebraska"],
    "Montana": ["North Dakota", "South Dakota", "Wyoming", "Idaho"],
    "Nebraska": ["South Dakota", "Iowa", "Missouri", "Kansas", "Colorado", "Wyoming"],
    "Nevada": ["Oregon", "Idaho", "Utah", "Arizona", "California"],
    "New Hampshire": ["Maine", "Vermont", "Massachusetts"],
    "New Jersey": ["New York", "Delaware", "Pennsylvania"],
    "New Mexico": ["Colorado", "Oklahoma", "Texas", "Arizona"],
    "New York": ["New Jersey", "Pennsylvania", "Vermont", "Massachusetts", "Connecticut"],
    "North Carolina": ["Virginia", "Tennessee", "Georgia", "South Carolina"],
    "North Dakota": ["Montana", "South Dakota", "Minnesota"],
    "Ohio": ["Michigan", "Indiana", "Kentucky", "West Virginia", "Pennsylvania"],
    "Oklahoma": ["Kansas", "Missouri", "Arkansas", "Texas", "New Mexico", "Colorado"],
    "Oregon": ["Washington", "Idaho", "Nevada", "California"],
    "Pennsylvania": ["New York", "New Jersey", "Delaware", "Maryland", "West Virginia", "Ohio"],
    "Rhode Island": ["Massachusetts", "Connecticut"],
    "South Carolina": ["North Carolina", "Georgia"],
    "South Dakota": ["North Dakota", "Minnesota", "Iowa", "Nebraska", "Wyoming", "Montana"],
    "Tennessee": ["Kentucky", "Virginia", "North Carolina", "Georgia", "Alabama", "Mississippi", "Arkansas", "Missouri"],
    "Texas": ["Arkansas", "Louisiana", "Oklahoma", "New Mexico"],
    "Utah": ["Idaho", "Wyoming", "Colorado", "New Mexico", "Arizona", "Nevada"],
    "Vermont": ["New York", "New Hampshire", "Massachusetts"],
    "Virginia": ["Maryland", "Washington DC", "North Carolina", "Tennessee", "Kentucky", "West Virginia"],
    "Washington": ["Oregon", "Idaho"],
    "West Virginia": ["Ohio", "Pennsylvania", "Maryland", "Virginia", "Kentucky"],
    "Wisconsin": ["Minnesota", "Iowa", "Illinois", "Michigan"],
    "Wyoming": ["Montana", "South Dakota", "Nebraska", "Colorado", "Utah", "Idaho"],
    "Washington DC": ["Maryland", "Virginia"]
}

# List of colors
colors = ["Red", "Green", "Blue", "Yellow"]

# Dictionary to store the color assigned to each state
coloring = {}

# Initial state: No state is colored
for state in graph:
    coloring[state] = ""

# Goal test: Check if all states are colored and no adjacent states have the same color
def goal_test(coloring):
    for state, adjacent_states in graph.items():
        if coloring[state] == "":
            return False
        for adj_state in adjacent_states:
            if coloring[state] == coloring[adj_state]:
                return False
    return True

# Successor function: Find the next state to color and possible colors for that state
def successor(state, coloring):
    for color in colors:
        if all(color != coloring[adj_state] for adj_state in graph[state]):
            yield color

# Cost function: We can consider the cost as a constant (1) for each step
def cost():
    return 1

# Backtracking algorithm to find a solution
def color_map(state=0):
    if state == len(graph):
        return True

    current_state = list(graph.keys())[state]
    for color in successor(current_state, coloring):
        coloring[current_state] = color
        if color_map(state+1):
            return True
        coloring[current_state] = ""

    return False

# Measure time
start_time = time.time()

# Start the algorithm with the first state
if color_map():
    print("Solution found:")
    print(coloring)
else:
    print("No solution found")

# Print time taken
print("--- %s seconds ---" % (time.time() - start_time))
