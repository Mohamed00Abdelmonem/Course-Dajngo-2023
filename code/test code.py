
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




# from itertools import product
# a = input() 
# b = input() 
# a= a.split()
# b= b.split()
# for i in a:
#     for ii in b:
#         print(f"({i},{ii}) " ,end='')

# from itertools import product
# a = map(int, input().split())
# b = map(int, input().split())

# print(*product(a, b))






# T = int(input())
# S = input()

# if 0 < T < 100:
#     if S == ".*" :
#         print ("True")
#     else:
#         print("False")    

# import re 
# T = int(input())
# S = re
# Enter your code here. Read input from STDIN. Print output to STDOUT


# import re
# for _ in range(int(input())):
#     ans = True
#     try:
#         reg = re.compile(input())
#     except re.error:
#         ans = False
#     print(ans)


# def solve(s):
#     word = s.split()
#     result = [w.capitalize() for w in word if 0 < len(word)<1000]
#     return (' '.join(result))
    
 
# print(solve("hello    mohamed"))
    


# N, M = map(int,raw_input().split()) # More than 6 lines of code will result in 0 score. Blank lines are not counted.
# for i in xrange(1,N,2): 
#     print ('.|.'*i).center(M,'-')
# print "WELCOME".center(M,'-')
# for i in xrange(N-2,-1,-2): 
#     print ('.|.'*i).center(M,'-')







# size = int(input("enter size : "))

# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# for i in range(size-1, -1,-1):
#     result = letters[:size-i]

#     result = (" ".join(result))
   
#     print(f"{size*'-'}-{result}-{result}-{size*'-'}")
# print(f"-------- {result} --------", end=" ")



def print_rangoli(size):
    w = 2 * (size + size - 1) - 1
    l = [chr(ord("a")+i) for i in range(size)]
    r = [chr(ord("a")+i) for i in range(size-1, -1, -1)]
    for i in range(size):
        print("-".join(e for e in r[0:i]+l[-1-i:]).center(w, "-"))
    for i in range(size-2, -1, -1):
        print("-".join(e for e in r[0:i]+l[-1-i:]).center(w, "-")) 

print(print_rangoli(5))





# r = [chr(ord("a")+i) for i in range(size-1, -1, -1)]

# print(r)