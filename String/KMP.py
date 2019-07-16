import pytest
def substring_search(text:str, pattern:str) -> int:

    prefix_pos = compute_prefix_positions(pattern)
    i, j = 0,0
    # stop iteration if we reach either of end of text or end of pattern
    while i < len(text) and j< len(pattern) :
        if text[i] == pattern[j]:
            j = j+1
        # didnt match, if index of pattern(j) is not 0 then update index(j) of pattern to the last found prefix 
        elif j != 0:
                j=prefix_pos[j-1]
        i = i+1
    # if pattern index was equal to pattern length viola!! we found the pattern
    return i-j if j == len(pattern) else -1

def compute_prefix_positions(pattern: str) -> list:
    j, i , prefix_pos = 0, 1, [''] * len(pattern)
    prefix_pos[j] = 0
    while i < len(pattern):
        #if we find a matching prefix keep moving ahead and continue 
        if pattern[j] == pattern[i]:
            prefix_pos[i] = j+1
            j, i = j+1, i+1
        #we didnt find the matching prefix position, 2 possibilities and 1 exit condition
        else:
            prefix_pos[i] = 0
            #back to the first char in the pattern after walking to the last character
            # we have seen it all , exit 
            if j==0 and i == len(pattern)-1:
                break
            # we haven't walked to the last character yet, increment i as no match
            if i < len(pattern)-1:
                i = i+1
            
            # no match and J was in b/w the pattern , go back to the last knwn prefix
            if j > 0:
                j = prefix_pos[j-1]
    return prefix_pos

def test_compute_prefix_positions():
    pass
    assert [0,1,2,3,4] == compute_prefix_positions('ttttt')
    assert [0, 0, 0, 1, 2, 0] == compute_prefix_positions('abcaby')
    assert [0, 0, 0, 0, 1, 2, 3, 1] == compute_prefix_positions('abcdabca')
    assert [0, 1, 0, 1, 2, 3, 4, 5, 2] == compute_prefix_positions('aabaabaaa')
    assert [0, 0, 0, 0, 0, 0, 0] == compute_prefix_positions('abcrcst')

def test_sub_string_search():
    assert 11 == substring_search("abcdpqrstuvabcabyst", 'abcaby')
    assert -1 == substring_search("abcdpqrstuvabcabst", 'abcaby')
    assert 14 == substring_search("abcdaabaabaardaabaabaaabaabaaa", 'aabaabaaa')

test_compute_prefix_positions()
test_sub_string_search()
