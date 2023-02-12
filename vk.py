import vk_api
from vk_api.audio import VkAudio
import time


def main():
    t_start = time.time()  # начало работы
    user_id1 = '152062114'  # user1 мама
    user_id2 = '550033465'  # user2 сёма

    # авторизация
    login, password = '+79891331486', 'AFsdqw12'
    vk_session = vk_api.VkApi(login, password)
    vk_session.auth()
    print('вход')

    # подгрузка всех записей в json
    vkaudio = VkAudio(vk_session)
    tracks1 = vkaudio.get(user_id1)
    print('загруженно user1')
    tracks2 = vkaudio.get(user_id2)
    print('загруженно user2')
    # print(tracks)

    user1 = []
    user2 = []
    for el in tracks1:
        user1.append(el['id'])

    for el in tracks2:
        user2.append(el['id'])

    per = []
    # print(user1)
    # print(user2)

    for i in user1:
        if i in user2:
            per.append(i)

    print()
    print(len(per), "совпадений", end='\n')
    print(f"{round((len(per) / len(user1)) * 100, 2)}% сопадений user1 c user2")
    print(f"{round((len(per) / len(user2)) * 100, 2)}% сопадений user2 c user1", end='\n\n')
    # print(per)

    print()
    for el in tracks1:
        if el['id'] in per:
            print(f"artist: {el['artist']}  title: {el['title']}")

    t_end = time.time()
    print()
    print('Время выполнения:', int((t_end - t_start) / 60), 'минут', int(t_end - t_start) % 60, 'секунд')


if __name__ == '__main__':
    main()
