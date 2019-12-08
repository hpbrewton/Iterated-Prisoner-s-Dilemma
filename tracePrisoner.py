class Prisoner:
	previousEnemyMove = "split"	

	def __init__(self):
		pass

	# takes the string "steal" or "split" representing the other player's move
	# result is ingored
	def result(self, other):
		previousEnemyMove = other	
	

	# return the string "steal" or "split" representing your move
	def play(self):
		if previousEnemyMove == "split":
			return "split"
		
		return "steal"
