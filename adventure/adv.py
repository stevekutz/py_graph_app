from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

######
from util import Queue, Stack


# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "adventure/maps/test_line.txt"
map_file = "adventure/maps/test_cross.txt"
# map_file = "adventure/maps/test_loop.txt"
# map_file = "adventure/maps/test_loop_fork.txt"
# map_file = "adventure/maps/main_maze.txt"

# map_file = "projects/adventure/maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

#visited = set()


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

s = Stack()
s.push(player.current_room)

while len(visited_rooms) < len(world.rooms):
    current_r  = s.pop()

    print(f' current_r  {current_r} ')
    print(f' current_r.id  {current_r.id}')

    if current_r.id not in visited_rooms:


        break


for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)
    print(f' visited_rooms {visited_rooms} ')

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")

#     visited.add(player.current_room.id)  # starting room
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
       

#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
