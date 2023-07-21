# Let's consider a word too long, if
# its length is strictly more than 10 characters.
# All too long words should be replaced with a special abbreviation.
#
# This abbreviation is made like this: we write down
# the first and the last letter of a word and between
# them we write the number of letters between the first
# and the last letters. That number is in decimal system
# and doesn't contain any leading zeroes.
#
# Thus, "localization" will be spelt as "l10n", and "internationalization»
# will be spelt as "i18n".


n = int(input())

for _ in range(n):
    word = input()

    if len(word) > 10:
        b_number = len(word[1:-1])
        print(f"{word[0]}{b_number}{word[-1]}")
    else:
        print(word)

        # Time Complexity O(n)


        
