from numb3rs import validate


def main():
    test_ip_true()
    test_ip_false()


def test_ip_true():
    assert validate("123.123.123.123") == True
    assert validate("255.255.255.255") == True

def test_ip_false():
    assert validate("cat") == False
    assert validate("1.000.256.256") == False
    assert validate("1111.111.33333.44444") == False


if __name__ == "__main__":
    main()

