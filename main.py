import vk_api
from vk_api.audio import VkAudio
import time

def main():
    t_start = time.time()
    user_id = 550033465
    login, password = '+79891331486', 'AFsdqw12'
    vk_session = vk_api.VkApi(login, password)
    vk_session.auth()
    print('вход')

    vkaudio = VkAudio(vk_session)
    tracks = vkaudio.get(user_id)
    print('загруженно')
    print(tracks)

    for el in tracks:
        print(el['id'], el['artist'], el['title'])

    t_end = time.time()
    print()
    print('Время выполнения:', (t_end - t_start))

if __name__ == '__main__':
    main()