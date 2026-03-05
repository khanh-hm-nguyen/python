favorite_languages = {
    "jade": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python"
}

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}")

# looping through all keys in dictionary
for name in favorite_languages.keys():
    print(name.title())

if "erin" not in favorite_languages.keys():
    print("Erin, please take our poll")

# looping through all keys in dictionary in particular order
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

# looping through all values in dictionary
print("the following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# set to pull out unique item
for language in set(favorite_languages.values()):
    print(language.title())