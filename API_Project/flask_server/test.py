import json

with open("가천대_naver_news.json", "r") as json_file:
    data = json.load(json_file)

# news_dict = json.loads(data)

print(data[0:11])

data_sliced = data[0:11]

# for element in data_sliced:
#     news_dict = json.loads(str(element)

# print(news_dict)

# news_dict_list = []
