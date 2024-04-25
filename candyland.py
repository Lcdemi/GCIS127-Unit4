import random
p1_lost = False #global variables for lost turns
p2_lost = False
p3_lost = False
p4_lost = False

def create_deck(): #creates the deck and shuffles it
    deck = ["SR", "SR", "SR", "SR", "SP", "SP", "SP", "SP", "SY", "SY", "SY", "SY", "SB", "SB", "SB", "SB", "SO", "SO", "SO", "SO", "SG", "SG", "SG", "SG", "DR", "DR", "DR", "DP", "DP", "DP", "DY", "DY", "DY", "DB", "DB", "DB", "DO", "DO", "DO", "DG", "DG", "DG", "PM", "PN", "LP", "IC"]
    shuffled_deck = []
    cards = 45
    while cards >= 0:
        random_card = random.randint(0, cards)
        shuffled_deck.append(deck[random_card])
        #print(deck[random_card:random_card+1]) Test Code
        deck.remove(deck[random_card])
        cards -= 1
    #print(shuffled_deck) test code
    #print(deck) test code
    return shuffled_deck

def create_board(): #creates the game board
    #board_output = ['R', 'P', 'Y', 'BS35', 'O', 'G', 'R', 'P', 'Y', 'B', 'O', 'G', 'R', 'P', 'Y', 'B', 'O', 'GS24', 'R', 'P', 'PM', 'Y', 'B', 'O', 'G', 'R', 'PL', 'Y', 'B', 'O', 'G', 'R', 'PN', 'P', 'Y', 'B', 'O', 'G', 'R', 'P', 'Y', 'B', 'O', 'G', 'R', 'P', 'Y', 'B', 'O', 'LP', 'G', 'R', 'P', 'YL', 'B', 'O', 'G', 'R', 'P', 'Y', 'B', 'O', 'G', 'R', 'P', 'Y', 'IC', 'B', 'O', 'G', 'R', 'P', 'Y', 'B', 'O', 'G', 'R', 'P', 'Y', 'B', 'O', 'G', 'MC']
    board = []
    counter = 0
    for _ in range(78):
        #special objects
        if counter == 20:
            board.append("PM")
        if counter == 31: #spaces - 1
            board.append("PN")
        if counter == 47: #spaces - 2
            board.append("LP")
        if counter == 63: #spaces - 3
            board.append("IC")
        if counter == 3:
            board.append("BS35")
        elif counter == 17:
            board.append("GS24")
        elif counter == 25:
            board.append("PL")
        elif counter == 50:
            board.append("YL")
        elif counter % 6 == 0:
            board.append("R")
        elif counter % 6 == 1:
            board.append("P")
        elif counter % 6 == 2:
            board.append("Y")
        elif counter % 6 == 3:
            board.append("B")
        elif counter % 6 == 4:
            board.append("O")
        elif counter % 6 == 5:
            board.append("G")
        counter += 1
    board.append("MC")
    return board

def take_turn(player, board, deck): 
    player_position = player[1]
    player_card = deck[0]
    print("Player ", player[0], " drew a ", player_card, ".", sep="") #prints out the players drawn card
    #print(board[player_position:]) test code
    counter = 0
    if player_card == "SR": #single red 
        for value in range(player_position+1, 83):
            if board[value] == "R":
                player_position = value
                break
            if value == 82: #if player reaches the end
                player_position = 82
                break
    elif player_card == "SP": #single purple
        for value in range(player_position+1, 83):
            if board[value] == "P" or board[value] == "PL":
                player_position = value
                break
            if value == 82:
                player_position = 82
                break
    elif player_card == "SY": #single yellow
        for value in range(player_position+1, 83):
            if board[value] == "Y" or board[value] == "YL":
                player_position = value
                break
            if value == 82:
                player_position = 82
                break
    elif player_card == "SB": #single blue
        for value in range(player_position+1, 83):
            if board[value] == "B" or board[value] == "BS35":
                player_position = value
                break
            if value == 82:
                player_position = 82
                break
    elif player_card == "SO": #single orange
        for value in range(player_position+1, 83):
            if board[value] == "O":
                player_position = value
                break
            if value == 82:
                player_position = 82
                break
    elif player_card == "SG": #single green
        for value in range(player_position+1, 83):
            if board[value] == "G" or board[value] == "GS24":
                player_position = value
                break
            if value == 82:
                player_position = 82
                break
    elif player_card == "DR": #double red
        for value in range(player_position+1, 83):
            if board[value] == "R":
                player_position = value
                counter += 1
                if counter > 1:
                    player_position = value
                    break
            if value == 82:
                player_position = 82
                break
    elif player_card == "DP": #double purple
        for value in range(player_position+1, 83):
            if board[value] == "P" or board[value] == "PL":
                player_position = value
                counter += 1
                if counter > 1:
                    player_position = value
                    break
            if value == 82:
                player_position = 82
                break
    elif player_card == "DY": #double yellow
        for value in range(player_position+1, 83):
            if board[value] == "Y" or board[value] == "YL":
                player_position = value
                counter += 1
                if counter > 1:
                    player_position = value
                    break
            if value == 82:
                player_position = 82
                break
    elif player_card == "DB": #double blue
        for value in range(player_position+1, 83):
            if board[value] == "B" or board[value] == "BS35":
                player_position = value
                counter += 1
                if counter > 1:
                    player_position = value
                    break
            if value == 82:
                player_position = 82
                break
    elif player_card == "DO": #double orange
        for value in range(player_position+1, 83):
            if board[value] == "O":
                player_position = value
                counter += 1
                if counter > 1:
                    player_position = value
                    break
            if value == 82:
                player_position = 82
                break
    elif player_card == "DG": #double green
        for value in range(player_position+1, 83):
            if board[value] == "G" or board[value] == "GS24":
                player_position = value
                counter += 1
                if counter > 1:
                    player_position = value
                    break
            if value == 82:
                player_position = 82
                break
    else: #cards drawn other than colors (pm, pn, lp, ic)
        for space in board:
            if player_card == "PM": #peppermint
                if space == "PM":
                    player_position = 20
                    break
            elif player_card == "PN": #peanut
                if space == "PN":
                    player_position = 32
                    break
            elif player_card == "LP": #lollipop
                if space == "LP":
                    player_position = 49
                    break
            elif player_card == "IC": #icecream
                if space == "IC":
                    player_position = 66
                    break
        
    if player_position == 3: #BS35 shortcut
        player_position = 35
        print("Player", player[0], "took a shortcut!")
    if player_position == 17: #GS24 shortcut
        player_position = 24
        print("Player", player[0], "took a shortcut!")
    return player_position #returns the index of the players position

