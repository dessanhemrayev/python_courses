import req
r=requests.get('https://stepic.org/media/attachments/course67/3.6.3/699991.txt')
s="We"
for s in r.text:
    r=requests.get('https://stepic.org/media/attachments/course67/3.6.3/'+r.text)



