def main():
    answer_string=input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    answer_string=answer_string.strip("  ").lower()
    answer=answer_string


    match answer:
        case "42"|"forty two"|"forty-two":
            print("Yes")
        case _:
            print("No")

main()