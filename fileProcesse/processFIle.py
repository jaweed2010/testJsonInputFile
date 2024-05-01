import json

# Open the file containing the JSON data
with open('output.json', 'r') as file:
    # Load the JSON data from the file into a variable
    input_file = json.load(file)

# Now you can work with the 'data' variable, which contains the JSON data
print(input_file)

# print list of all applications along with their folder names
for line in input_file:
    for app in line["applications"]:
        print(f"{line["folder"]}/{app}")

# print list of only 1 application along with its folder names
for line in input_file:
    print(f"{line["folder"]}/{line["applications"][0]}")