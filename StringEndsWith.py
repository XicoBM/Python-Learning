def solution(text, ending):
    text_size:int = len(text)
    end_size:int = len(ending)
    var: str = ""
    starting_point: int = text_size - end_size

    for i in range(starting_point, text_size):
        var += text[i]
    
    return ending == var

assert solution("abcde", "cde") == True
assert solution("abcde", "abc") == False
assert solution("abcde", "de") == True
assert solution("abcde", "e") == True
assert solution("abcde", "f") == False
assert solution("abcde", "") == True
