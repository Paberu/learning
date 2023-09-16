from pymonad.tools import curry
from pymonad.state import State

car_init = {'roots': [], 'gas': 40}

roots = {'Pskov-PushGory': 15,
         'Pskov-Ostrov': 5,
         'Ostrov-Pushgory': 10,
         }

car_state = State.insert(car_init['roots'])


@curry(2)
def drive(root_key, car_roots):
    def count_computation(gas_remained):
        return car_roots + [root_key], gas_remained - roots[root_key]

    return State(count_computation)


@curry(1)
def fill_the_tank(car_roots):
    def count_computation(gas_remained):
        return car_roots + ['Gas Station'], 40

    return State(count_computation)


finale = car_state.then(drive('Pskov-PushGory')).then(drive('Ostrov-Pushgory')).then(fill_the_tank()).then(drive('Pskov-Ostrov'))

print(finale.run(car_init['gas']))
