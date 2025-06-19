
def spin_words(sentence):
    str_list = sentence.split(" ")
    new_str = []
    
    for string in str_list:
        if len(string) >= 5:
            word = string[::-1]
        else:
            word = string
        new_str.append(word)
    
    return " ".join(new_str)

assert spin_words("Welcome") == "emocleW"
assert spin_words("This is a test") == "This is a test"
assert spin_words("This is another test") == "This is rehtona test"
assert spin_words("You are almost to the last test") == "You are tsomla to the last test"
assert spin_words("Just kidding there is still one more") == "Just gniddik ereht is llits one more"
assert spin_words("Hey fellow warriors") == "Hey wollef sroirraw"