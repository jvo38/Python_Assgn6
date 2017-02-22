#Jimmy Vo
#Jimmyvo866@gmail.com
#CPSC 223P
#Assignment 6

class Permutation:
	def __init__(self, l):
		self.l = l
	
	def __iter__(self):
		while True:
			self.l = ''.join(self.l) #join list to make string
			for x, y in enumerate(self.l): #(0, a),(1,b),(2,c)
				z = (self.l[:x] + self.l[x+1:]) #last two letters of string
				yield y + z #add the letter taken out with 2 remaining letter
				z = (z[1] + z[0]) #switch remaining letters
				yield y + z
def main():
	s = ['a','b', 'c']
	p = Permutation(s)
	for i in p:
		print(i)
		if i == 'cba':
			break

if __name__ == '__main__':

	main()
