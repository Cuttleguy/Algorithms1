def gcd(m, n):
    while m % n != 0:
        m, n = n, m % n
    return n
# Python Program to find the L.C.M. of two input number

def lcm(x, y):

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm