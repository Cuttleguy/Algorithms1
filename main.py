class Fraction:
  def __init__(self,top,bottom):
    self.numerator=top
    self.denomenator=bottom
  def show(self):
    print(f'{self.numerator}/{self.denomenator}')
  def __str__(self):
   return f'{self.numerator}/{self.denomenator}'
  def __add__(self, other):
      new_numerator=self.numerator*other.denomenator
