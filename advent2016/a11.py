from __future__ import print_function
import itertools
import collections
from pprint import pprint

input_raw = """The first floor contains a strontium generator, a strontium-compatible microchip, a plutonium generator, and a plutonium-compatible microchip.
The second floor contains a thulium generator, a ruthenium generator, a ruthenium-compatible microchip, a curium generator, and a curium-compatible microchip.
The third floor contains a thulium-compatible microchip.
The fourth floor contains nothing relevant."""

#initial_state = (
#        frozenset(['SG', 'S', 'PG', 'P']),
#        frozenset(['TG', 'RG', 'R', 'CG', 'C']),
#        frozenset(['T']),
#        frozenset(),
#        0)

initial_state = (
        frozenset(['SG', 'S', 'PG', 'P', 'eG', 'e', 'D', 'DG']),
        frozenset(['TG', 'RG', 'R', 'CG', 'C']),
        frozenset(['T']),
        frozenset(),
        0
        )
#initial_state = (
#        frozenset(['E', 'H', 'L']),
#        frozenset(['HG']),
#        frozenset(['LG']),
#        frozenset(),
#        )

gen_for = {'S': 'SG', 'P': 'PG', 'T': 'TG', 'R': 'RG', 'C': 'CG',
        'e': 'eG', 'D': 'DG'}

def is_valid_row(floor):
    gens = set()
    chips = set()
    for thing in floor:
        if len(thing) == 1:
            chips.add(thing)
        else:
            gens.add(thing[0])
    if not gens:
        return True
    paired = gens & chips
    gens_wo_chips = gens - paired
    chips_wo_gens = chips - paired
    return len(chips_wo_gens) == 0

assert(not is_valid_row(frozenset(['P', 'PG', 'S'])))
assert(is_valid_row(frozenset(['P', 'PG', 'SG'])))
assert(not is_valid_row(frozenset(['P', 'PG', 'S', 'SG', 'R'])))
assert(not is_valid_row(frozenset(['P', 'RG', 'SG']))) # not
assert(not is_valid_row(frozenset(['P', 'SG']))) # not
assert(is_valid_row(frozenset(['SG', 'PG'])))

floor_list = [[1], [0, 2], [1, 3], [2]]
def next_valid_states(state):
    current_floor = state[4]
    things = state[current_floor]
    floors_to_try = floor_list[current_floor]
    for i in floors_to_try:
        for thing in things:
            # move with one thing to another floor:
            change_set = frozenset([thing])
            old_floor = state[current_floor] - change_set
            if not is_valid_row(old_floor):
                continue
            new_floor = state[i] | change_set
            if not is_valid_row(new_floor):
                continue
            new_state = list(state)
            new_state[current_floor] = old_floor
            new_state[i] = new_floor
            new_state[4] = i
            yield tuple(new_state)
        for thing1, thing2 in itertools.combinations(things, 2):
            # move with two things to another floor:
            #if 'G' in thing1 and thing2 == thing1[0]:
            #    continue
            #if 'G' in thing2 and thing1 == thing2[0]:
            #    continue
            change_set = frozenset([thing1, thing2])
            old_floor = state[current_floor] - change_set
            if not is_valid_row(old_floor):
                continue
            new_floor = state[i] | change_set
            if not is_valid_row(new_floor):
                continue
            new_state = list(state)
            new_state[current_floor] = old_floor
            new_state[i] = new_floor
            new_state[4] = i
            yield tuple(new_state)

full_length = sum(len(x) for x in initial_state[:-1])
def is_final_state(state):
    return len(state[3]) == full_length

def search_state():
    frontier = [initial_state]
    seen = {initial_state}
    i = 0
    while True:
        i += 1
        next_frontier = []
        for state in frontier:
            for next_state in next_valid_states(state):
                h = hash(next_state)
                if h in seen:
                    continue
                if is_final_state(next_state):
                    print(i)
                    return
                seen.add(h)
                next_frontier.append(next_state)
        print(i, len(frontier))
        frontier = next_frontier

if __name__ == '__main__':
    search_state()
