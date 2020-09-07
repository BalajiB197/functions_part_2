import os
import session7
from session7 import *
import pytest

vowels = {'i','o','a','u','e'}

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_fib_num():
    assert check(5) == True, "5 is a Fibonacci number!"

def test_fib_num2():
    assert check(4) != True, "4 is not a Fibonacci number!"

def test_add_odd_even():
    l1 = [1,2,3,4,5] # Even
    l2 = [3,5]       # odd
    assert add_odd_even(l1,l2) == [5,9], "Add even num and odd num"

def test_add_odd_even2():
    l1 = [1,2,3,4,5] # Even
    l2 = [1,3,5,7,9] # odd
    assert add_odd_even(l1,l2) == [3,7], "Add even num and odd num"

def test_anti_vowel():
    assert anti_vowel(vowels, 'balaji') == 'blj', "discard vowel chars"

def test_anti_vowel2():
    assert anti_vowel(vowels, 'aeiou') == '', "discard vowel chars"

def test_relu_python():
    list1 = [1,2,-1, -0.22, -0.5, -100]
    assert relu_python(list1) == [1,2,0,0,0,0], "change neg to zero"

def test_relu_python2():
    list1 = [1,2,1,3,45,67]
    assert relu_python(list1) == [1,2,1,3,45,67], "change neg to zero"

def test_basic_sigmoid():
    list1 = [1,2,-1, -0.22, -0.5, -10]
    assert basic_sigmoid(list1) == [0.7310585786300049, 0.8807970779778823, 
    0.2689414213699951, 0.4452207648927852, 0.3775406687981454, 4.5397868702434395e-05], "sigmoid in python"

def test_shift_char():
    shift = 4
    text = 'ba'
    assert shift_char(shift, text) == ['f', 'e'], "shift 4 characters in ascii order"

def test_shift_char2():
    shift = 5
    text = 'xy'
    assert shift_char(shift, text) == ['C', 'D'], "shift 4 characters in ascii order"

def test_check_swear_words():
    text = 'balaji'
    assert check_swear_words(text) == False, "Does'nt balaji exists"

def test_check_swear_words2():
    text1 = 'willy'
    check_swear_words(text1) == True, "Contains willy word"

def test_add_even_reduce():
    numbers = [1,2,3,4]
    assert add_even_reduce(numbers) == 6, "using reduce method to sum even num"

def test_add_even_reduce2():
    numbers = [2,4,6,8,10]
    assert add_even_reduce(numbers) == 30, "using reduce method to sum even num"

def test_rand_rto():
    assert rand_rto() == 15, "generate 15 random vehicle registration num"

def test_partial_rto():
    state = 'DL'
    partial_rto(state) == 15, "generate 15 state wise random vehicle registration num"

