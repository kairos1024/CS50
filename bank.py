def main():



    def value(greeting):
        greeting_string=input("Greeting:")
        greeting_string=greeting_string.strip("  ")
        greeting=greeting_string

        match greeting:
            case "Hello" | "Hello, Newman"|"Hello there" :
                return("$0")
            case "How you doing?"| "Hi" | "Hey" |"How's it going":
                return("$20")
            case _:
                return("$100")

if __name__ == "__main__":
    main()
