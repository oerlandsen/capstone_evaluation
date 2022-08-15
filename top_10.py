import json


data = [json.loads(line) for line in open(
    'farmers-protest-tweets-2021-03-5.json', 'r')]


def top_retweeted(data):
    data_sorted = sorted(data, key=lambda x: x['retweetCount'], reverse=True)
    for i in range(10):
        print(
            f'{data_sorted[i]["content"]}   {data_sorted[i]["retweetCount"]}')


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


def main(data):

    conected = True
    while conected:
        print("1 for top 10 retweeted")
        print("2 for top 10 users")
        print("3 for top 10 dates")
        print("4 for top 10 hashtags")
        print("5 to exit")
        option = int(input('option: '))
        if option == 1:
            top_retweeted(data)
        elif option == 2:
            top_users(data)
        elif option == 3:
            top_date(data)
        elif option == 4:
            top_hashtags(data)
        elif option == 5:
            conected = False


main(data)
