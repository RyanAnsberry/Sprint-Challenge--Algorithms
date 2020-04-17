'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # Base case: If word is less than 2 letters, it must be 0 "th"
    if len(word) < 2:
        return 0
    # Check if first two letters of passed in word are "th" if so, return 1 and recurse
    elif word[0] == "t" and word[1] == "h":
        return 1 + count_th(word[1:])
    # If the first 2 letters are not 'th' recurse again
    else:
        return count_th(word[1:])

