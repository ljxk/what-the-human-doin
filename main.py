class human:
  def __init__(self,_height,_skincolor,_haircolor,_amountoffeet,_eyecolor,_gender):
    self.height = _height
    self.skincolor = _skincolor
    self.haircolor = _haircolor
    self.amountoffeet = _amountoffeet
    self.eyecolor = _eyecolor
    self.gender = _gender
    self.foodinbelly = 0
    self.toomuchfood = 20
  def die(self):
    print ("the human dies")
  
def eat(self):
  if self.foodinbelly < self.toomuchfood:
    self.foodinbelly = self.foodinbelly + 1
    print ("the human eats")
  else:
    print ("the human dies")

human = human("5ft 9in", "beige", "brown", 2, "brown", "male")
human.eat()
  
  
    