import vk
from time import sleep

import sys, os
from pathlib import Path
home = str(Path.home())

sys.path.append(os.path.abspath(home + '/scripts/DATA/'))
from vk_universal import token, id 

APIVersion = 5.73

session = vk.Session(access_token=token)
vk_api = vk.API(session,v=APIVersion)

#N likes
count = input("\nNumber of photos: ")
#miss N pictures
offset = str(0)


source = vk_api.photos.get(owner_id=id, album_id=-15, count=count, rev=1, offset=offset)
print(source)

n = 0
counter = 0

while(n != int(count)):
    json_data = source['items'][n]['id']
    print (json_data)
    r = vk_api.likes.add(owner_id=id, item_id=json_data, type='photo')
    counter += 1
    n +=1 
    print(counter, json_data, r)
    sleep (1.5)
