import sys
import mailbox
import email
import quopri
from bs4 import BeautifulSoup as bs
import json

MBOX=sys.argv[1]

def jsonifymessage(msg):
    jmsg=[]
    for (k,v) in msg.items():
        jmsg[k]=v.decode('utf8','ignore')
    for k in ['To','Cc','Bcc']:
        if not jmsg.get(k):
            continue
        jmsg[k]=jmsg[k].replace('\n','').replace('\n','').replace('\t','').replace('\r','').decode('utf8','ignore').split(',')
    for part in msg.walk:
        jpart['contenttype']=part.get_content_type()
        content=part.get_payload(decode=False).decode('utf8','ignore')
        c=quopri.decodestring(content)
        soup=bs(content)
        jpart['content']=''.join(soup.findAll(text=True))
        jmsg['part'].append(jpart)
    return jmsg
        
mbox=mailbox.UnixMailbox(open(MBOX,'rb'),email.message_from_file)
json_msgs=[]
while 1:
    msg=mbox.next()
    if msg is None:
        break
    json_msgs.append(jsonifymessage(msg))
print json.dumps(json_msgs,indent=4)