def play_game(num_players): #plays the game with the amount of players declared in the parameter
    global p1_lost #redeclares the global variables for the play_game function
    global p2_lost
    global p3_lost 
    global p4_lost
    deck = create_deck() #creates shuffled deck
    board = create_board() #creates board
    #print(board) test code
    winner = False
    winning_player = ""
    if int(num_players) >= 1: #assigns players
        p1 = ("Red", 0)
    if int(num_players) >= 2:
        p2 = ("Yellow", 0)
    if int(num_players) >= 3:
        p3 = ("Blue", 0)
    if int(num_players) == 4:
        p4 = ("Green", 0)
    while winner != True: #while winner is not declared
        if int(num_players) >= 1: #if one player is in the game
            if p1_lost != True:
                p1_position = take_turn(p1, board, deck) #takes the turn for the player
                p1 = ("Red", p1_position)
                #print(p1_position)
                print("Player ", p1[0], " has landed on ", board[p1_position], p1_position + 1, ".", sep="")
                deck.remove(deck[0]) #removes picked card from the deck
                if p1_position == 26: #purple licorice space (losing a turn)
                    print("Player ", p1[0], " lost a turn", sep="")
                    p1_lost = True
                if p1_position == 53: #yellow licorice space (losing a turn)
                    print("Player ", p1[0], " lost a turn", sep="")
                    p1_lost = True
                if p1_position == 82: #multicolored space (wins game)
                    winner = True
                    winning_player = "Red"
                    break
            else:
                p1_lost = False
        if int(num_players) >= 2: #if two players are in the game
            if p2_lost != True:
                p2_position = take_turn(p2, board, deck)
                p2 = ("Yellow", p2_position)
                print("Player ", p2[0], " has landed on ", board[p2_position], p2_position + 1, ".", sep="")
                deck.remove(deck[0])
                if p2_position == 26:
                    print("Player ", p2[0], " lost a turn", sep="")
                    p2_lost = True
                if p2_position == 53:
                    print("Player ", p2[0], " lost a turn", sep="")
                    p2_lost = True
                if p2_position == 82:
                    winner = True
                    winning_player = "Yellow"
                    break
            else:
                p2_lost = False
        if int(num_players) >= 3: #if three players are in the game
            if p3_lost != True:
                p3_position = take_turn(p3, board, deck)
                p3 = ("Blue", p3_position)
                print("Player ", p3[0], " has landed on ", board[p3_position], p3_position + 1, ".", sep="")
                deck.remove(deck[0])
                if p3_position == 26:
                    print("Player ", p3[0], " lost a turn", sep="")
                    p3_lost = True
                if p3_position == 53:
                    print("Player ", p3[0], " lost a turn", sep="")
                    p3_lost = True
                if p3_position == 82:
                    winner = True
                    winning_player = "Blue"
                    break
            else:
                p3_lost = False
        if int(num_players) >= 4: #if four players are in the game
            if p4_lost != True:
                p4_position = take_turn(p4, board, deck)
                p4 = ("Green", p4_position)
                print("Player ", p4[0], " has landed on ", board[p4_position], p4_position + 1, ".", sep="")
                deck.remove(deck[0])
                if p4_position == 26:
                    print("Player ", p4[0], " lost a turn", sep="")
                    p4_lost = True
                if p4_position == 53:
                    print("Player ", p4[0], " lost a turn", sep="")
                    p4_lost = True
                if p4_position == 82:
                    winner = True
                    winning_player = "Green"
                    break
            else:
                p4_lost = False
    return winning_player #returns winning player

def main():
    players = input("How many players (1-4): ") #declares # of players in the game
    winner = play_game(players) #runs play_game function
    print("Player", winner, "Wins!") #prints winner

if __name__ == "__main__":
    main() #call to main