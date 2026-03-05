# accessing values in a dictionary
alien_0 = {"color": "green"}
print(alien_0['color'])
alien_0 = {"color": "green", "points": 5}
new_points = alien_0['points']
print(f"you just earned {new_points} points!")

# adding new key-value pairs
alien_0['x_position'] = 0
alien_0['y_poistion'] = 25
print(alien_0)

# starting with an empty dictionary
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

#modifying values in a dictionary
alien_0["color"] = "yellow"
print(f"the alien is now {alien_0["color"]}")

alien_0 = {"x_position": 0, "y_position": 25, "speed": "medium"}
print(f"alien original position: {alien_0['x_position']}")

# move the alien to the right
# determine how far to move the alien based on its current speed
if alien_0["speed"] == "slow":
    x_increment = 1
elif alien_0["speed"] == "medium":
    x_increment = 2
else:
    x_increment = 3

alien_0["x_position"] = alien_0["x_position"] + x_increment
print(f"new position: {alien_0["x_position"]}")

# removing key-value pairs
alien_0 = {"color": "green", "points": 5}
del alien_0["points"]
print(alien_0)

# a dictionary of similar objects
favorite_languages = {
    "jade": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python"
}
print(f"Sharah's favorite language is {favorite_languages["sarah"].title()}")

# using get() to access values
alien_0 = {"color": "green", "speed": "low"}
point_value = alien_0.get("points", "No point value assignment")
print(point_value)