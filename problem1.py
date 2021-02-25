#!python3
"""
Print the list named "people"
Ask the user to enter a word from the list
Ask the user to enter another word
Replace the first word with the second word.

inputs:
string
string

outputs:
list

example:
['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Rick']
Choose a person from the list to replace:Rick
Enter the replacement:Dan
['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Dan']

"""

people = ['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Rick']
print(people)

name1=input("Enter a name from the list for replacement: ").strip()
id=people.index(name1)
people.remove(name1)

name2=input("Enter the replacement word: ").strip()
people.insert(int(id),name2)
print(people)
