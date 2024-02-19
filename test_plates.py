from plates import is_valid



def main():
    test_plates


def test_plates():
    assert is_valid("CS50")== True
    assert is_valid("AAA02A")== False
    assert is_valid("C")== False
    assert is_valid("22")== False
    assert is_valid("AAA22A")== False
    assert is_valid("AAA022")== False
    assert is_valid("CS.50") == False



if __name__ == "__main__":
    main()




