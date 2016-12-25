import itertools
import assembunny

with open('day25_input') as f:
    input = f.read()

for a in itertools.count():
    counter = 0
    clock_signal = True

    def out(signal):
        global counter, clock_signal
        clock_signal = signal == counter % 2
        counter += 1
        return counter > 16 or not clock_signal

    assembunny.run(input, out, a=a)

    if clock_signal:
        print(a)
        break
