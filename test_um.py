from um import count

def main():
    test_um_word()


def test_um_word():

    assert count("um...") == 1
    assert count("um")==1
    assert count("Um, hello everyone") == 1
    assert count("hello um, world") == 1
    assert count("um, hi, um, world") == 2
    assert count("yummy") == 0
    assert count("Um, thanks for the album.")==1
    assert count("Um, thanks, um...") == 2
    assert count("um?")

if __name__ == "__main__":
    main()




