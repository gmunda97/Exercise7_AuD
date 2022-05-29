import nltk
import random
# nltk.download()
from nltk.corpus import wordnet
from nltk.corpus import names

# Questions 1 and 2

def generate_names(char, num):
    female_namelist = []
    basic_female_namelist = []
    male_namelist = []
    basic_male_namelist = []
    male_names = names.words('male.txt')
    female_names = names.words('female.txt')

    tagged_male_names = [(str(name), 'male') for name in male_names]
    non_tagged_male_names = [name for name in male_names]
    tagged_female_names = [(str(name), 'female') for name in female_names]
    non_tagged_female_names = [name for name in female_names]

    male_text = 'male_text.txt'
    female_text = 'female_text.txt'

    if type(char) == str:
        name_check = 0
        for name in range(len(female_names)):
            if female_names[name].startswith(char):
                name_check += 1

    if type(char) != str:
        raise ValueError("Cannot display names that are not strings")
    elif name_check == 0:
        print('No female names found')
    else:
        for i in range(num):
            j = 0
            while j == 0:
                x = random.randint(0, len(female_names) - 1)
                if female_names[x].startswith(char):
                    female_namelist.append(tagged_female_names[x])
                    basic_female_namelist.append(non_tagged_female_names[x])
                    j += 1

        print(female_namelist)

        with open(female_text, 'w') as writer:
            for name in basic_female_namelist:
                writer.write(name)
                writer.write("\n")

    if type(char) == str:
        name_check = 0
        for name in range(len(male_names)):
            if male_names[name].startswith(char):
                name_check += 1

    if type(char) != str:
        raise ValueError("Cannot display names that are not strings")
    elif name_check == 0:
        print("No male names found")
    else:
        for i in range(num):
            j = 0
            while j == 0:
                x = random.randint(0, len(male_names))
                if male_names[x].startswith(char):
                    male_namelist.append(tagged_male_names[x])
                    basic_male_namelist.append(non_tagged_male_names[x])
                    j += 1

        print(male_namelist)

        with open(male_text, 'w') as writer:
            for name in basic_male_namelist:
                writer.write(name)
                writer.write("\n")


generate_names('R', 3)


# Question 3

class SynAnt:
    def __init__(self):
        self.words = []  # the constructor accepts a list of words used to find synonyms and antonyms

    def append_words(self, word):  # function to append words into the list
        self.words.append(word)

    def find_synonyms(self):
        if len(self.words) == 0:  # if the list is empty ...
            raise Exception("Cannot find synonyms from empty lists")  # raise an error to avoid reading empty lists
        for word in self.words:
            if type(word) != str:  # if a non string type is inserted, raise a value error
                raise ValueError("Cannot find synonyms for non string types")
            else:  # otherwise, find the synonyms for the inserted word
                synonyms = []  # create an empty list into which synonyms can be appended
                for syn in wordnet.synsets(word):
                    for l in syn.lemmas():
                        synonyms.append(l.name())

            if len(synonyms) == 0:  # if no synonyms are found, appends a custom message into the list
                synonyms.append("No synonyms found")

            print("Synonym of '{}': {}".format(word, set(synonyms)))  # printing the result in a set

    def find_antonyms(self):
        if len(self.words) == 0:
            raise Exception("Cannot find antonyms from empty lists")
        for word in self.words:
            if type(word) != str:
                raise ValueError("Cannot find antonyms for non string types")
            else:
                antonyms = []
                for syn in wordnet.synsets(word):  # find synonyms to get antonyms
                    for i in syn.lemmas():
                        if i.antonyms():
                            antonyms.append(i.antonyms()[0].name())

            if len(antonyms) == 0:
                antonyms.append("No antonyms found")

            print("Antonyms of '{}' : {}".format(word, set(antonyms)))


S1 = SynAnt()
S1.append_words('dark')
S1.append_words('big')
S1.append_words('joy')
S1.find_synonyms()

A1 = SynAnt()
A1.append_words('sweet')
A1.append_words('beautiful')
A1.append_words('computer')
A1.find_antonyms()
