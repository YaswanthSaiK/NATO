# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }

#Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
import pandas
df = pandas.read_csv("nato_phonetic_alphabet.csv")
df.to_dict()
#Loop through rows of a data frame23
# for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    # pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
lis = {row.letter : row.code for (index, row) in df.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
isok = True
while isok:
    h = input("enter your word: ")
    try:
        li = [lis[n.upper()] for n in h]
    except KeyError:
        print("Sorry! alphabets only please.")
    else:
        print(li)
        isok = False
