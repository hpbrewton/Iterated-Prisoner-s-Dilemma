class Dilemma:
	def __init__(self,
			player1,
			player2,
			):
		self.player1 = player1
		self.player2 = player2
		self.ww = (0.5, 0.5)
		self.lw = (0, 1)
		self.wl = (1, 0)
		self.ll = (0, 0)
		self.allowed = ["steal", "split"]

	def run(self, ngames):
		s1 = 0
		s2 = 0
		for i in range(ngames):
			m1 = self.player1.play()
			m2 = self.player2.play()
			lose1 = m1 not in self.allowed
			lose2 = m2 not in self.allowed
			game = None
			if lose1 and lose2:
				game = self.ll
			if lose1 and not lose2:
				game = self.lr
			if not lose1 and lose2:
				game = self.rl
			else:
				if m1 == "split" and m2 == "split":
					game = self.ww
				elif m1 == "split" and m2 == "steal":
					game = self.lw
				elif m1 == "steal" and m2 == "split":
					game = self.wl
				elif m1 == "steal" and m2 == "steal":
					game = self.ll
			s1 += game[0]
			s2 += game[1]
		return (s1, s2)
