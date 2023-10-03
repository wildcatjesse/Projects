def get_successors(state_index, color_index, max_color_index=4):
    if color_index < max_color_index:
        yield state_index, color_index + 1
    if state_index < len(states) - 1:
        yield state_index + 1, 0

def dfs_coloring(states, adj_list, color_assignment):
    colors = ["red", "green", "yellow", "blue"]
    stack = [(0, 0, 0)]
    while stack:
        current_state_index, color_index, cost = stack.pop()
        if current_state_index >= len(states):
            continue

        current_state = states[current_state_index]
        current_color = colors[color_index]

        if all(current_color != color_assignment[neighbor] for neighbor in adj_list[current_state]):
            color_assignment[current_state] = current_color
            if current_state_index == len(states) - 1:
                return True, cost  # Found a valid coloring
            for successor in get_successors(current_state_index, color_index):
                stack.append((*successor, cost + 1))
        else:
            for successor in get_successors(current_state_index, color_index):
                stack.append((*successor, cost + 1))

    return False, cost

# Define the adjacency list (partial, continue adding all states and their neighbors)
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
    "Washington DC": ["Maryland", "Virginia"],
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
color_assignment = {state: None for state in states}

result, cost = dfs_coloring(states, adj_list, color_assignment)
if result:
    print(f"Solution found with cost {cost}")
    for state, color in color_assignment.items():
        print(f"{state}: Color {color}")
else:
    print("No solution found")