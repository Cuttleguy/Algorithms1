from algorithms import *

class Fraction:
  def __init__(self,top,bottom):

    self.numerator=top
    self.denomenator=bottom
    if top % 1 != 0 or bottom % 1 != 0:
        raise RuntimeError("Fraction parts are not integer")
    if bottom < 0:
        self.denomenator*=-1
        self.numerator*=-1
    common = gcd(self.numerator, self.denomenator)
    self.numerator=self.numerator//common
    self.denomenator=self.denomenator//common
  def show(self):
    print(f'{self.numerator}/{self.denomenator}')
  def __str__(self):
   return f'{self.numerator}/{self.denomenator}'
  def __repr__(self):
   return f'{self.numerator}/{self.denomenator}'
  def __add__(self, other):
      new_num=self.numerator*other.denomenator+self.denomenator*other.numerator
      new_den=self.denomenator*other.denomenator
      return Fraction(new_num, new_den)
  def __radd__(self, other):
      new_num=self.numerator*other.denomenator+self.denomenator*other.numerator
      new_den=self.denomenator*other.denomenator
      return Fraction(new_num, new_den)
  def __eq__(self, other):
      first_num = self.numerator * other.denomenator
      second_num = other.numerator * self.denomenator

      return first_num == second_num
  def __sub__(self, other):
      new_num = self.numerator * other.denomenator - self.denomenator * other.numerator
      new_den = self.denomenator * other.denomenator

      return Fraction(new_num, new_den)
  def __mul__(self, other):
      new_num=self.numerator*other.numerator
      new_den=self.denomenator*other.denomenator

      return Fraction(new_num,new_den)
  def __truediv__(self, other):
      flippedFraction= Fraction(other.denomenator,other.numerator)
      return self * flippedFraction
  def __gt__(self, other):
      lcmValue=lcm(self.denomenator,other.denomenator)
      num1=self.numerator*(lcmValue/self.denomenator)
      num2=other.numerator*(lcmValue/other.denomenator)
      return num1>num2
  def __lt__(self, other):
      lcmValue=lcm(self.denomenator,other.denomenator)
      num1=self.numerator*(lcmValue/self.denomenator)
      num2=other.numerator*(lcmValue/other.denomenator)
      return num1<num2
  def __le__(self, other):
      lcmValue=lcm(self.denomenator,other.denomenator)
      num1=self.numerator*(lcmValue/self.denomenator)
      num2=other.numerator*(lcmValue/other.denomenator)
      return num1<=num2
  def __ge__(self, other):
      lcmValue=lcm(self.denomenator,other.denomenator)
      num1=self.numerator*(lcmValue/self.denomenator)
      num2=other.numerator*(lcmValue/other.denomenator)
      return num1>num2
  def __iadd__(self, other):
      new_num = self.numerator * other.denomenator + self.denomenator * other.numerator
      new_den = self.denomenator * other.denomenator
      self.numerator=new_num
      self.denomenator=new_den
  def get_num(self):
      return self.numerator
  def get_dem(self):
      return self.denomenator



