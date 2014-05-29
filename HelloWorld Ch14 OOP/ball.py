class Ball:

	def bounce(self):
		if self.direction == "down":
			self.direction = "up"     #has to be a single equals sign to assign!
			
myBall = Ball() #makes an instance of the class
myBall.direction = "down"
myBall.color = "red"
myBall.size = "small"

print "I just created a ball."
print "My ball is", myBall.size
print "My ball is", myBall.color
print "My ball's direction is", myBall.direction
print "Now I'm going to bounce the ball"
print 										#just to print a blank line I guess?
myBall.bounce() 
print "Now the ball's direction is", myBall.direction
