
import pytest

#zadanie1_1.py (Функция для поиска значения в сложном объекте (РЕКУРСИЯ))---------------------------------

from zadanie1_1 import find1, find2


test_task = [1, 2, [3, 4, [5, [6, []]]]]

def test_for_find11():
    assert find1(test_task, 1) == 0
    assert find1(test_task, 2) == 1
    assert find1(test_task, 3) == 2

    assert find1(test_task, 100) is None
    assert find1(test_task, 'hello') is None

def test_for_find21():
    assert find1(test_task, 1) == 0
    assert find1(test_task, 2) == 1
    assert find1(test_task, 3) == 2

    assert find1(test_task, 100) is None
    assert find1(test_task, 'hello') is None
    
def test_foranswer1():
    assert find1(test_task, 4) == find2(test_task, 4)
    assert find1(test_task, 'spam') == find2(test_task, 'spam')


#zadanie1_2.py (Функция для поиска значения в сложном объекте (БЕЗ РЕКУРСИЯ))---------------------------------

from zadanie1_2 import find3, find4

def test_for_find12():
    assert find3(test_task, 1) == 0
    assert find3(test_task, 2) == 1
    assert find3(test_task, 3) == 2

    assert find3(test_task, 100) is None
    assert find3(test_task, 'hello') is None

def test_for_find22():
    assert find4(test_task, 1) == 0
    assert find4(test_task, 2) == 1
    assert find4(test_task, 3) == 2

    assert find4(test_task, 100) is None
    assert find4(test_task, 'hello') is None
    
def test_foranswer2():
    assert find3(test_task, 4) == find2(test_task, 4)
    assert find4(test_task, 'spam') == find2(test_task, 'spam')

#zadanie2_1.py ----------------------------------------------------------------------------------------------

from zadanie2_1 import calc1, calc2

def test_foranswer3():
    assert calc1(3, 2, 4) == calc2(3, 2, 4)
    
def test_calc1():
    assert calc1(5, 10, 1) == (5, 10)
    assert calc1(1, 2, 2) == (5, 10)
    assert calc1(1, 2, 3) == (25, 210)

def test_calc2():
    assert calc2(5, 10, 1) == (5, 10)
    assert calc2(1, 2, 2) == (5, 10)
    assert calc2(1, 2, 3) == (25, 210)
    
    
    
 #zadanie2_2.py ---------------------------
    
from zadanie2_1 import calc3, calc4


def test_foranswer4():
    assert calc3(3, 2, 4) == calc4(3, 2, 4)

def test_calc3():
    assert calc3(5, 10, 1) == (5, 10)
    assert calc3(1, 2, 2) == (5, 10)
    assert calc3(1, 2, 3) == (25, 210)

def test_calc4():
    assert calc4(5, 10, 1) == (5, 10)
    assert calc4(1, 2, 2) == (5, 10)
    assert calc4(1, 2, 3) == (25, 210)