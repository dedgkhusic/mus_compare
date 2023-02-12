import vk_api
from vk_api.audio import VkAudio
import time


def main():
    t_start = time.time()  # начало работы
    user_id1 = '550033465'  # user1 я
    user_id2 = '152062114'  # user2 алина

    # авторизация
    login, password = '+79891331486', 'AFsdqw12'
    vk_session = vk_api.VkApi(login, password)
    vk_session.auth()
    print('authorization')

    # подгрузка всех записей в json
    vkaudio = VkAudio(vk_session)
    tracks1 = vkaudio.get(user_id1)
    print('download user1')
    tracks2 = vkaudio.get(user_id2)
    print('download user2')
    print(tracks1)
    print(tracks2)
    print()

    user1 = []
    user2 = []
    for el in tracks1:
        user1.append(el['id'])

    for el in tracks2:
        user2.append(el['id'])

    per = []
    for i in user1:
        if i in user2:
            per.append(i)

    print()
    print(len(per), "tracks", end='\n')
    print(f"{round((len(per) / len(user1)) * 100, 2)}% сопадений user1 c user2")
    print(f"{round((len(per) / len(user2)) * 100, 2)}% сопадений user2 c user1", end='\n\n')
    # print(per)

    print()
    for el in tracks1:
        if el['id'] in per:
            print(f"artist: {el['artist']} -- title: {el['title']} -- id: {el['id']}")

    print()
    print()

    for el in tracks2:
        if el['id'] in per:
            print(f"artist: {el['artist']} -- title: {el['title']} -- id: {el['id']}")

    t_end = time.time()
    print()
    print('Execution time:', int((t_end - t_start) / 60), 'min', int(t_end - t_start) % 60, 'sec')


if __name__ == '__main__':
    main()
