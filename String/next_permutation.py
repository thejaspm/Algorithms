def next_lexographical_permutation(number: int) -> str:
    """
    prints the next lexographical permutation successor, if no such successor exists print the input it self
    :param number:
    :return:
    """

    n = [x for x in str(number)]
    j = len(n) - 1

    # find the non-decreasing sequence from the unit place
    while n[j] <= n[j - 1] and j > 0:
        j -= 1

    # completely sorted in decreasing
    if j == 0:
        return "".join(n)

    # non decreasing just in the units place
    if j == len(n) - 1:
        n[j], n[j - 1] = n[j - 1], n[j]
        return "".join(n)

    # set pivot element to swap with, the one before the end of non-decreasing seq
    pivot, next_n, swap_n = j - 1, n[j], j

    # find the min value element in the non-decreasing seq which is greater than the pivot element
    for i in range(j + 1, len(n)):
        if n[pivot] < n[i] < next_n:
            next_n, swap_n = n[i], i

    # swap the pivot element and the next greater element
    n[pivot], n[swap_n] = n[swap_n], n[pivot]

    # sort the length of the non-decreasing seq from the units place
    y = [x for x in n[pivot + 1:]]
    y.sort()

    # append results
    return "".join(n[:pivot + 1] + y)


def test_nlp():
    assert next_lexographical_permutation(123) == "132"
    assert next_lexographical_permutation(121) == "211"
    assert next_lexographical_permutation(17427865) == "17428567"
    assert next_lexographical_permutation(11111) == "11111"
    assert next_lexographical_permutation(11199) == "11919"
    assert next_lexographical_permutation(321) == "321"



test_nlp()
