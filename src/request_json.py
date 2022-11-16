import requests

url = 'https://cnodejs.org/api/v1/topics'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url,headers=headers)

response_dict = r.json()

print(response_dict.keys())
print(response_dict['success'])
print(f"success: {response_dict['success']}")
print(f"number: {len(response_dict['data'])}")

topics = response_dict['data']

for topic in topics:
	print(f"{topics.index(topic) + 1}: {topic['title']}")