temperature=float(input("input the current temperature:"))
if temperature>=30:
    print("It's a hot day. Stay hydrated!")
elif 20 <= temperature <= 29:
    print("It's a warm day. Enjoy the weather!")

elif 10 <= temperature <= 19:
    print("It's a cool day. Wear a jacket!")
elif temperature<=10:
    print("It's a cold day. Stay warm!")
else:
    print('y is 30 or more')
