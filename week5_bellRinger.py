# Problem Set 1: Indexing and Slicing Strings
# Basic Indexing:
# Given the string magic = 'abracadabra',
magic = 'abracadabra'
# a. Retrieve the 5th character.
fifth_char = print(magic [4])
# b. Retrieve the second to last character.
stic = print(magic [-2])
# c. Find the first occurrence of the letter 'c'.
first_c_index = print(magic.index('r'))
#fins last occurance of a letter
last_a_index = print(magic.rindex('a'))



# Advanced Slicing:
# Given the string alphabet = 'abcdefghijklmnopqrstuvwxyz',
alphabet = 'abcdefghijklmnopqrstuvwxyz'
# a. Extract the letters 'hij'.
#hij = print(alphabet [7:10])
hij = print(alphabet.index('hij'))
hij2 = print(alphabet [7:10])

# b. Extract every second letter starting from 'a' to 'm'.
m_index = print(alphabet. index ('m'))
every_second = print(alphabet [0:13:2])

# c. Reverse the entire string using slicing.
reversed_alphabet = print(alphabet [ : : -1])
i_have_a_dream = "With this faith, we will be able to hew out of the mountain of despair a stone of hope. With this faith, we will be able to transform the jangling discords of our nation into a beautiful symphony of brotherhood. With this faith, we will be able to work together, to pray together, to struggle together, to go to jail together, to stand up for freedom together, knowing that we will be free one day."

reversed_i_have_a_dream = print(i_have_a_dream [: : -1])

# Problem Set 2: Extracting Information
# From Descriptions:
# Extract the name of the famous personality from the quote "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
famous_quote = "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
john_f_k = print(famous_quote. find("John F. Kennedy"))

extract_name = print(famous_quote[83: ])

# Manipulating Words:
# Given the string info = "Python is fun. Fun is good. Good is subjective.",
# a. Extract the word 'subjective' without knowing its exact position.
python = "Python is fun. Fun is good. Good is subjective."
subject = print(python.find ('subjective') )
extract_word = print(python[36: ])
# b. Extract every third word.
third_letter = print(python[: :3])

# c. Reverse the positions of the words, but keep the characters in each word in the same order.
words = python.split()
print(words)
reversed_words = ' '.join(reversed(words))
print(reversed_words)
# Problem Set 3: String Methods
# Upper & Lower:
# Convert the following text to lowercase: MAY THE FORCE BE WITH YOU

text = "MAY THE FORCE BE WITH YOU."
print(text.lower())


# String Joining and Splitting:
# Given the list motto = ["Make", "haste", "slowly."],
# a. Convert the list into a single string.
motto = ["Make", "haste", "slowly."]
mottos = (' '.join((motto)))
# b. Now, split the string at every occurrence of the letter 'a'.
splitm = print(mottos.split('a'))


# Replacing Words:
# Modify the sentence: "Life is what happens when you are busy making other plans."
# a. Replace "busy" with "distracted".
sentence = "Life is what happens when you are busy making other plans."
replace1 = sentence.replace("busy", "distracted").replace("plans", "mistakes")
print(replace1)
# b. Replace "plans" with "mistakes".



# Problem Set 4: String Properties and Advanced Operations
# Repetition:
# Concatenate the word "Iteration" 7 times.
repeated_words = print("ilertation " * 7)

# Word Search:
# Check if the word "moonlight" appears in the quote: "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
wor="moonlight"
sen ="With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
wod_in_sen = print(wor in sen)


# Length and Count:
# a. Calculate the number of characters (including spaces and punctuation) in the word/phrase: "Supercalifragilisticexpialidocious".
# b. Count the number of times the letter 'i' appears in the same word/phrase.