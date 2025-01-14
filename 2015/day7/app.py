"""
--- Day 7: Some Assembly Required ---
This year, Santa brought little Bobby Tables a set of wires and bitwise logic gates! Unfortunately, little Bobby is a little under the recommended age range, and he needs help assembling the circuit.

Each wire has an identifier (some lowercase letters) and can carry a 16-bit signal (a number from 0 to 65535). A signal is provided to each wire by a gate, another wire, or some specific value. Each wire can only get a signal from one source, but can provide its signal to multiple destinations. A gate provides no signal until all of its inputs have a signal.

The included instructions booklet describes how to connect the parts together: x AND y -> z means to connect wires x and y to an AND gate, and then connect its output to wire z.

For example:

123 -> x means that the signal 123 is provided to wire x.
x AND y -> z means that the bitwise AND of wire x and wire y is provided to wire z.
p LSHIFT 2 -> q means that the value from wire p is left-shifted by 2 and then provided to wire q.
NOT e -> f means that the bitwise complement of the value from wire e is provided to wire f.
Other possible gates include OR (bitwise OR) and RSHIFT (right-shift). If, for some reason, you'd like to emulate the circuit instead, almost all programming languages (for example, C, JavaScript, or Python) provide operators for these gates.

For example, here is a simple circuit:

123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i
After it is run, these are the signals on the wires:

d: 72
e: 507
f: 492
g: 114
h: 65412
i: 65079
x: 123
y: 456
In little Bobby's kit's instructions booklet (provided as your puzzle input), what signal is ultimately provided to wire a?

"""
# Read the input instructions
with open("2015/day7/input.txt") as f:
    instructions = f.read().splitlines()

# Define a dictionary to store the values of each wire
wires = {}

# Function to evaluate a wire's value
def get_value(wire):
    if wire.isdigit():
        # If wire is a digit, it's a constant value
        return int(wire)
    if wire not in wires:
        raise ValueError(f"Wire {wire} has no value or definition.")
    # Evaluate the value lazily
    if isinstance(wires[wire], str):
        wires[wire] = evaluate(wires[wire])
    return wires[wire]

# Function to evaluate an instruction
def evaluate(expression):
    parts = expression.split()
    if "AND" in parts:
        return get_value(parts[0]) & get_value(parts[2])
    elif "OR" in parts:
        return get_value(parts[0]) | get_value(parts[2])
    elif "LSHIFT" in parts:
        return get_value(parts[0]) << int(parts[2])
    elif "RSHIFT" in parts:
        return get_value(parts[0]) >> int(parts[2])
    elif "NOT" in parts:
        return ~get_value(parts[1]) & 0xFFFF  # Ensure 16-bit value
    else:
        return get_value(parts[0])  # Direct assignment

# Parse the input and store instructions in the wires dictionary
original_wires = {}
for instruction in instructions:
    expr, wire = instruction.split(" -> ")
    original_wires[wire] = expr

# Function to reset the circuit and override a specific wire
def reset_wires(override=None):
    global wires
    wires = original_wires.copy()
    if override:
        wires.update(override)

# Part 1: Get the initial signal for wire 'a'
reset_wires()
signal_a = get_value("a")
print("Signal to wire 'a' (Part 1):", signal_a)

"""
--- Part Two ---
Now, take the signal you got on wire a, override wire b to that signal, and reset the other wires (including wire a). What new signal is ultimately provided to wire a?
"""

# Part 2: Override wire 'b' with the signal from Part 1 and re-evaluate
reset_wires(override={"b": str(signal_a)})
new_signal_a = get_value("a")
print("Signal to wire 'a' (Part 2):", new_signal_a)

f.close()
