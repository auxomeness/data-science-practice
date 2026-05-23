# Import package
import requests

# Assign URL to variable: url
url = "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&exintro=&titles=pizza"


# Always include a descriptive User-Agent (Wikipedia requires this)
headers = {
    "User-Agent": "Checking out the Wikipedia API"
}

# Package the request, send the request and catch the response: r
r = requests.get(url, headers=headers)

# Decode the JSON data into a dictionary: json_data
json_data = r.json()

# Print the Wikipedia page extract
pizza_extract = json_data['query']['pages']['24768']['extract']
print(pizza_extract)
