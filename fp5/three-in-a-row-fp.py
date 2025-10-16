# Для создания иммутабельного элемента, приходится использовать namedtuple, чтобы значение можно было получить по имени

from collections import namedtuple

Element = namedtuple('Element', ['value'])

