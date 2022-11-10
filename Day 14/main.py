from art import logo, vs
from game_data import data
from random import randrange
from os import system

current_score = 0
game_playing = True


def clear():
    system("clear")


def generate_random_persons():
    global random_person_a, random_person_b, name_person_a, name_person_b, followers_person_a, followers_person_b, description_person_b, description_person_a, country_person_a, country_person_b
    random_person_a = randrange(len(data))
    name_person_a = data[random_person_a]["name"]
    followers_person_a = data[random_person_a]["follower_count"]
    description_person_a = data[random_person_a]["description"]
    country_person_a = data[random_person_a]["country"]
    random_person_b = randrange(len(data))
    while random_person_b == random_person_a:
        random_person_b = randrange(len(data))
    name_person_b = data[random_person_b]["name"]
    followers_person_b = data[random_person_b]["follower_count"]
    description_person_b = data[random_person_b]["description"]
    country_person_b = data[random_person_b]["country"]


def switch(person_a, person_b):
    global random_person_a, random_person_b, name_person_a, name_person_b, followers_person_a, followers_person_b, description_person_b, description_person_a, country_person_a, country_person_b
    person_a = person_b
    person_b = randrange(len(data))
    while person_b == person_a:
        person_b = randrange(len(data))
    random_person_a = person_a
    random_person_b = person_b
    name_person_a = data[person_a]["name"]
    followers_person_a = data[person_a]["follower_count"]
    description_person_a = data[person_a]["description"]
    country_person_a = data[person_a]["country"]
    name_person_b = data[person_b]["name"]
    followers_person_b = data[person_b]["follower_count"]
    description_person_b = data[person_b]["description"]
    country_person_b = data[person_b]["country"]


print(logo)
generate_random_persons()

while game_playing:
    clear()
    print(logo)
    if current_score > 0:
        print(f"You're right! Current score: {current_score}")
    print(
        f"Compare A: {name_person_a}, a {description_person_a}, from {country_person_a}. {followers_person_a}"
    )
    print(vs)
    print(
        f"Against B: {name_person_b}, a {description_person_b}, from {country_person_b}. {followers_person_b}"
    )
    # print(random_person_a, random_person_b)
    more_followers = input("Who has more followers? Type 'A' or 'B': ")
    # print(more_followers)

    if (more_followers == "A" and followers_person_a > followers_person_b) or (
        more_followers == "B" and followers_person_b > followers_person_a
    ):
        current_score += 1
        # print(f"You're right! Current score: {current_score}")
        switch(random_person_a, random_person_b)
        # random_person_a = random_person_b
        # random_person_b = randrange(len(data))
    else:
        print(f"Sorry, that's wrong. Final score: {current_score}")
        game_playing = False

    # print(random_person_a, random_person_b)
    # print(name_person_a, name_person_b)
