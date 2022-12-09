import sys

input_filename = sys.argv[1]

with open(input_filename) as f:
    input = f.read()

my_figure_table = {
    'A X': 'C',
    'B X': 'A',
    'C X': 'B',
    'A Y': 'A',
    'B Y': 'B',
    'C Y': 'C',
    'A Z': 'B',
    'B Z': 'C',
    'C Z': 'A',
}
figure_score = {'A': 1, 'B': 2, 'C': 3}

total_score = 0
for round in input.strip().split('\n'):
    round = round.strip()
    outcome = round[-1]
    my_figure = my_figure_table[round]
    total_score += 6 * (outcome == 'Z')
    total_score += 3 * (outcome == 'Y')
    total_score += figure_score[my_figure]

print(total_score)
