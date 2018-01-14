#
# Cameron Hawtin
#
# This program is a hockey/NHL quiz game that uses multi-dimensional lists 
# to access its' information. In this assignment we explore function
# definitions as well as different variations of using lists. 
#

# this function translates a, b, and c inputs into their respective integer values
def translateMCAnswer(answer):
	if answer == "a" or answer == "A":
		answer = 0
	elif answer == "b" or answer == "B":
		answer = 1
	elif answer == "c" or answer == "C":
		answer = 2
	else:
		print("Invalid input. Please enter 'a', 'b', or 'c'.")
	return answer

# this function translates t and f inputs into their respective True/False values
def translateTFAnswer(answer):
	if answer == "T" or answer == "t":
		answer = True
	if answer == "F" or answer == "f":
		answer = False
	else:
		print("Invalid input. Please enter 't' or 'f'.")
	return answer

# this is the main function that holds the code for the game and the questions	
def game(mchoiceList, tfList):
	
	# These are all the questions inside of their lists 
	# MC Questions
	quit = False
	mchoiceList[0] = ["Which former NHL goaltender recorded the all-time most wins?", 0, ["Matrin Brodeur", "Patrick Roy", "Ed Belfour"], -1, 1]
	mchoiceList[1] = ["Which NHL team sports a red home jersey?", 2, ["Los Angeles Kings", "Edmonton Oilers", "Detroit Red Wings"], -1, 2]
	mchoiceList[2] = ["What is Ottawa's NHL team?", 1, ["Ottawa Canucks", "Ottawa Senators", "Ottawa Maple Leafs"], -1, 4]
	mchoiceList[3] = ["Which player famously wore the jersey number 99?", 1, ["Mario Lemieux", "Wayne Gretzky", "Maurice Richard"], -1, 5]
	mchoiceList[4] = ["Who is the captain of the Pittsburgh Penguins?", 0, ["Sidney Crosby", "Alexander Ovechkin", "Evgeni Malkin"], -1, 7]
	mchoiceList[5] = ["Who won the gold medal at the 1980 Olympics for ice hockey?", 1, ["Canada", "U.S.A.", "Soviet Union"], -1, 8]
	mchoiceList[6] = ["Who was the NHL's 2015 first round draft pick?", 2, ["Auston Matthews", "Jack Eichel", "Connor McDavid"], -1, 10]
	mchoiceList[7] = ["Which former NHL player won the all-time most Conn Smythe Trophies?", 1, ["Wayne Gretzky", "Patrick Roy", "Bobby Orr"], -1, 11]
	mchoiceList[8] = ["How many periods are there in an NHL hockey game?", 1, ["2 periods", "3 periods", "4 periods"], -1, 13]
	mchoiceList[9] = ["How many teams are there in the NHL as of 2016?", 2, ["20 teams", "25 teams", "30 teams"], -1, 14]
	# TF Questions
	tfList[0] = ["In the NHL, a regular penalty is 3 minutes long. (T)rue or (F)alse?", False, -1, 3]
	tfList[1] = ["The Montreal Canadiens have won 24 Stanley Cups. (T)rue or (F)alse?", True, -1, 6]
	tfList[2] = ["The Chicago Blackhawks won the 2015 Stanley Cup. (T)rue or (F)alse?", True, -1, 9]
	tfList[3] = ["Sidney Crosby won the Calder Trophy for rookie of the year in 2005. (T)rue or (F)alse?", False, -1, 12]
	tfList[4] = ["There is no limit to the degree of a hockey stick's curve in the NHL. (T)rue or (F)alse?", False, -1, 15]
# While loop loops through the game until the user decides to end it	
	while quit == False:
		score = 0
		print("\nWelcome to the Hockey/NHL Trivia game.")	
		print("For the multiple choice questions, please answer with 'a', 'b', or 'c'.")
		print("For the true/false questions, please answer with 't' or 'f'.")
		input("\nPress any key to begin.")
		
# MULTI-CHOICE QUESTIONS
		for i in range (0, 10):
			print("\nQuestion ",i+1,".  ", mchoiceList[i][0], sep="")
			print("    a.", mchoiceList[i][2][0])     
			print("    b.", mchoiceList[i][2][1])  
			print("    c.", mchoiceList[i][2][2]) 
			#apply answer to list
			answer = input()
			#check if answer is valid
			while answer != "a" and answer != "b" and answer != "c" and answer != "A" and answer != "B" and answer != "C":
				print("Invalid input. Please enter a valid answer.")
				answer = input()
			answer = translateMCAnswer(answer)
			mchoiceList[i][3] = answer
			#check if answer is correct
			if mchoiceList[i][3] == mchoiceList[i][1]:
				print("\nCorrect!")
				score += 1
			else:
				print("\nIncorrect.")
			print("Your current score is", score, "out of 15.")
			#ask to quit
			q =  input("\nPress (y) if you would like to quit, and any key to continue. ")
			if q == "y":
				print("Thanks for playing!")
				quit = True
				break
			print()
		
# TRUE-FALSE QUESTIONS
		if quit == False:
			for j in range (0, 5):
				print("\nQuestion ", j+11,".  ", tfList[j][0], sep="")
				#apply answer to list
				answer = input()
				#check if answer is valid
				while answer != "t" and answer != "f" and answer != "T" and answer != "F":
					print("Invalid input. Please enter a valid answer.")
					answer = input()
				answer = translateTFAnswer(answer)
				tfList[j][2] = answer
				#check if answer is correct
				if tfList[j][2] == tfList[j][1]:
					print("\nCorrect!")
					score += 1
				else:
					print("\nIncorrect.")
				if j < 4: 	
					print("Your current score is", score, "out of 15.")
					#ask to quit
					q =  input("\nPress (y) if you would like to quit, and any key to continue. ")
					if q == "y":
						print("Thanks for playing!")
						quit = True
						break	
					print()
				else:
					print("Your final score is", score, "out of 15.")
					#calculate percent correct
					percentCorrect = float(score)/15*100
					print("You got ", format(percentCorrect, ".2f"), "% of the questions correct.", sep="")
					#ask to play again
					q =  input("\nWould you like to play again?(y/n): ")
					while q != "n" and q != "y" and q != "N" and q != "Y":
						print("Invalid input. Please enter a valid answer.")
						q = input()
					if q == "n":
						print("Thanks for playing!")
						quit = True
						break	
					print()		
		
def main():
	mchoiceList = [-1] * 10
	tfList = [-1] * 5
	game(mchoiceList, tfList)

main()
