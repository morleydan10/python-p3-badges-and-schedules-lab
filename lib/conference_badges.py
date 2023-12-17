def badge_maker(name):
    return (f"Hello, my name is {name}.")

def batch_badge_creator(names):
    badges = []
    for name in names:
        badge = badge_maker(name)
        badges.append(badge)
    return badges

def assign_rooms(names):
    room_assignments = []
    for i, name in enumerate(names, start = 1):
        message = (f"Hello, {name}! You'll be assigned to room {i}!")
        room_assignments.append(message)
    return room_assignments

def printer(names):
    badges = batch_badge_creator(names)
    for badge in badges:
        print(badge)
    
    rooms = assign_rooms(names)
    for room in rooms:
        print(room)