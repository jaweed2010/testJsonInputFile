import json

# Sample data
data = [
    {
        "ear": "BW_StoreTrans",
        "folder": "Sterling",
        "applications": ["BW_StoreTrans-UK", "BW_StoreTrans-US"]
    },
    {
        "ear": "BW_Adapter",
        "folder": "Sterling",
        "applications": ["BW_Adapter-UK", "BW_Adapter-US"]
    },
{
        "ear": "OrderSubmit",
        "folder": "Sterling",
        "applications": ["OrderSubmit"]
    }
]

# Define the filename to save the JSON data
filename = 'output.json'

# Write the data to a JSON file
with open(filename, 'w') as file:
    json.dump(data, file)

print(f"JSON data has been written to {filename}.")
