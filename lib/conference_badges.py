def badge_maker(name):
    return (f'Hello, my name is {name}.')

def batch_badge_creator(names):
    name_lists = []
    for n in names:
        name_lists.append(f'Hello, my name is {n}.')
    return name_lists
    

def assign_rooms(names):
    room_assignments = []
    for index, item in enumerate(names):
        room_number = index + 1
        room_assignments.append(f"Hello, {item}! You'll be assigned to room {room_number}!")
    return room_assignments

def printer(names):
    for badge in batch_badge_creator(names):
        print(badge)
    for room in assign_rooms(names):
        print(room)
