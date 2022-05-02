import csv
import datetime
import requests
import matplotlib.pyplot as plt


def parse_time(text):
    return datetime.datetime.strptime(text, "%Y-%m-%d %H:%M:%S.%f")


def get_messages():
    url = f"https://raw.githubusercontent.com/true-grue/kispython/main/data/messages.csv"
    response = requests.get(url).text.splitlines()
    print(response)
    return list(csv.reader(response))


messages = get_messages()

hours_activity = dict([(i, 0) for i in range(24)])
for message in messages:
    hours_activity[parse_time(message[4]).hour] += 1
plt.bar(hours_activity.keys(), hours_activity.values())
plt.show()

days_activity = dict([(i, 0) for i in range(7)])
for message in messages:
    days_activity[parse_time(message[4]).weekday()] += 1
plt.bar(days_activity.keys(), days_activity.values())
plt.show()

groups_activity = dict([(message[3][1:2] + message[3][5:7], 0) for message in messages])
for message in messages:
    groups_activity[message[3][1:2] + message[3][5:7]] += 1
plt.bar(groups_activity.keys(), groups_activity.values())
plt.show()

groups_efficiency = dict([(message[3][1:2] + message[3][5:7], 0) for message in messages])
for message in messages:
    groups_efficiency[message[3][1:2] + message[3][5:7]] += (int(message[1]))
plt.bar(groups_efficiency.keys(), groups_efficiency.values())
plt.show()

tasks_difficulty = dict([(message[2], 0) for message in messages])
for message in messages:
    tasks_difficulty[message[2]] += int(message[1])
plt.bar(tasks_difficulty.keys(), tasks_difficulty.values())
plt.show()


