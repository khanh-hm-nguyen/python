string = "this is a string, because it is inside the quote or double quote."

# changing case in a string with methods
name = "ada lovelace"
print(name.title())
name = "Ada Lovelace"
print(name.upper())
print(name.lower())

# using variables in string
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(f"Hello {full_name.title()}")

# adding whitespace to string with tabs or newlines
print("python")
print("\tpython")
print("add\nnewline\nin\na\nstring")

#stripping whitespace
language = " python "
print(language)
print(language.strip())
print(language.lstrip())
print(language.rstrip())

#removing prefixes
url = "https://urls.com"
print(url.removeprefix("https://"))

