from pacifist import Pacifist
from evil import Evil
from dilemma import Dilemma

if __name__ == "__main__":
	p = Pacifist()
	e = Evil()
	score = Dilemma(p, e).run(100)
	print(score)
