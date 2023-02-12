import vk_api
import time

vk_session = vk_api.VkApi('+79888384971', 'aRV20050505')
vk_session.auth()

vk = vk_session.get_api()
for i in range(10):
    try:
        if s_id and code:
             print(vk.wall.repost(object='wall-126227863_90727', captcha_sid=s_id, captcha_key=code))
             s_id = False
             code = False
        else:
             print(vk.wall.repost(object='wall-126227863_90727'))
    except vk_api.Captcha as e:
        s_id = e.sid
        print(e.url)
        code = input()
        i = i-1