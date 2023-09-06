# The classic programming language of Bitland is Bit++. This language is so peculiar and complicated.
#
# The language is that peculiar as it has exactly one variable,
# called x. Also, there are two operations:
#
# Operation ++ increases the value of variable x by 1.
# Operation -- decreases the value of variable x by 1.
# A statement in language Bit++ is a sequence, consisting of exactly one operation and one variable x.
# The statement is written without spaces, that is, it can only contain characters "+", "-", "X". Executing
# a statement means applying the operation it contains.
#
# A programme in Bit++ is a sequence of statements, each of them needs to be executed. Executing a programme
# means executing all the statements it contains.
#
# You're given a programme in language Bit++. The initial value of x is 0. Execute the programme and find
# its final value (the value of the variable when this programme is executed).


n = int(input())

total_score = 0

for statement in range(n):
    sequence = input()

    plus = 0
    minus = 0

    for ch in sequence:
        if ch == "+":
            plus += 1

            if plus >= 2:
                total_score += 1


        elif ch == "-":
            minus += 1

            if minus >= 2:
                total_score -= 1

print(total_score)

# Time Complexity O(n)

# MORE OPTIMISED SOLUTION

# program = ["++X", "X--", "++X", "--X"]
# x = 0
#
# for statement in program:
#     if "++" in statement:
#         x += 1
#     elif "--" in statement:
#         x -= 1
#
# print("Final value of x:", x)

