from functools import reduce
import math
import string
import random

def check(num=1):
  fib = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]], range(n-2), [0, 1])
  if len(list(filter(lambda y: y==num,fib(10000)))) >= 1:
    return True
  else:
    return False

def add_odd_even(l1,l2):
  return list(map(lambda x,y:x+y, list(filter(lambda n:n%2 == 0, l1)), list(filter(lambda n:n%2 != 0, l2))))

def anti_vowel(vowels, text):
    return ''.join([c for c in text if c not in vowels])

def relu_python(list1):
  return list(map(lambda x:max(x,0), list1))

def basic_sigmoid(list1):
    return list(map(lambda x:1/(1+math.exp(-x)), list1))

def shift_char(shift, text):
  return list(map(lambda index:string.ascii_letters[index % len(string.ascii_letters)], [ord(letter) - ord('a') + shift for letter in text]))

def check_swear_words(text):
  f = open('lists.txt', 'r+')
  lines = [line for line in f.readlines()]
  f.close()
  if list(filter(lambda y: y==text, list(map(lambda s: s.strip(), lines)))):
    return True
  else:
    return False

def add_even_reduce(numbers):
  return reduce(lambda x, y: x + y if not y % 2 else x, numbers, 0)

# def biggest_char(text):
#   print([ord(letter) - ord('a') for letter in text])
#   return reduce(lambda index:string.ascii_letters[index % len(string.ascii_letters)] if x > y else 0)

def biggest_char(test:str)->str:
    '''Outputs the biggest char in the string provided'''
    return reduce(lambda x,y: max(x,y), test)

def add_third_num(numbers):
  return reduce(lambda x, y: x+y, numbers[3::3])

def rand_rto():
  RTO = ['KA'+str(random.randint(10, 99))+'JB'+str(random.randint(1000, 9999)) for _ in range(15)]
  return len(RTO)

def partial_1(state, static1):
  return [state+str(random.randint(10, 99))+'JB'+static1 for _ in range(15)]

def partial_rto(state):
  static1 = str(random.randint(1000, 9999))
  state_wise_len = partial_1(state, static1)
  return state_wise_len


