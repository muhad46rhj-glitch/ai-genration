print("Hello I am AI Bot. What's your name? : ")

name = input()

print(f"Nice to meet you, {name}!")

print("How are you feeling today? (good/bad) : ")

mood = input().lower()

if mood == "good":
    print("I am glad to hear that!")
elif mood == "bad":
    print("I am sorry to hear that. Hope things get better soon")
else:
    print("I see. Sometimes it's hard to put feelings into words.")

print("What is your favorite color? : ")

color = input()

print(f"{color} is a nice color, {name}!")

print("What is your favorite food? : ")

food = input()

print(f"Wow! I like hearing about {food}!")

print("What do you like to do in your free time? : ")

hobby = input()

print(f"That sounds fun! I hope you enjoy {hobby}.")

print("What is your favorite animal? : ")

animal = input()

print(f"{animal} is a great choice!")

print("Do you like AI? (yes/no) : ")

ai = input().lower()

if ai == "yes":
    print("That's great! I am happy you like AI!")
elif ai == "no":
    print("That's okay! Maybe I can change your mind someday.")
else:
    print("Interesting! I understand.")

print(f"It was nice chatting with you {name}.")
print(f"I learned that you like {food}, your favorite color is {color},")
print(f"you enjoy {hobby}, and your favorite animal is {animal}.")
print("Goodbye! Have a great day!")