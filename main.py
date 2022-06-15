import pandas
#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}
data= pandas.read_csv ("nato_phonetic_alphabet.csv")
phondict={row.letter: row.code for(index,row) in data.iterrows()}
word= input("Enter a word: ").upper()
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
output_list= [phondict [letter] for letter in word]
print(output_list)
