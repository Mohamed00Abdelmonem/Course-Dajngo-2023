
# # Complete the solve function below.
# try:
        
#     def solve(s):
        
#         word = s.split()
#         result = [w.capitalize() for w in word ]
#         print(' '.join(result))
        
    
#     solve("hello world")
    
# except Exception as e:
#     print(e)



# def solve(s):
#     words = s.split()
#     capitalized_words = [word.capitalize() for word in words]
#     capitalized_name = ' '.join(capitalized_words)
#     return capitalized_name

# # Example usage

# capitalized_name = solve("hello world ")
# print(capitalized_name)



# def solve(s):
#     names = s.split()  # Split the full name into a list of names

    
#     # Capitalize the first letter of each name
#     capitalized_names = [name.capitalize() for name in names]
    
#     capitalized_full_name = ' '.join(capitalized_names)  # Join the capitalized names back into a string
    
#     return capitalized_full_name

# # Example usage

# print(solve('hello   world  lol'))

# def solve(s):
#     names = s.split()  # Split the full name into a list of names

#     # Capitalize the first letter of each name while preserving the rest of the word
#     capitalized_names = [name[0].title() + name[1:] for name in names]

#     capitalized_full_name = ' '.join(capitalized_names)  # Join the capitalized names back into a string without additional spacing

#     return capitalized_full_name

# Example usage
# print(solve("hello   world  lol"))




# var = "James Bond"
# print(var[2::-1])

# sampleSet = {"Jodi", "Eric", "Garry"}
# sampleSet.add( "Vicki")
# print(sampleSet)




# def minion_game(string):
#     s=len(string)
#     vowel = 0
#     consonant = 0
     
#     for i in range(s):
#         if string[i] in 'AEIOU':
#            vowel+=(s-i)
#         else:
#            consonant+=(s-i)
                
#     if vowel < consonant:
#         print('Stuart ' + str(consonant))
#     elif vowel > consonant:
#         print('Kevin ' + str(vowel))
#     else:
#         print('Draw')

# minion_game("Hello")




from itertools import product
a = input("entera: ") 
b = input("enterb: ") 
a= a.split()
b= b.split()


for i in a:
    for ii in b:
        print(f" ({i},{ii})" ,end='')
