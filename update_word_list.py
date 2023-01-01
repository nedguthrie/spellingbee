#! python3

import urllib3
from bs4 import BeautifulSoup
import ast
from spelling_bee_solve import sb_solve
from spelling_bee_solve import read_word_list

if __name__ == "__main__":
    """! Solves todays spelling bee and then compares answers
        to the answers scraped from the NYT webpage. Remove invalid
        words from the word list and add new ones
    """

    http = urllib3.PoolManager()

    url = 'https://www.nytimes.com/puzzles/spelling-bee'
    response = http.request('GET', url)
    soup = BeautifulSoup(response.data, features="html.parser")

    scripts = soup.find_all('script')

    for script in scripts:
        # Find the script that contains the game data
        if('window.gameData' in script.text):

            # Split off the dictionary
            dictionary = script.text.split(' = ', 1)[-1]
            data = ast.literal_eval(dictionary)
            centerLetter = data.get("today").get("centerLetter")
            outerLetters = data.get("today").get("outerLetters")
            NYTAnswers = data.get("today").get("answers")

            # Make everything upper case to match our solve script
            centerLetter = centerLetter.upper()
            outerLetters = [x.upper() for x in outerLetters]
            NYTAnswers = [x.upper() for x in NYTAnswers]

    print(f'center = {centerLetter}')
    print(f'outer letters = {outerLetters}')
    print(f'NYT answers = {NYTAnswers}')

    # Open yesterday's word list 
    wordList = read_word_list(f'word_lists/sb_word_list.txt')

    # Solve the puzzle using yesterday's word list
    myAnswers = sb_solve(centerLetter, outerLetters, wordList)

    print(f'My answers = {myAnswers}')

    # Check each of my answers to see if it is in the NYT list
    # If not, remove from the word list
    # and add it to the invalid list
    invalidWordList = read_word_list(f'word_lists/invalid_sb_word_list.txt')
    for word in myAnswers:
        if(word not in NYTAnswers):
            print(f'Removing "{word}" from word list')
            wordList.remove(word)
            invalidWordList.append(word)

    # Check if there are words in the NYT list not in my list
    # If so, add it
    for word in NYTAnswers:
        if(word not in myAnswers):
            print(f'Adding "{word}" to word list')
            wordList.append(word)

    # Sort the new word list and store
    wordList.sort()
    invalidWordList.sort()

    with open(f'word_lists/sb_word_list.txt', 'w') as file:
        for word in wordList:
            file.write(f'{word}\n')

    with open(f'word_lists/invalid_sb_word_list.txt', 'w') as file:
        for word in invalidWordList:
            file.write(f'{word}\n')
