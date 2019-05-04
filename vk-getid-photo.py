import json
import vk, time, math

import sys, os
from pathlib import Path
home = str(Path.home())

sys.path.append(os.path.abspath(home + '/scripts/DATA/'))
from vk_universal import token, id, path_photo_liker 

APIVersion = 5.73

timestamp = int(time.time())

#N likes
#count  = str(125)
count = input("\nNumber of photos: ")
#miss N pictures
offset = str(0)

#name+time
#name = (count + "pic" + offset + "miss.json" )
name = (str(timestamp) + ".json")
filepath = (home + path_photo_liker + name)


session = vk.Session(access_token=token)
vk_api = vk.API(session,v=APIVersion)


source = vk_api.photos.get(owner_id=id, album_id=-15, count=count, rev=1, offset=offset)
#extended=1
print(source)

print ("\nFILENAME:", timestamp)

with open(filepath, "w") as write_file:
    json.dump(source, write_file)
