# Spelling Bee Solver
This is an entirely unecessary program since you can easily view the page source on the NYT spelling bee web page to find today's answers. I made it as a programming exercise and as an opportunity to explore GitHub actions to automatically update my word list daily.

This programs solves the NYT Spelling Bee game and updates the valid word list. Each day at 9am the update_word_list.py will run automatically. This will solve the day's puzzle and compare the answers to the NYT answers. The valid word list will be updated by removing any answers that NYT did not deem valid.
