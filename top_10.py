import json


data = [json.loads(line) for line in open(
    'farmers-protest-tweets-2021-03-5.json', 'r')]


def top_retweeted(data):
    data_sorted = sorted(data, key=lambda x: x['retweetCount'], reverse=True)
    for i in range(len(data_sorted)):
        if i < 10:
            print(data_sorted[i]['retweetCount'])


def top_users(data):
    users = {}
    for i in range(len(data)):
        if users.get(data[i]['user']['username']):
            users[f'{data[i]["user"]["username"]}'] += 1
        else:
            users.update({data[i]['user']['username']: 1})
    users_sorted = sorted(users.items(), key=lambda x: x[1],  reverse=True)
    for i in range(10):
        print(users_sorted[i])


def top_date(data):
    data_sorted = sorted(data, key=lambda x: x['date'], reverse=True)
    dates = {}
    for i in range(len(data_sorted)):
        if dates.get(data_sorted[i]['date'][0:10]):
            dates[f'{data_sorted[i]["date"][0:10]}'] += 1
        else:
            dates.update({data_sorted[i]['date'][0:10]: 1})
    dates_sorted = sorted(dates.items(), key=lambda x: x[1],  reverse=True)
    for i in range(10):
        print(dates_sorted[i])


def top_hashtags(data):
    data_sorted = sorted(data, key=lambda x: x['retweetCount'], reverse=True)
    hashtags = {}
    for i in range(len(data_sorted)):
        if data_sorted[i]['content'].count('#') >= 2:
            data_sorted[i]['content'] = data_sorted[i]['content'].replace(
                '#FarmersProtest', ' ')
            data_split = data_sorted[i]['content'].replace(
                '\n', ' ').split(' ')

            for word in data_split:
                if '#' in word:
                    if hashtags.get(word):
                        hashtags[f'{word}'] += 1
                    else:
                        hashtags.update({word: 1})

    hashtags = sorted(hashtags.items(), key=lambda x: x[1],  reverse=True)
    for i in range(10):
        print(hashtags[i])


top_users(data)
