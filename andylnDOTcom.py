import random

class Prisoner:
	def __init__(self):
		self.stealPercentage = 0.75

	# takes the string "steal" or "split" representing the other player's move
	# result is ingored
	def result(self, other):
		if (other == "steal"):
			self.stealPercentage += 0.01
		if (other == "split"):
			self.stealPercentage -= 0.01

		if (self.stealPercentage < 0.00):
			self.stealPercentage = 0.00
		if (self.stealPercentage > 1.00):
			self.stealPercentage = 1.00

	# return the string "steal" or "split" representing your move
	def play(self):
		return random.choices(
			population=['steal', 'split'],
			weights=[self.stealPercentage, 1.00 - self.stealPercentage],
			k=1
		)[0]