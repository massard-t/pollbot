#!/usr/bin/env python3.5
# coding: utf-8
import yaml
from collections import namedtuple

INFOS = "data.yaml"

songs = [
        {"name": "This is the first song",
            "banned": 0},
        {"name": "This is the second song",
            "banned": 0},
        {"name": "Kill me please",
            "banned": 1}
        ]

firstAlbum = {
        "nbr_songs": len(songs),
        "songs": songs,
        "name": "a pretty cool album"
        }

albums = [
        firstAlbum
        ]



res = yaml.dump(albums)

with open(INFOS, 'w') as f:
    f.writelines(res)

with open(INFOS, 'r') as f:
    content = yaml.load(f)

print(content[0])
