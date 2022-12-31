import string

def sb_solve(centerLetter: str, outerLetters: list, wordList: list) -> list:
    """! Solves the spelling bee
    @param centerLetter  A single character that is the center of the beehive
    @param outerLetters  A list of the other 6 letters in the beehive
    @param wordList      A list of words that could be valid solutions

    @return              A list of solutions
    """

    # Assumtiosn made:
    # 1) The 'centerLetter' is a single character 
    # 2) The 'outerLetters' + 'centerLetter' contains 7 unique letters
    # 4) The 'wordList' contains only words >=4 letters long
 
    # Create set of letters not allowed in word be removing the valid letters
    # from the alphabet
    validLetters = list(centerLetter) + outerLetters
    alphabet = string.ascii_uppercase
    badLetters = set(alphabet) - set(validLetters)

    # The solution list starts empty
    solutions = []

    # Walk through the whole word list looking for valid answers
    for word in wordList:

        # Find the unique letters in the current word
        lettersInWord = set(word)

        # First check if the center letter is in the word
        if(centerLetter in lettersInWord):

            # If it is then see if there are any invalid
            # letters in the word.
            if len(lettersInWord.intersection(badLetters)) == 0:
                
                # No invalid letters so add the word to the solution list
                solutions.append(word)
    
    return solutions

def read_word_list(word_list_file: str) -> list:
    # create the word list from the file
    with open(word_list_file) as file:
        wordsFromFile = file.readlines()

        # Strip the newline characters
        wordList = []
        for word in wordsFromFile:
            wordList.append(word.strip('\n'))

    return wordList

if __name__ == "__main__":
    # Ask the user for the letters
    # must be 7 letters and they must be unique
    numLetters = 0
    while(numLetters != 7):
        letters = input("Enter letters, center letter first: ")
        letters = letters.upper()
        centerLetter = letters[0]
        outerLetters = list(letters[1:7])
        numLetters = len(set(letters))
        if(numLetters != 7):
            print(f'{numLetters} unique letters entered, try again with 6 letters')

    wordList = read_word_list('sb_word_list.txt')

    solutions = sb_solve(centerLetter, outerLetters, wordList)

    print(solutions)