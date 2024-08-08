#game setup
size    = 2
HEIGHT  = 360 * size
WIDTH   = round(HEIGHT*1.77778)
FPS     = 30
CENTER  = (WIDTH/2,HEIGHT/2)

card_width = 120*size
card_height = 160*size

cards = {
    0 : {'name':'fool','desc':['potential', 'innocence', 'new journey'], 'path' : 'art/fool.png'},
    1 : {'name' :'magician', 'desc' : ['manifestation','creation','conduit'], 'path': 'art/magician.png'},
    2: {'name': 'high priestess', 'desc': ['intuition', 'inner knowing', 'reception'], 'path': 'art/hp.png'},
    3: {'name': 'empress', 'desc': ['abundance', 'pleasure', 'nurturance'], 'path': 'art/empress.png'},
    4: {'name': 'emperor', 'desc': ['leadership', 'stability', 'community'], 'path': 'art/emperor.png'},
    5: {'name': 'hierophant', 'desc': ['beliefs', 'sacred knowledge', 'ritual'], 'path': 'art/heirophant.png'},
    6: {'name': 'lovers', 'desc': ['love', 'connection', 'choice'], 'path': 'art/lovers.png'},
    7: {'name': 'chariot', 'desc': ['triumph', 'willpower', 'achievement'], 'path': 'art/chariot.png'},
    8: {'name': 'strength', 'desc': ['courage', 'compassion', 'confidence'], 'path': 'art/strength.png'},
    9: {'name': 'hermit', 'desc': ['solitude', 'reflection', 'enlightenment'], 'path': 'art/hermit.png'},
    10: {'name': 'wheel of fortune', 'desc': ['cycles', 'change', 'staying present'], 'path': 'art/wof.png'},
    11: {'name': 'justice', 'desc': ['truth', 'fairness', 'accountability'], 'path': 'art/justice.png'},
    12: {'name': 'hanged man', 'desc': ['surrender', 'stillness', 'understanding'], 'path': 'art/hangman.png'},
    13: {'name': 'death', 'desc': ['release', 'endings', 'rebirth'], 'path': 'art/death.png'},
    14: {'name': 'temperance', 'desc': ['trust', 'faith', 'balance'], 'path': 'art/temperence.png'},
    15: {'name': 'devil', 'desc': ['shadow', 'power', 'freedom'], 'path': 'art/devil.png'},
    16: {'name': 'tower', 'desc': ['upheaval', 'transformation', 'paradigm shift'], 'path': 'art/tower.png'},
    17: {'name': 'star', 'desc': ['healing', 'hope', 'renewal'], 'path': 'art/star.png'},
    18: {'name': 'moon', 'desc': ['subconscious', 'hidden things', 'visions'], 'path': 'art/moon.png'},
    19: {'name': 'sun', 'desc': ['awakening', 'worthiness', 'warmth'], 'path': 'art/sun.png'},
    20: {'name': 'judgement', 'desc': ['revelation', 'forgiveness', 'acceptance'], 'path': 'art/judgement.png'},
    21: {'name': 'world', 'desc': ['completion', 'wholeness', 'infinity'], 'path': 'art/world.png'}
}

sounds = {
    'appear'    :   ['sound/appear.wav','sound/appear1.wav','sound/appear2.wav','sound/appear3.wav'],
    'begin'     :   'sound/begin.wav',
    'intro'     :   'sound/intro.wav',
    'main'      :   'sound/main.wav',
    'move'      :   'sound/move.wav',
    'text'      :   'sound/text/wav' 
}

volume = {
    'music' : 0.5,
    'sfx' : 0.25
}

ui_dimensions = {
    1:  (320,180),
    2:  (640,360),
    3:  (1280,720),
    4:  (1920,1080),
    6:  (2560,1440)
}

screen_dimensions = {
    1:  (640,360),
    2:  (1280,720),
    3:  (1920,1080),
    4:  (2560,1440),
    6:  (3840,2160)
}

gear_button_size = {
    1: (50,50),
    2: (100,100),
    3: (150,150),
    4: (200,200)
}

# SCREEN DIMENSIONS
# 360p:     640x360    x1
# 720p:     1280x720   x2
# 1080p:    1920X1080  x3
# 1440p:    2560x1440  x4
# 2160p:    3840x2160  x6