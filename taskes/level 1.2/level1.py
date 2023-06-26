# Python Task Level 1 :


# **********************************************************************************************


# 1. Create a python function that takes 2 numbers x,y and prints 2 lists containing the odd and even numbers in
# the x,y range


# def numbers(start,end):
     
    ################################# list comprhanchan ################################

    # even = [int(i) for i in range (start,end+1) if i%2==0 ]
    # odd = [int(i) for i in range (start,end+1) if i%2 !=0 ]
    # print(f"even = {even}")
    # print (f"odd =  {odd}")

# print(numbers(2,9))


    ####################### the normal way #################################


#     even = []
#     odd = []
#     for i in range(start, end+1):
#         if i % 2 == 0 :
#             even.append(i)    
#         else:
#             odd.append(i)
#     return(even,odd)


# even,odd= numbers(2,9)
# print(f"enve =  {even}")   
# print(f"odd =  {odd}")   




# **********************************************************************************************

# 2. Create a python function that takes 2 numbers x,y and prints all the numbers between 1 and 100 than can
# be divided on x,y


    ################################# list comprhanchan ################################


# def divided_by_x_and_y(x,y):

    # var = [int(i) for i in range(1, 101) if i % x == 0 and i % y == 0]
    # return var



    ####################### the normal way #################################

#     value = []
#     for i in range(1,101):
#         if i % x ==0 and i % y ==0 :
#             value.append(i)
#     return value
    
# print(divided_by_x_and_y(3,5))




# **********************************************************************************************


# 3. Create a python function that takes 2 numbers x, y and prints the multiplication table from x to y

    ####################### the normal way #################################


# def multiplication_table(x,y):
#     for i in range(1,12+1):
#         for ii in range (x,y+1):
#          print(f" {i} * {ii} = {i*ii}")
        
# multiplication_table(1,9)
     



    ################################# list comprhanchan ################################



# def multiplication_table(x,y):
#     value = [[i,ii,i*ii] for i in range(x,y+1) for ii in range (1,y+1) ]
#     print(value)
#     for entry in value:
#         print(f"{entry[0]} * {entry[1]} = {entry[2]}")

    
# print(multiplication_table(2,5))


# **********************************************************************************************


# # 4. Create a function that takes a sentence and prints the sentence without duplicated words


    ####################### the normal way #################################


# def no_duplicated(sentenc):
#     result = []
#     words = sentenc.split(' ')
#     for word in words:
#         if word not in result:
#             result.append(word)
#             r = ' '.join(str(e) for e in result)
#     return r
# print(no_duplicated("aya is is aya is are you"))        



    ################################# list comprhanchan ################################


# def no_duplicated(sentence):
#     words = sentence.split(' ')
#     unique_words = []
#     result_list = [word for word in words if word not in unique_words]
#     x = " ".join(str(e) for e in result_list)
#     return x
# print(no_duplicated("hi mohamed hi and ahmed "))





# **********************************************************************************************



# 5. Create a function that takes a sentence and prints how many words in the sentence (do not count the
# spaces)

    ####################### The Normal way #################################


# def count_len_words_in_sentence(sentence):
#     list_empty = []
#     for word in sentence:
#         if word == " ":
#             continue
#         else:
#             list_empty.append(word)

#     return len(list_empty)
# print(count_len_words_in_sentence("hello  mr Mohamed"))        


    ################################# list comprhanchan ################################



# def count_len_words_in_sentence(sentence):
#     result = [len(word) for word in sentence if word != " " ]
#     return sum(result)

# print(count_len_words_in_sentence("hello  mr Mohamed"))        


# **********************************************************************************************



# 6. Create a function that takes a sentence and word and remove the word from the sentence


    ####################### The Normal way #################################

# def remove_word_from_sentence(sentence, word):
#     empty_list = []
#     x = sentence.split(" ")
#     for i in x:
#         if i == word:
#             continue
#         elif i != word:
#             empty_list.append(i)
#             x = " ".join(str(e) for e in empty_list)
#     return x
# print(remove_word_from_sentence("remove the word from the sentence", "the"))        


    ################################# list comprhanchan ################################


# def remove_word_from_sentence(sentence, word):
#     i = sentence.split(" ")
#     list_result = [str(x) for x in i if x != word  ]
    
#     print (' '.join (str(e) for e in list_result))

# (remove_word_from_sentence("remove the word from the sentence", "the"))        




# **********************************************************************************************


# 7. Create a function takes a sentence and a word and prints how many time the word used in the sentence

# def count_word(sentence ,word):
#     x = sentence.split(' ')
#     n = 0
#     for i in x:
#         if i == word:   
#            n+=1
#     print(n)
# count_word("hello mohamed hello hello hello", "hello")


    ################################# list comprhanchan ################################



# def count_word(sentence, word):
#     split_sentence = sentence.split(" ")
#     list_result = [length for length in split_sentence if length == word]
#     print(len(list_result))

# count_word("hello mohamed hello hello hello", "hello")






# **********************************************************************************************




# 8. Create a function that takes x,y and prints all the number that can be divide by y from x to 100


    ################################# list comprhanchan ################################



# def divied_by_y (x,y):
#     list_result = [int(i) for i in range(x,101) if i % y == 0 ]
#     result = ' '.join(str(e) for e in list_result)
#     print(f"{result}")

# divied_by_y(6,3)    




    ####################### The Normal way #################################



# def divied_by_y(x,y):
#     for i in range(x,101):
#        if i % y ==0 :
        
#         print(i)

# print(divied_by_y(3,5))


# **********************************************************************************************
# **********************************************************************************************
# **********************************************************************************************
# **********************************************************************************************
# **********************************************************************************************
# **********************************************************************************************
# **********************************************************************************************
# **********************************************************************************************
