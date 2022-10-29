# KAEL MURPHY
# COMP-SCI1026 ASSIGNMENT2
# SOUNDEX CALCULATOR

# the prompt at the start of the program
print('Enter names, one on each line. Type DONE to quit entering names.')


def userInput():
    """this is the function where we gather user input"""
    keepGoing = ''
    # where we will store the names
    namesList = []
    # stops the loop when the user types in DONE
    while keepGoing != 'no':
        userInp = input()
        if userInp == 'DONE':
            keepGoing = "no"
        else:
            # adds the names to the list
            namesList.append(userInp)
    # sorts the list so it outputs in the correct order
    namesList.sort()
    # returns the list to be used in a later function
    return namesList


def lowerFunction(x):
    """an extra function I added to turn all the input to lowercase for letter replacement"""
    namesListLower = []
    namesList = x
    for i in range(len(namesList)):
        namesListLower.append(namesList[i].lower())
    return namesListLower


def letterReplacementFunction(x):
    """this is the function that will replace all the letters of names list with numbers"""
    # I used a dictionary for letter replacement instead of a bunch of strings
    letterReplacement = {'0': ['a', 'e', 'i', 'o', 'u', 'y', 'h', 'w'],
                         '1': ['b', 'f', 'p', 'v'],
                         '2': ['c', 'g', 'j', 'k', 'q', 's', 'x', 'z'],
                         '3': ['d', 't'],
                         '4': ['l'],
                         '5': ['m', 'n'],
                         '6': ['r']}
    newList = x
    numberList = []
    # for loop that creates a string and adds digits to a new string that correspond to the original name string
    for i in range(len(newList)):
        # string will be reset after it is appended to a list at the end of the for loop
        D = ''
        for j in range(len(newList[i])):
            M = newList[i][j]
            if M in letterReplacement['0']:
                D = D + '0'
            elif M in letterReplacement['1']:
                D = D + '1'
            elif M in letterReplacement['2']:
                D = D + '2'
            elif M in letterReplacement['3']:
                D = D + '3'
            elif M in letterReplacement['4']:
                D = D + '4'
            elif M in letterReplacement['5']:
                D = D + '5'
            elif M in letterReplacement['6']:
                D = D + '6'
        # adds the new string will all the letters to a new section of the list
        numberList.append(D)
    return numberList


def sameLetter(x):
    """this is the function that will determine whether two adjacent numbers are the same, it will replace one of the
    numbers with 0 """
    numberList = x
    newNumberList = []
    # for loop that will run through all the numbers for every string in the list
    for i in range(len(numberList)):
        newNumber = numberList[i]
        if len(numberList[i]) > 1:
            for k in range(0, len(numberList[i]) - 1):
                # this if statement compares whether the two numbers are the same, and replaces one of them with 0
                if numberList[i][k] == numberList[i][k + 1]:
                    newNumber = newNumber[:k] + '0' + newNumber[k + 1:]
        newNumberList.append(newNumber)
    return newNumberList


def zeroStripper(x):
    """this is the function that will get rid of all the 0's in all the stings in the number list"""
    newNumberList = x
    middleNumberList = []
    # this for loop will replace all the 0's with ''
    for j in range(len(newNumberList)):
        D = newNumberList[j]
        D = D.replace('0', '')
        middleNumberList.append(D)
        # this adds a bunch of 0's onto the end of each string to ensure that they all have enough digits
        middleNumberList[j] = middleNumberList[j] + '00000'
    return middleNumberList


def firstNumberReplacement(x, y, z):
    """this function is responsible for replacing the first digit of every string with the lowercase letter that
    comes at the start of the original names list """
    originalnumberlist = z
    namesListLower = x
    numberList = y
    soundexList = []
    # this loop gets rid of the second digit if it has the same encoding as the lowercase at the start of the string
    for j in range(len(numberList)):
        if originalnumberlist[j][0] == numberList[j][0]:
            numberList[j] = numberList[j][1:]
    # this loop combines the first letter of the string with the rest of the digits in the number string
    for i in range(len(numberList)):
        numberList[i] = namesListLower[i][0] + numberList[i]
        # this makes sure that all the strings that are going to the soundex list have the proper length
        soundexList.append(numberList[i][:4])
    return soundexList


def comparisonFunction(x, y):
    """this is the function where I will compare two given soundex encodings, if they are the same I will add both of
    the names to a list and return the list """
    namesList = y
    soundexList = x
    finalList = []
    for i in range(len(soundexList)):
        # changed the range around the bit, so it will only compare each two names once
        for j in range(i, len(soundexList)):
            # this ensures that I don't compare names to themselves
            if j != i:
                # if the two words being compared are the same I send them to my final list
                if soundexList[i] == soundexList[j]:
                    finalList.append('{} and {} have the same Soundex encoding.'.format(namesList[i], namesList[j]))
    return finalList


def soundexFunction(x):
    """this soundex function will call and run all the soundex components, it will print my final list,
    one string on each line """
    y = lowerFunction(x)
    z = letterReplacementFunction(y)
    w = sameLetter(z)
    v = zeroStripper(w)
    q = firstNumberReplacement(y, v, z)
    r = comparisonFunction(q, x)
    # this prints each string on a different line instead of printing the whole list consecutively
    for i in range(len(r)):
        print(r[i])


def main():
    """this is the main function that will call the user output function, assign it a value x, then call the soundex
    function using x (user input) as its parameter """
    x = userInput()
    soundexFunction(x)


main()
