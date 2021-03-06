from typing import List


class YourAI:

    def __init__(self, word_lenght: int, guess_limit: int):
        """
        Initialize the AI class here, this is called when the test starts and persists between tests
        Inialization time does not count towards the score
        You can use this to load words from a file or anything else
    
        Tip: You can find all the words in the words-.csv file in Game/words directory (where  is the word length)
          See the example in BadAI.py for how to load words from a file
          Second parameter in file is the popularity of the word
          The more popular the word, the more likely it is to be the answer

        :param word_lenght: The length of the word to be guessed
        :param guess_limit: The maximum number of guesses the player has
        """
        pass

    def clean(self):
        """
        Called before each test
        :return: None
        """
        pass

    def next(self, past_guesses: List[str], past_results: List[int], left: int):
        """
        Called when the AI needs to make a guess
        :param past_guesses: A list of all the guesses made so far
        :param past_results: A list of the results of the guesses made so far
           Each result is a list of length `word_length` and the meaning of each element is:
             1 for correct letter and place,
             0 for letter that appears in the word but in different place,
            -1 for letter that does not appear in the word
            -2 for invalid input (word does not exist, wrong length, etc)
        :param left: The number of guesses left
        :return:
        """
        pass
