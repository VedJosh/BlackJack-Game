from BLACKJACK_ART import Card, cards
import random

class Player:
    def __init__(self,name,money_left) -> None:
        self.player_name = name 
        self.player_card = []
        self.score = 0
        self.win = None # initialized to neither win nor lose
        self.lcards = []
        self.money = money_left
    
    def initialize_cards(self): # adds 2 cards to user and computer's hand
        self.player_card = [random.choice(cards) for j in range(2)]

    def display_cards(self,key=''): # key tells whether last card is to be hidden
        self.lcards = [_[0] for _ in self.player_card] 
        c = [Card(i,'') for i in self.lcards] 

        if key == 'Computer': # last card is hidden if key is Computer
            c[-1]=Card(-1,'Computer') 
        
        # all the cards are displayed
        for i in range(len(c[0].card)):
            for j in range(len(c)):
                print(c[j].card[i], end = '\t')
            print()
    
    # score is updated/calculated
    def calc_score(self):
        self.score = 0
        for eachcard in self.player_card:
            if eachcard != ('A',11): # if card is not ACE
                self.score += eachcard[1] 
            else:
                if (self.score + 11) > 21: 
                    self.score += 1 # if adding ACE as 11 can bust the user
                else: 
                    self.score += 11 # if adding ACE as 11 will not bust the user

    def hit_card(self,u_choice): # if user choice is to hit the card, random card is equipped
        if u_choice=='hit':
            self.player_card.append(random.choice(cards))
    
    def if_busted(self): # it changes win attribute to False if player is busted
        if self.score>21:
            self.win = False
    
    def isblackjack(self):
        return (self.score==21 and len(self.player_card)==2)

def user_choice(): # takes user input and returns the same
    playerchoice = input("Do you want to hit or stand (hit/stand): ").lower()
    return playerchoice

def blackjack(user_name,money_left_u,money_left_c): 
    # creates user and computer instances
    players_list = user, computer = Player(user_name,money_left_u), Player('Computer',money_left_c)
    for _ in players_list:
        _.initialize_cards() # initialize 2 cards for user and computer 
        print(_.player_name) 
        _.display_cards(_.player_name) # displays card for user and computer. If player is computer, last card is hidden
        _.calc_score() # calculates the score
        print(f"{_.player_name} has ${_.money}")
    print('Your Total :',user.score) 
    
    c=''
    # hit or stand for user
    while user.win!=False and c!='stand':
        
        # check if user has blackjack
        if user.isblackjack(): 
            print("Your BlackJack")
            print('You win 😁')
            user.win=True
            print("You get $200")
            user.money+=200
            computer.money-=200
            break
        
        # taking user choice to hit or stand if he does not get blackjack
        c = user_choice()
        while c!='hit' and c!='stand': # handles exeption if user gives invalid move
            print("That's not a move!") 
            c = user_choice()
        user.hit_card(c)
        user.display_cards()
        user.calc_score()
        user.if_busted()
        print('Your Total :',user.score) 

    # if user is busted
    if user.win==False: 
        print('You Busted')
        print('You lose $150 😤')
        print(f"Computer's final score: {computer.score}, Your final score: {user.score}") 
        user.money-=150
        computer.money+=150
    
    elif user.win!=True: # if user is not busted and not having blackjack
        # checks if computer has a blackjack 
        if computer.isblackjack(): 
            print("Computer's BlackJack")
            print('You lose $200 😤')
            user.money-=200
            computer.money+=200
        else:
            # hit or stand for computer
            while computer.score<17:
                computer.hit_card('hit')
                computer.calc_score()
                computer.if_busted()
            
            print(user.player_name)
            user.display_cards()
            print(computer.player_name)
            computer.display_cards()
            print(f"Computer's final score: {computer.score}, Your final score: {user.score}") 

            # if computer is busted
            if computer.win==False:  
                print('Opponent went over. You win 😁')
                user.money+=150
                computer.money-=150
                print("You get $150")
            
            # checks who has higher score
            elif user.score>computer.score:
                print('You win 😁')
                user.money+=150
                computer.money-=150
                print("You get $150")
            elif user.score==computer.score:
                print("TIE")
            else:
                print('You lose 😤')
    return user.money>=150, computer.money>=150, user.money, computer.money