import pandas as pd

data = pd.read_csv('nato_phonetic_alphabet.csv')

phonetic_dict = {row.letter: row.code for (item, row)in data.iterrows()}

word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]


print(output_list)