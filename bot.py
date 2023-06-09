from vk_api.longpoll import VkEventType
import vk_captchasolver as vc
import threading
import datetime
import random
import vk_api
import time

msgs = [t for t in m_file.read().split("\n") if t]
m_file.close()

now = datetime.datetime.now()
n = str(now).replace(" ", "_").replace(":", "-").split(".")[0]
log_path = f"logs/log_{n}.txt"


def write_log(info):
    print(info)
    log = open(log_path, "at", encoding='utf-8', errors='ignore')
    log.write(str(info)+"\n")
    log.close()
def print_msg(u_id, text):
    print("*" * 50)
    print("Сообщение в личке")
    print(f"От кого: https://vk.com/id{u_id}")
    print(f"Сообщение: {text}")

def thr_st(void, arg=()):
def friends():
    while True:
        try:
            try:
                friend_rq = vk.friends.getRequests()['items']
                for user in friend_rq:
                    vk.friends.add(user_id=user)
            except:
                pass
            try:
                unfriend_rq = vk.friends.getRequests(out="true")['items']
                for user in unfriend_rq:
                    vk.friends.delete(user_id=user)
            except:
                pass
            friend_rq = vk.friends.getRequests()['items']
            for user in friend_rq:
                vk.friends.add(user_id=user)
            unfriend_rq = vk.friends.getRequests(out="true")['items']
            for user in unfriend_rq:
                vk.friends.delete(user_id=user)
        except:
            pass


def send_message(peer, text, reply_to=True, reply_id=None):
    try:
        if reply_to:
            vk.messages.send(
                peer_id=peer,
                random_id=random.randint(1, 999999),
                message=text,
                reply_to=reply_id
            )
        else:
            vk.messages.send(
                peer_id=peer,
                random_id=random.randint(1, 999999),
                message=text
            )
    except vk_api.Captcha as e:
        answer = vc.solve(sid=e.sid, s=1)
        if reply_to:
            vk.messages.send(
                peer_id=peer,
                message=text,
                random_id=random.randint(1, 999999),
                reply_to=reply_id,
                captcha_key=answer,
                captcha_sid=e.sid
            )
        else:
            vk.messages.send(
                peer_id=peer,
                message=text,
                random_id=random.randint(1, 999999),
                captcha_key=answer,
                captcha_sid=e.sid
            )
        time.sleep(5)


thr_st(friends, ())
def send_message(peer, text, reply_to=True, reply_id=None):
    try:
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and not event.from_me:
                msg = random.choice(msgs)
                peer_id = event.peer_id
                chat_id = peer_id - 2000000000
                user_id = event.user_id
                ch = random.choice(chance)
                msg_id = event.message_id
                event_msg = vk.messages.getById(message_ids=msg_id)
                isreply = False
                try:
                    rep_to_user = event_msg['items'][0]['reply_message']['from_id']
                    if rep_to_user == cfg.acc_id:
                        if event.text:
                            write_log("*" * 50)
                            write_log(f"Айди чата: {chat_id}")
                            write_log(f"От кого: https://vk.com/id{event.user_id}")
                            write_log(f"Сообщение: {event.text}")
                        ch = 1
                        isreply = True
                except:
                    pass
                if ch == 1 and not isreply and cfg.answer_only_on_replies:
                    ch = 0

                if event.text and chat_id < 0:
                    kf_pos = event.text.find("https://vk.me/join/")
                    if kf_pos > -1:
                        link = event.text[kf_pos:].split(" ")[0]
                        vk.messages.joinChatByInviteLink(link=link)
                    else:
                        write_log("*" * 50)
                        write_log("Сообщение в личке")
                        write_log(f"От кого: https://vk.com/id{event.user_id}")
                        write_log(f"Сообщение: {event.text}")
                if ch == 1 and chat_id not in chat_ignore and user_id not in user_ignore and user_id > 0:
                if chat_id not in chat_ignore and user_id not in user_ignore and user_id > 0:
                    ch = random.choice(chance)
                    event_msg = vk.messages.getById(message_ids=msg_id)
                    try:
                        if cfg.acc_id in event.raw['mentions']:
                            ch = 1
                            print_msg(user_id, event.text)
                    except:
                        pass
                    if event.text and peer_id < 2000000000:
                        print_msg(user_id, event.text)
                        kf_pos = event.text.find("https://vk.me/join/")
                        if kf_pos > -1:
                            link = event.text[kf_pos:].split(" ")[0]
                            vk.messages.joinChatByInviteLink(link=link)
                    if ch == 1:
                        vk.messages.setActivity(
                            type="typing",
                            peer_id=peer_id
                        )
                    except:
                        pass
                    time.sleep(cfg.send_delay)
                    if cfg.reply_only == 1:
                        send_message(peer_id, msg, reply_id=msg_id)
                    elif cfg.reply_only == 2:
                        reply = random.choice([True, False])
                        if reply:
                            send_message(peer_id, msg, reply_id=msg_id)
                        else:
                            send_message(peer_id, msg, reply_to=False)
                    elif cfg.reply_only == 0:
                        send_message(peer_id, msg, reply_to=False)

                        msg = random.choice(msgs)
                        try:
                            vk.messages.send(
                                peer_id=peer_id,
                                random_id=random.randint(1, 999999),
                                message=msg,
                                reply_to=msg_id
                            )
                        except vk_api.Captcha as e:
                            answer = vc.solve(sid=e.sid, s=1)
                            time.sleep(5)
                            vk.messages.send(
                                peer_id=peer_id,
                                message=msg,
                                random_id=random.randint(1, 999999),
                                reply_to=msg_id,
                                captcha_key=answer,
                                captcha_sid=e.sid
                            )
    except KeyboardInterrupt:
        break
    except:
        pass