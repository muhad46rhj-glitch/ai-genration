import re, random
from colorama import Fore, init

init(autoreset=True)

destinations = {
    "beaches": ["Bali" , "Maldives", "Phuket"],
    "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],
    "cities": ["Tokyo", "Paris", "New York"]
}

jokes = [
    "Why don't programmers like nature?Too many bugs!",
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why do travelers always feel warm? Because of all their hot spots!"
    ]

    def normalize_input(text):
        return re.sub(r"\s+","", text.stip().lower())

    def recommend():
        print(Force.CYAN + "TravelBot: Beanches, mountains, or cities?")
        preference = input(Force.YELLOW + "You: ")
        prefernces = normalize_input(preference)

