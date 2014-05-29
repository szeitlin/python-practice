class Ball:

	def __init__(self, color, size, direction):
		self.color = color
		self.size = size
		self.direction = direction

	def __str__(self):
		msg = "Hi, I'm a " + self.size + " " + self.color + " ball!"
		return msg

	def bounce(self):
		if self.direction == "down":
			self.direction = "up"     #has to be a single equals sign to assign!
			
myBall = Ball("red", "small", "down")
print "I just created a ball and gave it attributes at the same time!"

print myBall

print "Now I'm going to bounce the ball"
print
myBall.bounce()
print "now the ball is going", myBall.direction
