'''
--- Day 6: Probably a Fire Hazard ---
Because your neighbors keep defeating you in the holiday house decorating contest year after year, you've decided to deploy one million lights in a 1000x1000 grid.

Furthermore, because you've been especially nice this year, Santa has mailed you instructions on how to display the ideal lighting configuration.

Lights in your grid are numbered from 0 to 999 in each direction; the lights at each corner are at 0,0, 0,999, 999,999, and 999,0. The instructions include whether to turn on, turn off, or toggle various inclusive ranges given as coordinate pairs. Each coordinate pair represents opposite corners of a rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square. The lights all start turned off.

To defeat your neighbors this year, all you have to do is set up your lights by doing the instructions Santa sent you in order.

For example:

> turn on 0,0 through 999,999 would turn on (or leave on) every light.
> toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning off the ones that were on, and turning on the ones that were off.
> turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.

After following the instructions, how many lights are lit?
'''



# Load the input instructions
with open('2015/day6/input.txt') as f:
    lines = f.readlines()

# Part 1: Count the number of lit lights
lights_part1 = [[0] * 1000 for _ in range(1000)]

for line in lines:
    parts = line.strip().split(' ')
    if parts[0] == 'toggle':
        x1, y1 = map(int, parts[1].split(','))
        x2, y2 = map(int, parts[3].split(','))
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                lights_part1[i][j] = 1 - lights_part1[i][j]
    elif parts[0] == 'turn':
        x1, y1 = map(int, parts[2].split(','))
        x2, y2 = map(int, parts[4].split(','))
        value = 1 if parts[1] == 'on' else 0
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                lights_part1[i][j] = value

lit_count = sum(sum(row) for row in lights_part1)
print("Part 1: Number of lit lights =", lit_count)


'''
--- Part Two ---
You just finish implementing your winning light pattern when you realize you mistranslated Santa's message from Ancient Nordic Elvish.

The light grid you bought actually has individual brightness controls; each light can have a brightness of zero or more. The lights all start at zero.

The phrase turn on actually means that you should increase the brightness of those lights by 1.

The phrase turn off actually means that you should decrease the brightness of those lights by 1, to a minimum of zero.

The phrase toggle actually means that you should increase the brightness of those lights by 2.

What is the total brightness of all lights combined after following Santa's instructions?

For example:

turn on 0,0 through 0,0 would increase the total brightness by 1.
toggle 0,0 through 999,999 would increase the total brightness by 2000000.
'''

# Part 2: Calculate the total brightness
lights_part2 = [[0] * 1000 for _ in range(1000)]

for line in lines:
    parts = line.strip().split(' ')
    if parts[0] == 'toggle':
        x1, y1 = map(int, parts[1].split(','))
        x2, y2 = map(int, parts[3].split(','))
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                lights_part2[i][j] += 2
    elif parts[0] == 'turn':
        x1, y1 = map(int, parts[2].split(','))
        x2, y2 = map(int, parts[4].split(','))
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if parts[1] == 'on':
                    lights_part2[i][j] += 1
                elif parts[1] == 'off':
                    lights_part2[i][j] = max(0, lights_part2[i][j] - 1)

total_brightness = sum(sum(row) for row in lights_part2)
print("Part 2: Total brightness =", total_brightness)

f.close()