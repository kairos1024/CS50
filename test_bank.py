from bank import value

def main():
    test_bank()

def test_bank():
    assert value("hello cai") == 0
    assert value("HeLlo Cai") == 0
    assert value("hello") == 0
    assert value("Hi") == 20
    assert value("What's up") == 100

if __name__=="__main__":
    main()
