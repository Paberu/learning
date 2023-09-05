from pymonad.tools import curry
from pymonad.state import State


user_init = {'items': [], 'money': 2000}

items = {'apples': 70,
         'wine': 300,
         'milk': 80,
         'chips': 100
         }

user_state = State(user_init['items'], user_init['money'])


@curry(2)
def buy(user_items, item):
    @State
    def count_computation(old_count):
        if old_count < items[item] or item not in items:
            return user_items, old_count
        return user_items.append(item), old_count - items[item]
    return count_computation


finale = user_state.then(buy('wine')).then(buy('apples')).then(buy('chips')).then(buy('chips')).then(buy('milk'))
