# Matrix Chain Multiplication
import sys
import pytest
sys.setrecursionlimit(1500)

def matric_chain_multiplication(a: list, parentesis_begin: int, pranthesis_end: int) -> int:
    if parentesis_begin == pranthesis_end:
        return 0
    # matricses A,B,C,D
    # evaluate (A)(BCD) , (AB)(BC) , (ABC)(D) for minimum multiplications needed
    # (A)(BCD) further breaks down to (B)(CD) , (BC) D and gives the minimum way to muliply this to (BCD)
    _min = sys.maxsize
    for pantesis_divider in range(parentesis_begin, pranthesis_end):
        count = matric_chain_multiplication(a, parentesis_begin, pantesis_divider) + \
            matric_chain_multiplication(
                a, pantesis_divider+1, pranthesis_end) + a[parentesis_begin-1] * a[pantesis_divider] * a[pranthesis_end]
        if count < _min:
            _min = count
    return _min


def test_MCM():
    assert matric_chain_multiplication([1,2,3,4,5], 1, 4) == 38
    assert matric_chain_multiplication([10,20,30], 1, 2) == 6000
    assert matric_chain_multiplication([10, 20, 30, 40, 30], 1, 4) == 30000
    assert matric_chain_multiplication([40, 20, 30, 10, 30], 1, 4) == 26000

test_MCM()
