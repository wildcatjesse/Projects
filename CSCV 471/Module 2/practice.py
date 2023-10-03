
def color_map(states, adj_list, color_assignment, current_state_index=0):
    if current_state_index == len(states):
        return True
    colors = ['Red', 'Green', 'Blue', 'Yellow']
    for color in colors:
        if all(color != color_assignment[neighbor] for neighbor in adj_list[states[current_state_index]]):
            color_assignment[states[current_state_index]] = color
            if color_map(states, adj_list, color_assignment, current_state_index + 1):
                return True
            color_assignment[states[current_state_index]] = -1

    return False


# Define all the states and their neighbors (partial list, you would need to add all adjacencies)
adj_list = {
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

states = list(adj_list.keys())
color_assignment = {state: -1 for state in states}

if color_map(states, adj_list, color_assignment):
    for state, color in color_assignment.items():
        print(f"{state}:{color}")

# Define the USA map as a graph with states as nodes and adjacent states as edges.
usa_map = {
    'Washington': ['Oregon', 'Idaho'],
    'Oregon': ['Washington', 'Idaho', 'Nevada', 'California'],
    'Idaho': ['Washington', 'Oregon', 'Montana', 'Wyoming', 'Utah', 'Nevada'],
    'Montana': ['Idaho', 'North Dakota', 'South Dakota', 'Wyoming'],
    'North Dakota': ['Montana', 'Minnesota', 'South Dakota'],
    'South Dakota': ['North Dakota', 'Montana', 'Wyoming', 'Nebraska', 'Iowa', 'Minnesota'],
    'Wyoming': ['Montana', 'South Dakota', 'Idaho', 'Utah', 'Colorado', 'Nebraska'],
    'Nevada': ['Oregon', 'Idaho', 'Utah', 'Arizona'],
    'Utah': ['Idaho', 'Wyoming', 'Colorado', 'New Mexico', 'Arizona', 'Nevada'],
    'Arizona': ['Nevada', 'Utah', 'New Mexico'],
    'New Mexico': ['Arizona', 'Utah', 'Colorado', 'Oklahoma', 'Texas'],
    'Texas': ['New Mexico', 'Oklahoma', 'Arkansas', 'Louisiana'],
    'Oklahoma': ['New Mexico', 'Texas', 'Arkansas', 'Missouri'],
    'Arkansas': ['Texas', 'Oklahoma', 'Missouri', 'Tennessee', 'Mississippi', 'Louisiana'],
    'Louisiana': ['Texas', 'Arkansas', 'Mississippi'],
    'Minnesota': ['North Dakota', 'South Dakota', 'Iowa', 'Wisconsin'],
    'Iowa': ['Minnesota', 'South Dakota', 'Nebraska', 'Missouri', 'Wisconsin', 'Illinois'],
    'Missouri': ['Iowa', 'Nebraska', 'Kansas', 'Oklahoma', 'Arkansas', 'Illinois', 'Kentucky', 'Tennessee'],
    'Wisconsin': ['Minnesota', 'Iowa', 'Illinois', 'Michigan'],
    'Illinois': ['Wisconsin', 'Iowa', 'Missouri', 'Kentucky', 'Indiana'],
    'Kentucky': ['Illinois', 'Missouri', 'Indiana', 'Ohio', 'West Virginia', 'Virginia', 'Tennessee'],
    'Tennessee': ['Kentucky', 'Missouri', 'Arkansas', 'Mississippi', 'Alabama', 'Georgia', 'North Carolina'],
    'Mississippi': ['Arkansas', 'Louisiana', 'Tennessee', 'Alabama'],
    'Alabama': ['Tennessee', 'Mississippi', 'Georgia', 'Florida'],
    'Georgia': ['Alabama', 'Tennessee', 'North Carolina', 'South Carolina', 'Florida'],
    'North Carolina': ['Tennessee', 'Georgia', 'South Carolina', 'Virginia'],
    'South Carolina': ['North Carolina', 'Georgia'],
    'Florida': ['Alabama', 'Georgia']
}

# Define the initial state, which is an empty coloring of the states.
initial_state = {state: None for state in usa_map.keys()}


# Define the goal test, which checks if no two adjacent states have the same color.
def goal_test(state):
    for state1, neighbors in usa_map.items():
        for state2 in neighbors:
            if state[state1] == state[state2]:
                return False
    return True


# Define the successor function, which generates new states by assigning colors to uncolored states.
def successor_function(state):
    uncolored_states = [s for s, color in state.items() if color is None]
    if not uncolored_states:
        return []

    # Choose an uncolored state and assign a color to it.
    next_state = state.copy()
    state_to_color = uncolored_states[0]

    # Try each color and generate a new state for each color choice.
    for color in ['Red', 'Green', 'Blue', 'Yellow']:
        next_state[state_to_color] = color
        yield next_state


# Define a cost function (not used in this case, as it's a blind search).

# Implement Depth-First Search to find a valid coloring.
def depth_first_search(problem):
    frontier = [problem.initial_state]

    while frontier:
        state = frontier.pop()
        if problem.goal_test(state):
            return state
        frontier.extend(problem.successor_function(state))

    return None


# Solve the map coloring problem.
from collections import namedtuple

Problem = namedtuple('Problem', ['initial_state', 'goal_test', 'successor_function', 'cost_function'])
problem = Problem(initial_state, goal_test, successor_function, None)
solution = depth_first_search(problem)

# Print the solution.
if solution:
    print("Map Coloring Solution:")
    for state, color in solution.items():
        print(f"{state}: {color}")

else:
    print("No valid coloring found.")