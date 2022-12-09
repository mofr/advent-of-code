import sys

input_filename = sys.argv[1]

with open(input_filename) as f:
    input = f.read()

winning_combs = {'A Y', 'B Z', 'C X'}
draw_combs = {'A X', 'B Y', 'C Z'}
figure_score = {'X': 1, 'Y': 2, 'Z': 3}

total_score = 0
for round in input.strip().split('\n'):
    round = round.strip()
    total_score += 6 * (round in winning_combs)
    total_score += 3 * (round in draw_combs)
    total_score += figure_score[round[-1]]

print(total_score)
