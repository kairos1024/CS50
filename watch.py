import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
     match =re.search('.+src="https?://(?:www.)?youtube.com/embed/(.+?)"', s)
     if match:
         l = "https://youtu.be/"+ match.group(1)
         return l
     else:
        return None




if __name__ == "__main__":
    main()
