#Ask user for an expression
x,y,z=input("Expression: ").split(" ")
#Calculate
x=float(x)
z=float(z)
if y== "+":
    answer=x + z
elif y== "-":
    answer=x - z
elif y== "*":
    answer=x*z
elif y=="/":
    answer=x / z
#Final output
print(answer)










