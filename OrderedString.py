def order(sentence):
    str_list = sentence.split()
    new_str = []
    
    def find_number(word):
        for char in word:
            if char.isdigit():
                return int(char)
        return -1
    
    new_str = sorted(str_list, key=find_number)
    return ' '.join(new_str)


assert order("is2 Thi1s T4est 3a") == "Thi1s is2 3a T4est"
assert order("4of Fo1r pe6ople g3ood th5e the2") == "Fo1r the2 g3ood 4of th5e pe6ople"
assert order("3 2 1") == "1 2 3"
assert order("1 2 3") == "1 2 3"
assert order("6Are 5You 4Ready 3For 2The 1Challenge") == "1Challenge 2The 3For 4Ready 5You 6Are"