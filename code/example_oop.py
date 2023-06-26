'''
Example For OOP

Game
-welcome  message : options[games] -----> option exit
-enter game number ----> start game
-ask play again ---> play agin ----> close
-game :
  - sentace ---> sentance no duplicate
  - x,y ----> [1:100] 

'''


class Game:
    def __init__(self):
        while True:    
            print('''
            welcome , choose one of out game ..
                1 : sentance_no_dublicate
                2 : divided_by_two 
                3 : user exit ''')
            
            user_choice = int(input("Enter game number: "))
            if user_choice == 1:
                sentance = input("Enter Your sentance: ")
                self.sentance_no_dublicate(sentance)

            elif user_choice == 2:
                x = int(input("Enter your number one or X value: "))
                y = int(input("Enter your number two or y value: "))
                self.divided_by_two(x,y)    
            elif user_choice == 3:
                print("Godbye .... ")
                break
            else:
                print("please enter number between 1:3")

            play_again = input("press any key to play agin, n to exit : ") 

            if play_again == "n":
                print("Godbye .... ")
                break 
            

    def sentance_no_dublicate(self,sentance):
            words = sentance.split()
            result = []
            for  word in words :
                if word not in result:
                    result.append(word)
            print( ' '.join(result))
                



    def divided_by_two(self, x ,y):
        result = []
        for i in range(1,101):
            if i % x ==0 and i% y ==0:
                result.append(i)
        print(result)


game_1 = Game()

