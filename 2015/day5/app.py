'''
--- Day 5: Doesn't He Have Intern-Elves For This? ---
Santa needs help figuring out which strings in his text file are naughty or nice.

A nice string is one with all of the following properties:

It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
For example:

ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of the disallowed substrings.
aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
jchzalrnumimnmhp is naughty because it has no double letter.
haegwjzuvuyypxyu is naughty because it contains the string xy.
dvszwmarrgswjxmb is naughty because it contains only one vowel.
How many strings are nice?

To begin, get your puzzle input.
'''

f = open('2015/day5/input.txt', 'r')
lines = f.readlines()
f.close()

nice_strings = 0
for line in lines:
    line = line.replace('\n', '')
    # line contains atleast three vowels
    if (line.count('a') + line.count('e') + line.count('i') + line.count('o') + line.count('u')) >= 3:
        # line contains a double letter
        if any(line[i] == line[i+1] for i in range(len(line)-1)):
            # line does not contain the strings ab, cd, pq, or xy
            if not ('ab' in line or 'cd' in line or 'pq' in line or 'xy' in line):
                nice_strings += 1
   
print(nice_strings)

'''
--- Part Two ---
Realizing the error of his ways, Santa has switched to a better model of determining whether a string is naughty or nice. None of the old rules apply, as they are all clearly ridiculous.

Now, a nice string is one with all of the following properties:

It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.
For example:

qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and a letter that repeats with exactly one letter between them (zxz).
xxyxx is nice because it has a pair that appears twice and a letter that repeats with one between, even though the letters used by each rule overlap.
uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with a single letter between them.
ieodomkazucvgmuy is naughty because it has a repeating letter with one between (odo), but no pair that appears twice.
How many strings are nice under these new rules?
'''
# Define functions for the new rules

def has_repeated_pair(s):
    """Check if the string contains a pair of any two letters that appears at least twice without overlapping."""
    for i in range(len(s) - 1):
        pair = s[i:i+2]
        if pair in s[i+2:]:
            return True
    return False

def has_repeat_with_one_between(s):
    """Check if the string contains at least one letter which repeats with exactly one letter between them."""
    for i in range(len(s) - 2):
        if s[i] == s[i+2]:
            return True
    return False

def is_nice_new_rules(s):
    """Check if the string is nice under the new rules."""
    return has_repeated_pair(s) and has_repeat_with_one_between(s)

nice_count = 0
# Remove the newline character
line = line.replace('\n', '')
nice_count = sum(is_nice_new_rules(s) for s in lines)

print(nice_count)