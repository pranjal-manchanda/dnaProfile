import sys
import csv
from collections import OrderedDict


def main():
    # Produce error message if incorrect number of inputs passed in
    if len(sys.argv) != 3:
        print("Error. Incorrect Input")
        sys.exit(1)

    # Read the database and the individual sample files as lists
    dbReader = list(csv.reader(open(sys.argv[1])))
    sampleReader = list(csv.reader(open(sys.argv[2])))

    # Create list to keep track of number of sequence occurences
    strCount = []

    # Iterate through the database fieldNames
    for sequence in dbReader[0][1:]:
        # Append output from frequencyCount function to strCount dictionary
        strCount.append(str(frequencyCount(str(sampleReader[0]), sequence)))

    # If sequence count matches database, then print name of individual
    for row in dbReader[1:]:
        if row[1:] == strCount:
            print(row[0])
            sys.exit(0)

    # Else, no match
    print("No match")


def frequencyCount(mainStr, subStr):
    """
    # Input: Takes an individuals' dna sample and an str pattern
    # Output: Number of times the sample appears consecutively in the mainStr
    """

    # Initialize count variables and find the first occurance of subStr at index pos
    count = maxCount = 0
    pos = mainStr.find(subStr)

    # If subStr not found, return 0
    if pos == -1:
        return count

    count += 1

    # Find maximum number of consecutive occurances
    while(True):
        # If count > maxCount, then maxCount = count
        if count > maxCount:
            maxCount = count

        # Continue iterating to the next string
        newPos = mainStr.find(subStr, pos + 1)

        # If no match found, return current maxCount value
        if newPos == -1:
            return maxCount

        # If newPos is consecutively next from pos, add to count
        elif newPos == pos + len(subStr):
            count += 1
            # print(count)

        # Otherwise, set count back to 1
        else:
            count = 1

        # Update pos to newPos
        pos = newPos
        # i = newPos

    return maxCount  # This is probably redundant


main()
