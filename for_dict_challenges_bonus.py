"""
Пожалуйста, приступайте к этой задаче после того, как вы сделали и получили ревью ко всем остальным задачам
в этом репозитории. Она значительно сложнее.


Есть набор сообщений из чата в следующем формате:

```
messages = [
    {
        "id": "efadb781-9b04-4aad-9afe-e79faef8cffb",
        "sent_at": datetime.datetime(2022, 10, 11, 23, 11, 11, 721),
        "sent_by": 46,  # id пользователя-отправителя
        "reply_for": "7b22ae19-6c58-443e-b138-e22784878581",  # id сообщение, на которое это сообщение является ответом (может быть None)
        "seen_by": [26, 91, 71], # идентификаторы пользователей, которые видели это сообщение
        "text": "А когда ревью будет?",
    }
]
```

Так же есть функция `generate_chat_history`, которая вернёт список из большого количества таких сообщений.
Установите библиотеку lorem, чтобы она работала.

Нужно:
1. Вывести айди пользователя, который написал больше всех сообщений.
2. Вывести айди пользователя, на сообщения которого больше всего отвечали.
3. Вывести айди пользователей, сообщения которых видело больше всего уникальных пользователей.
4. Определить, когда в чате больше всего сообщений: утром (до 12 часов), днём (12-18 часов) или вечером (после 18 часов).
5. Вывести идентификаторы сообщений, который стали началом для самых длинных тредов (цепочек ответов).

Весь код стоит разбить на логические части с помощью функций.
"""
import random
import uuid
import datetime

import lorem
from collections import Counter


def generate_chat_history():
    messages_amount = random.randint(200, 1000)
    users_ids = list(
        {random.randint(1, 10000) for _ in range(random.randint(5, 20))}
    )
    sent_at = datetime.datetime.now() - datetime.timedelta(days=100)
    messages = []
    for _ in range(messages_amount):
        sent_at += datetime.timedelta(minutes=random.randint(0, 240))
        messages.append({
            "id": uuid.uuid4(),
            "sent_at": sent_at,
            "sent_by": random.choice(users_ids),
            "reply_for": random.choice(
                [
                    None,
                    (
                        random.choice([m["id"] for m in messages])
                        if messages else None
                    ),
                ],
            ),
            "seen_by": random.sample(users_ids,
                                     random.randint(1, len(users_ids))),
            "text": lorem.sentence(),
        })
    return messages


def requrtion(message_id, reply_for_1, len_tread_1):
    if reply_for_1 != None:
        for message in history:
            if message["id"]==reply_for_1:
                len_tread_1 += 1
                len_tread_1 = requrtion(message["id"], message["reply_for"], len_tread_1)[0]
    return [len_tread_1, message_id]


def exercise1():
    ids = [mes['sent_by'] for mes in history]
    ctr = Counter(ids)
    print(f"Айди пользователя, который написал больше всех сообщений: {ctr.most_common(1)[0][0]}")


def exercise2():
    replys = [mes['reply_for'] for mes in history]
    user_list = []
    for message in history:
        for reply in replys:
            if reply != None and message["id"] == reply:
                user = message["sent_by"]
                user_list.append(user)
    ctr1 = Counter(user_list)
    print(f"Айди пользователя, на сообщения которого больше всего отвечали: {ctr1.most_common(1)[0][0]}")


def exercise3():
    seen_users = {}
    for message in history:
        if seen_users.get(message["sent_by"]) != None:
            seen_users[message["sent_by"]].union(message["seen_by"])
        else:
            seen_users.update({message["sent_by"]: message["seen_by"]})
            seen_users[message["sent_by"]] = set(seen_users[message["sent_by"]])
    seen_user_max = 0
    seen_user_max_id = []
    for seen_users_id in seen_users.values():
        if len(seen_users_id) >= seen_user_max:
            seen_user_max = len(seen_users_id)
    for user_id, seen_users_id in seen_users.items():
        if len(seen_users_id) == seen_user_max:
            seen_user_max_id.append(str(user_id))
    seen_user_max_id = ", ".join(seen_user_max_id)
    print(f"Айди пользователей, сообщения которых видело больше всего уникальных пользователей: {seen_user_max_id}")


def exercise4():
    time_am = 0
    time_pm = 0
    time_pm_2 = 0
    for message in history:
        if message['sent_at'].strftime('%H:%M') < "12:00":
            time_am += 1
        elif "12:00" <= message['sent_at'].strftime('%H:%M') < "18:00":
            time_pm += 1
        else:
            time_pm_2 += 1
    if time_am >= time_pm and time_am >= time_pm_2:
        print("В чате больше всего сообщений утром")
    elif time_pm >= time_am and time_pm >= time_pm_2:
        print("В чате больше всего сообщений днём")
    elif time_pm_2 >= time_am and time_pm_2 >= time_pm:
        print("В чате больше всего сообщений вечером")


def exercise5():
    len_tread_max = 0
    len_treads_max = []
    len_tread = [0,0]
    len_treads_max_id = []
    for message in history:
        if message["reply_for"] != None:
            len_tread = requrtion(message["id"],message["reply_for"], 1)
        if len_tread[0] >= len_tread_max:
            len_tread_max = len_tread[0]
            len_treads_max.append(len_tread) 
    for len_tread_new in len_treads_max:
        if len_tread_new[0] == len_tread_max and str(len_tread_new[1]) not in len_treads_max_id:
            len_treads_max_id.append(str(len_tread_new[1]))
    treads_max_id_messages = ", ".join(len_treads_max_id)
    print(f"Идентификаторы сообщений, которые стали началом для самых длинных тредов (цепочек ответов): {treads_max_id_messages}")


if __name__ == "__main__":
    history = generate_chat_history()
    exercise1()
    exercise2()
    exercise3()
    exercise4()
    exercise5()
