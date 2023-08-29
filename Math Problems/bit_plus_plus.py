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
