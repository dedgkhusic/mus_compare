import vk_api
from vk_api.audio import VkAudio
import time


def main():
    t_start = time.time()
    user_id1 = '396334047'  # я
    user_id2 = '550033465'  # алина

    login, password = '+79888384971', 'aRV20050505'
    vk_session = vk_api.VkApi(login, password)
    vk_session.auth()
    print('вход')

    vkaudio = VkAudio(vk_session)
    tracks1 = vkaudio.get(user_id1)
    print('загруженно user1')
    tracks2 = vkaudio.get(user_id2)
    print('загруженно user2')
    # print(tracks)

    user1 = []
    user2 = []
    for el in tracks1:
        # user1.append([el['id'], [el['artist'], el['title']]])
        # print(el['id'], '-', el['artist'], '-', el['title'])
        user1.append(el['id'])

    for el in tracks2:
        # print(el['id'], '-', el['artist'], '-', el['title'])
        # user2.append([el['id'], [el['artist'], el['title']]])
        user2.append(el['id'])

    per = []
    print(user1)
    print(user2)

    for i in user1:
        if i in user2:
            per.append(i)

    print()
    print(len(per), end='\n')
    print(f"{(len(per) / len(user1)) * 100}% сопадений user1 c user2")
    print(f"{(len(per) / len(user2)) * 100}% сопадений user2 c user1", end='\n')
    # print(per)

    for el in tracks1:
        if el['id'] in per:
            print(el['artist'], el['title'])

    t_end = time.time()
    print()
    print('Время выполнения:', (t_end - t_start), 'секунд')


if __name__ == '__main__':
    main()
