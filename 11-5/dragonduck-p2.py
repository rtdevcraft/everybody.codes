
def move_in_circle(current_index, steps, direction, list_length):
    if direction == 'R':
        new_index = (current_index + steps) % list_length
    elif direction == 'L':
        new_index = (current_index - steps) % list_length
    else:
        raise ValueError("Direction must be 'clockwise' or 'counterclockwise'")
    return new_index

def parse_instructions(instruction_string):
    direction = instruction_string[0]
    steps = int(instruction_string[1:])
    return direction, steps



names = "Vyrdax, Drakzyph, Fyrryn, Elarzris"
instructions = "R3,L2,R3,L1"

name_list = names.split(", ")
instruction_list = instructions.split(",")

current_position = 0

for instruction in instruction_list:
   direction, steps = parse_instructions(instruction)
   current_position = move_in_circle(current_position, steps, direction, len(name_list))

print(move_in_circle(3, 4, 'R', 4))
print(parse_instructions("R3"))