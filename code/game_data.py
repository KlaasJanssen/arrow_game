from settings import screen_height, screen_width

level_1 = {
'player_pos':(screen_width / 22, screen_height * (6/7)),
'ground_height':(screen_height * (6/7)),
'enemies':[
(screen_width * 17/22, screen_height * (6/7)),
],
'obstacles':[
]
}

level_2 = {
'player_pos':(screen_width / 22 + 30, screen_height * (6/7) + 20),
'ground_height':(screen_height * (6/7) + 20),
'enemies':[
(screen_width * 17/22, screen_height * (6/7) + 20),
(screen_width * 13/22, screen_height * (6/7) + 20)],
'obstacles':[
(screen_width * 40/44, screen_height / 2, screen_width * 43 / 44, screen_height)
]
}

level_3 = {
'player_pos':(screen_width / 22, screen_height * (6/7)),
'ground_height':(screen_height * (6/7)),
'enemies':[
(screen_width * 17/22, screen_height * (6/7)),
(screen_width * 13/22, screen_height * (6/7)),
(screen_width * 3/5, screen_height * 5/12)],
'obstacles':[
(screen_width / 2, screen_height * 5/12, screen_width * 4/5, screen_height * 1/2)
]
}

levels = {
1:level_1,
2:level_2,
3:level_3
}
