class GameObject:

	def __init__(self,name):
		self.name = name
	
	def pickUp(self, player):
		#add to collection
		
class Coin(GameObject):
	def __init__(self, value):
		GameObject.__init__(self) 		#inherit GameObject's init and add to it
		self.value = value
		
	def spend(self, buyer, seller):
		#remove from buyer's money and add to seller's money