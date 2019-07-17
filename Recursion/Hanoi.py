import pytest


def hanoi(disks: int, moves: list, source='a', intermediate='b', destination='c'):
    if disks == 1:
        moves.append(("{} -> {}".format(source, destination)))
        return
    hanoi(disks-1, moves, source, destination, intermediate)
    moves.append(("{} -> {}".format(source, destination)))
    hanoi(disks-1, moves, intermediate, source, destination)


def test_hanoi_1():
    moves = list()
    expected_moves = ['a -> c', 'a -> b', 'c -> b',
                      'a -> c', 'b -> a', 'b -> c', 'a -> c']
    hanoi(3, moves)
    assert moves == expected_moves


def test_hanoi_2():
    moves = list()
    hanoi(5, moves)
    expected_moves = ['a -> c', 'a -> b', 'c -> b', 'a -> c', 'b -> a', 'b -> c', 'a -> c',
                      'a -> b', 'c -> b', 'c -> a', 'b -> a', 'c -> b', 'a -> c', 'a -> b',
                      'c -> b', 'a -> c', 'b -> a', 'b -> c', 'a -> c', 'b -> a', 'c -> b',
                      'c -> a', 'b -> a', 'b -> c', 'a -> c', 'a -> b', 'c -> b', 'a -> c',
                      'b -> a', 'b -> c', 'a -> c']
    assert moves == expected_moves


def test_hanoi_3():
    moves = list()
    hanoi(8, moves)

test_hanoi_1()
test_hanoi_2()
