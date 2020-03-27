import requests
r=requests.get('https://stepic.org/media/attachments/course67/3.6.3/699991.txt')
print(r.text)
while(len(r.text)<15):
    r=requests.get('https://stepic.org/media/attachments/course67/3.6.3/'+r.text)
    print(r.text)


