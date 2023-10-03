from algorithms import *

class Fraction:
  def __init__(self,top,bottom):
    self.numerator=top
    self.denomenator=bottom
  def show(self):
    print(f'{self.numerator}/{self.denomenator}')
  def __str__(self):
   return f'{self.numerator}/{self.denomenator}'
  def __add__(self, other):
      new_num=self.numerator*other.denomenator+self.denomenator*other.numerator
      new_den=self.denomenator*other.denomenator
      common = gcd(new_num, new_den)
      return Fraction(new_num // common, new_den // common)
  def __eq__(self, other):
      first_num = self.numerator * other.denomenator
      second_num = other.numerator * self.denomenator

      return first_num == second_num
  def __sub__(self, other):
      new_num = self.numerator * other.denomenator - self.denomenator * other.numerator
      new_den = self.denomenator * other.denomenator
      common = gcd(new_num, new_den)
      return Fraction(new_num // common, new_den // common)
  def __mul__(self, other):
      new_num=self.numerator*other.numerator
      new_den=self.denomenator*other.denomenator
      common = gcd(new_num,new_den)
      return Fraction(new_num//common,new_den//common)
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


