#Alex Hornick
#June 8th, 2016
#This is a dice game that operates similar to BlackJack
#A player will play against a computer and compete to reach 21 first, or go bust/freeze.

import random #for random generation of die number

#the player class is used for both the player and the computer
class player:
	diceTotal = 0
	status = 'alive'  #can be 'alive' or 'frozen'

	def getTotal(self):
		return self.diceTotal
	def getStatus(self):
		return self.status
	def updateTotal(self, dieNumber): #when they roll a die
		self.diceTotal += dieNumber
	def statusChange(self, status): #when they decide to freeze
		self.status = status


#returns a random die from 1 to 6
def getDie():
	die = random.randrange(1, 6, 1)
	return die


#this function is a round of play, for the player and computer
def playRound():
	print "\nYour current total is ", player1.getTotal()
	answer = raw_input("Would you like to roll a die? ")
	
	if answer == "yes":
		die = getDie()
		print '\nThe die you rolled was ', die
		player1.updateTotal(die)
		print "Your new total is ", player1.getTotal()
	else:
		print 'You have chosen to freeze.'
		player1.statusChange('frozen')

	#Roll dice or freeze for computer now
	print "\nThe computer's dice total is: ", comp1.getTotal()
	if comp1.getStatus() == 'alive':
		if comp1.getTotal() < 19:
			die = getDie()
			comp1.updateTotal(die)
			print 'The computer has a new total of ', comp1.getTotal()
		else:
			print 'The computer has frozen with a total of: ', comp1.getTotal(), '\n'
			comp1.statusChange('frozen')
	else: 
		print "The computer is frozen with a total of ", comp1.getTotal()


#This function determines the status of the game and if it should continue
def getGameStatus():
	status = 'continue';
	if comp1.getStatus() == 'frozen' and player1.getStatus() == 'frozen':
		status = 'freezeTie'
	elif player1.getTotal() == 21:
		status = 'playerWin'
	elif comp1.getTotal() == 21:
		status = 'computerWin'
	elif player1.getTotal() > 21:
		status = 'playerLose'
	elif comp1.getTotal() > 21:
		status = 'computerLose'

	return status


#when the game has reached a stopping point, print an ending message
def finishGame(gameStatus):
	print '\n'
	if gameStatus == 'freezeTie':
		if player1.getTotal() > comp1.getTotal():
			print "Player 1 wins with a total of ", player1.getTotal()
		else:
			print "Computer wins with a total of ", comp1.getTotal()
	elif gameStatus == 'playerWin':
		print 'You reached 21! Congrats! You won!'
	elif gameStatus == 'computerWin':
		print 'The computer reached 21 first....sorry'
	elif gameStatus == 'playerLose':
		print 'You went over 21...you lost'
	elif gameStatus == 'computerLose':
		print 'The computer went over 21...you won!'


#this is what controls most of the game
def beginGame():
	game = True
	while game == True:
		playRound()
		gameStatus = getGameStatus()
		
		#when the game is over
		if gameStatus != 'continue':
			game = False;
			finishGame(gameStatus)




		

#Description for users
print "Welcome to Alex Hornick's Dice Simulation Game"
print "The rules are simple. "
print "The goal is for your consecutive dice rolls to add up to or be closer to the number 21 than your computer opponent."
print "Think BlackJack. After each roll, you will be told your total, and you can either freeze or continue for another die."
print "Good luck!\n"

#initiate players, begin game
player1 = player()
comp1 = player()
beginGame()


