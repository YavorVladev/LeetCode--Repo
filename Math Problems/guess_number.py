class Solution:
    def guessNumber(self, n: int) -> int:
        lowerBound, upperBound = 1, n
        # Binary division faster than (lowerBound + upperBound) //2
        myGuess = (lowerBound + upperBound) >> 1
        # walrus operator ':=' - assigns value of the function to the variable 'res'
        # and then compare res with 0
        while (res := guess(myGuess)) != 0:
            if res == 1:
                lowerBound = myGuess + 1
            else:
                upperBound = myGuess - 1
            myGuess = (lowerBound + upperBound) >> 1

        return myGuess

#       Time Complexity O(log n)





