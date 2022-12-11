from dataclasses import dataclass
from typing import Callable

input = open('input').read()


@dataclass
class Monkey:
    items: list
    inspect_item: Callable
    throw_to_monkey: Callable
    inspected_items: int = 0

def parse_monkey(monkey_description):
    _monkey, starting_items, operation, test, if_true, if_false = monkey_description.strip().split('\n')
    items = starting_items.split(': ')[1].split(', ')
    items = list(map(int, items))
    _op, _new, _eq, arg1, op, arg2 = operation.strip().split()
    _test, _divisible, _by, divisor = test.strip().split()
    divisor = int(divisor)
    if_true = int(if_true.split()[-1])
    if_false = int(if_false.split()[-1])

    def inspect_item(old):
        if arg2 == 'old':
            arg2_value = old
        else:
            arg2_value = int(arg2)
        if op == '+':
            return old + arg2_value
        if op == '*':
            return old * arg2_value

    def _test_func(val) -> bool:
        return val % divisor == 0

    def throw_to_monkey(worry_level) -> int:
        return if_true if _test_func(worry_level) else if_false

    return Monkey(items, inspect_item, throw_to_monkey)

monkeys = []
for monkey_description in input.split('\n\n'):
    monkeys.append(parse_monkey(monkey_description))

for round in range(20):
    for monkey in monkeys:
        for item in monkey.items:
            worry_level = monkey.inspect_item(item) // 3
            next_monkey = monkey.throw_to_monkey(worry_level)
            monkeys[next_monkey].items.append(worry_level)
        monkey.inspected_items += len(monkey.items)
        monkey.items = []

monkeys = sorted(monkeys, key=lambda m: -m.inspected_items)
print(monkeys[0].inspected_items * monkeys[1].inspected_items)
