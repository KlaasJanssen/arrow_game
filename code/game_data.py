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
(screen_width * 40/44, screen_height / 2, screen_width * 43 / 44, screen_height, 'wood', 'static')
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
(screen_width / 2, screen_height * 5/12, screen_width * 4/5, screen_height * 1/2, 'wood', 'static')
]
}

level_4 = {
'player_pos':(screen_width / 22, screen_height * (6/7)),
'ground_height':(screen_height * (6/7)),
'enemies':[
(screen_width * 17/22, screen_height * (6/7)),
(screen_width * 13/22, screen_height * (6/7)),
(screen_width * 1/2 + 30, screen_height * 5/12)],
'obstacles':[
(screen_width / 2, screen_height * 5/12, screen_width * 3/5, screen_height * 1/2, 'wood', 'dynamic', 'horizontal', 500, 1000, 2)
]
}

level_5 = {
'player_pos':(screen_width / 22, screen_height * (6/7)),
'ground_height':(screen_height * (6/7)),
'enemies':[
(screen_width * 17/44, screen_height * (6/7))
],
'obstacles':[
(screen_width * 7/22, screen_height * 8/12, screen_width * 8/22, screen_height * 6/7 + 1, 'wood', 'static'),
(screen_width * 7/22, screen_height * 8/12, screen_width * 10/22, screen_height * 17/24, 'wood', 'static'),
(screen_width * 13/22, screen_height * 7/12, screen_width * 14/22, screen_height * 6/7 + 1, 'metal', 'static')
]
}

levels = {
1:level_1,
2:level_2,
3:level_3,
4:level_4,
5:level_5
}
