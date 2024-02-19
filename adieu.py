import inflect
p = inflect.engine()
text=[]

while True:
    try:
        message=input("Name: ")
        text.append(message)
    except EOFError:

        print()
        break


output= p.join(text)
print("Adieu, adieu, to " + output)









