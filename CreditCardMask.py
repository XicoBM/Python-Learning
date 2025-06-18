
def maskify(cc):
    if len(cc) <= 4:
        return cc
    else:
        masked = "#" * len(cc[:-4])
        return masked + cc[-4:]
    
assert maskify("4556364607935616") == "############5616"
assert maskify("1") == "1"
assert maskify("11111") == "#1111"
assert maskify("") == ""
assert maskify("1234567890123456") == "############3456"
assert maskify("1234") == "1234"
assert maskify("12345678901234567890") == "################7890"