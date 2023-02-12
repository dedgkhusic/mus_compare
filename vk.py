import vk_api
from vk_api.audio import VkAudio
import time


def main():
    t_start = time.time()  # начало работы
    user_id1 = '396334047'  # user1
    user_id2 = '502662969'  # user2

    # авторизация
    login, password = '+79888384971', 'aRV20050505'
    vk_session = vk_api.VkApi(login, password)
    vk_session.auth()
    print('authorization')

    # подгрузка всех записей в json
    vkaudio = VkAudio(vk_session)
    tracks1 = vkaudio.get(user_id1)
    print('download user1')
    tracks2 = vkaudio.get(user_id2)
    print('download user2')
    # print(tracks1)
    # print(tracks2)
    print()

    user1 = []
    user2 = []
    for el in tracks1:
        user1.append([el['artist'], el['title'], el['duration']])

    for el in tracks2:
        user2.append([el['artist'], el['title'], el['duration']])

    per = []
    for i in user1:
        if i in user2 and i not in per:
            per.append(i)

    print()
    print(len(per), "tracks", end='\n')
    print(f"{round((len(per) / len(user1)) * 100, 2)}% сопадений user1 c user2")
    print(f"{round((len(per) / len(user2)) * 100, 2)}% сопадений user2 c user1", end='\n\n')
    # print(per)

    for i in per:
        print(i[1], '----', i[0], i[2])

    print()

    t_end = time.time()
    print()
    print('Execution time:', int((t_end - t_start) / 60), 'min', int(t_end - t_start) % 60, 'sec')


if __name__ == '__main__':
    main()
