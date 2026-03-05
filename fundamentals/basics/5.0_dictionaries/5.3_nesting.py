# a list of dicitonaries
alien_0 = {"color": "green", "point": 5}
alien_1 = {"color": "yellow", "point": 10}
alien_2 = {"color": "blue", "point": 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# make 30 aliens
aliens = []
for alien_number in range(30):
    new_alien = {"color": "green", "point": 5, "speed": "slow"}
    aliens.append(new_alien)
#show the first 5 aliens
for alien in aliens[:5]:
    print(alien)

for alien in aliens[0:3]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["speed"] = "medium"
        alien["points"] = 10
    elif alien["color"] == "yellow":
        alien["color"] = "red"
        alien["speed"] = "fast"
        alien["points"] = 15
for alien in aliens[:5]:
    print(alien)

# a list in dictionary
favorite_languages = {
    "jade":[ "python", "rust"],
    "sarah": "c",
    "edward": ["rust", "go"],
    "phil": ["python", "haskel"]
}
for name, languages in favorite_languages.items():
    print(f"{name.title()} favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")

# a dictionary in a dictionary
users = {
    "aeinstein": {
        "first": "albert",
        "last": "einstein",
        "location": "princeton",
    },
    "mcurie": {
        "first": "marie",
        "last": "curie",
        "location": "paris",
    }
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info["first"]} {user_info["last"]}"
    location = user_info["location"]

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")