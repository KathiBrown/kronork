import requests
import json
def get_updates(offset=None):
    url = "https://api.telegram.org/bot729045385:AAHFPuz1CdmGNSvUme8IPeTc8acF08E2Rsw/getUpdates?timeout=100"
    if offset:
        url = url+"&offset={}".format(offset+1)
    r = requests.get(url)
    return json.loads(r.content)
def send_message(msg,chat_id):
    url = "https://api.telegram.org/bot729045385:AAHFPuz1CdmGNSvUme8IPeTc8acF08E2Rsw/sendMessage?chat_id={}&text={}".format(chat_id, msg)
    if msg is not None:
        requests.get(url)


def make_reply(msg):
    reply = "Everyone hates you"
    return reply    
    
update_id = None
while True:
    print "..."
    updates = get_updates(offset=update_id)
    updates = updates["result"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                message = item["message"]["text"]
            except:
                message = None
            from_ = item["message"]["from"]["id"]
            reply = make_reply(message)
            send_message(reply,from_)
