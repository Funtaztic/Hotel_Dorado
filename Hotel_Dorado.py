# This will be a TRPG, Text-Based adventure game with
# lots of rooms, friend, enemies, hidden treasures, secrets,
# collectibles and more. Gain XP, save HP, have FUN! =D
# (listening to GameOfThrones music)...make them LIE! xD
# The player can not trust anyone! (after enough interactions)
# 'You can only ask 1 question'-type of characters.
# Moody characters, if (s)he's happy, will help you more.
# Lie-detector / Truth serum. (you know how it works)
# Give items (presents) to characters, make them happy.
# Give them alcohol? - makes happy, more likely to say dumb shit.
# Likelyhood: random choice out of 10(0), (7xYes + 3xNo = 70% chance.)
#   make a likelyhood situation where there is no option where we get to win. small help/big help, but no solution.
# Variables: Happy = 1 Helpful = 1 ---> =2. If sum >=2, big help comes.
# Stats print loop: print stats, run a function, stats, then another function.
#   Make a variable: storyline. add +1 to proceed to next one? (bad idea?)
#       or just include stats_print in all functions.

# Variables:
HP = 100
XP = 0
MONEY = 100
money_given = 0

def just_a_list_of_stages():
    print "---------------"
    print "Stages of the game:"
    print "Quasimodo"
    print "end_game"
    print "stats_print"
    print "---------------"

def Quasimodo():
    stats_print()
    print "Hi, I'm Quasimodo. Do you want to go inside? (yes/no)"
    Quasimodo_answer = raw_input()
    if Quasimodo_answer == "yes":
        print "You are in! :D"
        end_game()
    else:
        print "Then why are you here?"
        end_game()

def give_me_money():
    global MONEY
    global PoorJohnMoney
    PoorJohnMoney = 0
    while MONEY >= 0:
        print "Hi, I am PoorJohn. Please give me money! I have %r money now." % PoorJohnMoney
        print "How much would you give? :)"
        money_given = int(raw_input())
        MONEY = MONEY - money_given
        PoorJohnMoney = PoorJohnMoney + money_given
        print "HAHAHAH! I have %r money now!" % PoorJohnMoney
        stats_print()
        
        
def end_game():
    stats_print()
    print "Press Enter to close window."
    end_game = raw_input()

def stats_print():
    print "HP:      %r" %HP
    print "XP:      %r" %XP
    print "MONEY:   %r" %MONEY

give_me_money()
just_a_list_of_stages()
Quasimodo()