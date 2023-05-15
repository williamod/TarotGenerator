import pygame
import random
import math

pygame.init()
clock = pygame.time.Clock()
screen_width = 800
screen_height = 400
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('')

#GAME STATES
title_active = True
game_active = False
trans_active = False
key_active = False
return_trans = True
turn = 1
plays = 0
delay = 0
pause = 0
rec_wait = True

#ALPHAS
alpha = 225
alpha_cover = 255
alpha_card = 255
alpha_1 = 0
alpha_2 = 0
alpha_3 = 0
alpha_desc = 0
alpha_return = 0

#SOUNDS
title_music_active = False
game_music_active = False
trans_sound_active = False
card_trans = False
appear = False
appear1 = False
appear2 = False
appear3 = False
appear_text = False

#FONT OBJECTS
title_font = pygame.font.Font('Art/monobit.ttf', 200)
title_surf = title_font.render('Tar t',False, 'White')
title_rect = title_surf.get_rect(center = (400,50))
info_font = pygame .font.Font('Art/monobit.ttf', 45)
desc_font = pygame.font.Font('Art/monobit.ttf', 30)
return_font = pygame.font.Font('Art/monobit.ttf', 40)
return_surf = return_font.render('Press Space for Fortune', False, 'White')
return_rect = return_surf.get_rect(center = (400, 375))

names = ['Fool', 'Magician', 'High Priestess', 'Empress', 'Emperor', 'Heirophant', 'Lovers', 'Chariot', 'Strength', 'Hermit', 'Wheel of Fortune', 'Justice', 'Hanged Man', 'Death', 'Temperence', 'Devil', 'Tower', 'Star', 'Moon', 'Sun', 'Judgement', 'World']
desc_first1 = ['Potential', 'Manifestation', 'Intuition', 'Abundance', 'Leadership', 'Beliefs', 'Love', 'Triumph','Courage', 'Solitude', 'Cycles', 'Truth', 'Surrender','Release', 'Trust', 'Shadow', 'Upheaval', 'Healing', 'Subconscious', 'Awakening', 'Revelation', 'Completion']
desc_first2 = ['Innocence', 'Creation', 'Inner Knowing', 'Pleasure', 'Stability', 'Sacred Knowlede', 'Connection', 'Willpower', 'Comapssion', 'Reflection', 'Change', 'Fairness', 'Stillness', 'Endings', 'Faith', 'Power', 'Transformation', 'Hope', 'Hidden Things', 'Worthiness', 'Forgiveness', 'Wholeness']
desc_first3 = ['New Journey', 'Conduit', 'Reception', 'Nuturance', 'Community', 'Ritual', 'Choice', 'Achievement', 'Confidence', 'Enlightenment', 'Staying Present', 'Accountability', 'Understanding', 'Rebirth', 'Balance', 'Freedom', 'Paradigm Shift', 'Renewal', 'Visions', 'Warmth', 'Acceptance', 'Infinity']
desc_second1 =['Potential', 'Manifestation', 'Intuition', 'Abundance', 'Leadership', 'Beliefs', 'Love', 'Triumph','Courage', 'Solitude', 'Cycles', 'Truth', 'Surrender','Release', 'Trust', 'Shadow', 'Upheaval', 'Healing', 'Subconscious', 'Awakening', 'Revelation', 'Completion']
desc_second2 =['Innocence', 'Creation', 'Inner Knowing', 'Pleasure', 'Stability', 'Sacred Knowlede', 'Connection', 'Willpower', 'Comapssion', 'Reflection', 'Change', 'Fairness', 'Stillness', 'Endings', 'Faith', 'Power', 'Transformation', 'Hope', 'Hidden Things', 'Worthiness', 'Forgiveness', 'Wholeness']
desc_second3 =['New Journey', 'Conduit', 'Reception', 'Nuturance', 'Community', 'Ritual', 'Choice', 'Achievement', 'Confidence', 'Enlightenment', 'Staying Present', 'Accountability', 'Understanding', 'Rebirth', 'Balance', 'Freedom', 'Paradigm Shift', 'Renewal', 'Visions', 'Warmth', 'Acceptance', 'Infinity']
desc_third1 =['Potential', 'Manifestation', 'Intuition', 'Abundance', 'Leadership', 'Beliefs', 'Love', 'Triumph','Courage', 'Solitude', 'Cycles', 'Truth', 'Surrender','Release', 'Trust', 'Shadow', 'Upheaval', 'Healing', 'Subconscious', 'Awakening', 'Revelation', 'Completion']
desc_third2 =['Innocence', 'Creation', 'Inner Knowing', 'Pleasure', 'Stability', 'Sacred Knowlede', 'Connection', 'Willpower', 'Comapssion', 'Reflection', 'Change', 'Fairness', 'Stillness', 'Endings', 'Faith', 'Power', 'Transformation', 'Hope', 'Hidden Things', 'Worthiness', 'Forgiveness', 'Wholeness']
desc_third3 =['New Journey', 'Conduit', 'Reception', 'Nuturance', 'Community', 'Ritual', 'Choice', 'Achievement', 'Confidence', 'Enlightenment', 'Staying Present', 'Accountability', 'Understanding', 'Rebirth', 'Balance', 'Freedom', 'Paradigm Shift', 'Renewal', 'Visions', 'Warmth', 'Acceptance', 'Infinity']

#CARDS
card_width = 275/3
card_height = 475/3

card1 = pygame.image.load('Art/back.png')
card2 = pygame.image.load('Art/back.png')
card3 = pygame.image.load('Art/back.png')
card1_surf = pygame.transform.scale(card1, (card_width, card_height))
card2_surf = pygame.transform.scale(card2, (card_width, card_height))
card3_surf = pygame.transform.scale(card3, (card_width, card_height))

fool_surf = pygame.image.load('Art/0fool.png')
magician_surf = pygame.image.load('Art/1magician.png')
highpriestess_surf = pygame.image.load('Art/2highp.png')
empress_surf = pygame.image.load('Art/3empress.png')
emperor_surf = pygame.image.load('Art/4emperor.png')
heirophant_surf = pygame.image.load('Art/5heirophant.png')
lovers_surf = pygame.image.load('Art/6lovers.png')
chariot_surf = pygame.image.load('Art/7chariot.png')
strength_surf = pygame.image.load('Art/8strength.png')
hermit_surf = pygame.image.load('Art/9hermit.png')
wof_surf = pygame.image.load('Art/10wof.png')
justice_surf = pygame.image.load('Art/11justice.png')
hangedman_surf = pygame.image.load('Art/12hangman.png')
death_surf = pygame.image.load('Art/13death.png')
temperence_surf = pygame.image.load('Art/14temperence.png')
devil_surf = pygame.image.load('Art/15devil.png')
tower_surf = pygame.image.load('Art/16tower.png')
star_surf = pygame.image.load('Art/17star.png')
moon_surf = pygame.image.load('Art/18moon.png')
sun_surf = pygame.image.load('Art/19sun.png')
judgement_surf = pygame.image.load('Art/20judgement.png')
world_surf = pygame.image.load('Art/21world.png')

fool_surf = pygame.transform.scale(fool_surf, (card_width, card_height))
magician_surf = pygame.transform.scale(magician_surf, (card_width, card_height))
highpriestess_surf = pygame.transform.scale(highpriestess_surf, (card_width, card_height))
empress_surf = pygame.transform.scale(empress_surf, (card_width, card_height))
emperor_surf = pygame.transform.scale(emperor_surf, (card_width, card_height))
heirophant_surf = pygame.transform.scale(heirophant_surf, (card_width, card_height))
lovers_surf = pygame.transform.scale(lovers_surf, (card_width, card_height))
chariot_surf = pygame.transform.scale(chariot_surf, (card_width, card_height))
strength_surf = pygame.transform.scale(strength_surf, (card_width, card_height))
hermit_surf = pygame.transform.scale(hermit_surf, (card_width, card_height))
wof_surf = pygame.transform.scale(wof_surf, (card_width, card_height))
justice_surf = pygame.transform.scale(justice_surf, (card_width, card_height))
hangedman_surf = pygame.transform.scale(hangedman_surf, (card_width, card_height))
death_surf = pygame.transform.scale(death_surf, (card_width, card_height))
temperence_surf = pygame.transform.scale(temperence_surf, (card_width, card_height))
devil_surf = pygame.transform.scale(devil_surf, (card_width, card_height))
tower_surf = pygame.transform.scale(tower_surf, (card_width, card_height))
star_surf = pygame.transform.scale(star_surf, (card_width, card_height))
moon_surf = pygame.transform.scale(moon_surf, (card_width, card_height))
sun_surf = pygame.transform.scale(sun_surf, (card_width, card_height))
judgement_surf = pygame.transform.scale(judgement_surf, (card_width, card_height))
world_surf = pygame.transform.scale(world_surf, (card_width, card_height))

deck = [fool_surf, magician_surf, highpriestess_surf, empress_surf, emperor_surf, heirophant_surf, lovers_surf, chariot_surf, strength_surf, hermit_surf, wof_surf, justice_surf, hangedman_surf, death_surf, temperence_surf, devil_surf, tower_surf, star_surf, moon_surf, sun_surf, judgement_surf, world_surf]

moving_card_rect = pygame.Surface. get_rect(card2_surf, center = (screen_width/2, (screen_height/2)+50) )

card1_rect = pygame.Surface.get_rect(card1_surf, midtop = (400, 50))
card2_rect = pygame.Surface.get_rect(card2_surf, midtop = (400, 50))
card3_rect = pygame.Surface.get_rect(card3_surf, midtop = (400, 50))

#moon for now
moon_surf = pygame.image.load('Art/2.png')
moon_surf = pygame.transform.scale(moon_surf, (60,60))

beep = pygame.mixer.Sound('Art/bing.wav')

def draw_background():
    bg_1 = pygame.image.load('Art/1.png')
    bg_3 = pygame.image.load('Art/3.png')
    bg_4 = pygame.image.load('Art/4.png')
    bg_1 = pygame.transform.scale(bg_1, (screen_width,screen_height))
    bg_3 = pygame.transform.scale(bg_3, (screen_width,screen_height))
    bg_4 = pygame.transform.scale(bg_4, (screen_width,screen_height))

    screen.blit(bg_1, (0,0))
    screen.blit(bg_3, (0,0))
    screen.blit(bg_4, (0,0))
    
def card_cover_animation():
    global turn
    time = pygame.time.get_ticks()
    back_surf = pygame.image.load('Art/back.png')
    back_surf = pygame.transform.scale(back_surf, (abs((math.cos(time/1000)))*card_width, card_height))
    back_surf_flip = pygame.transform.flip(back_surf, True, False)
    back_rect = pygame.Surface.get_rect(back_surf, center = (screen_width/2, (screen_height/2)+50))
    flipper = (abs((math.cos(time/1000))))
    width = pygame.Surface.get_width(back_surf)

    if width < 1:
        turn = turn*(-1)

    if turn == 1:
        screen.blit(back_surf, (back_rect))

    if turn == -1:
        screen.blit(back_surf_flip, (back_rect))
     
def title_dis():
    global alpha
    screen.blit(title_surf, (title_rect))
    screen.blit(moon_surf, (420,45))
     
    for x in range(1000):
        alpha -= (x*0.00002)
            
        pygame.Surface.set_alpha(title_surf, alpha)
        pygame.Surface.set_alpha(moon_surf, alpha)
                                  
        if alpha <= 0:
            break
    
def card_move():
    global game_active, trans_active, card_trans 
    screen.blit(card2_surf, moving_card_rect)
    moving_card_rect.y -= 1.0
    if moving_card_rect.y <= 50:
        if not card_trans:
            pygame.mixer.music.load('sound/move.wav')
            pygame.mixer.music.play()
            card_trans = True
        moving_card_rect.y = 50
        screen.blit(card3_surf, card3_rect)
        screen.blit(card1_surf, card1_rect)
        
        card1_rect.x -= 1
        card3_rect.x += 1
        if card1_rect.x <= (400-(800/3)):
            card1_rect.x = (400-(800/3))
            game_active = True
            trans_active = False
        if card3_rect.x >= ((400+(800/3)-card_width)):
            card3_rect.x = (400+(800/3)-card_width)

def return_blink():
    time = pygame.time.get_ticks()
    pygame.Surface.set_alpha(return_surf, -127*(math.cos((time-13000)*.001))+127)
    screen.blit(return_surf, (return_rect))

while True:      
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  
            exit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE and key_active:
                plays += 1
                if plays ==1:
                    picks = random.sample([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21], 3)
                print(plays)
                trans_active = True
                title_active = False
                key_active = False
                game_active = False
            if event.key == pygame.K_RETURN and key_active:
                alpha = 255
                pygame.Surface.set_alpha(title_surf, alpha)
                pygame.Surface.set_alpha(moon_surf, alpha)
                
                trans_active = True
                game_active = False
                key_active = False

    draw_background()
    if title_active:
        if rec_wait:
            pygame.time.delay(6000)
            rec_wait = False
        if not title_music_active:
            pygame.mixer.music.load('sound/main.wav')
            pygame.mixer.music.play(-1)
            title_music_active = True
        time = pygame.time.get_ticks()
        screen.blit(moon_surf, (420,45))
        screen.blit(title_surf, (title_rect))
        card_cover_animation()
        
        if time > 13000:
            return_blink()
            key_active = True

    if trans_active:
        appear = False
        appear1 = False
        appear2 = False
        appear3 = False
        appear_text = False
        if not trans_sound_active:
            pygame.mixer.music.load('sound/begin.wav')
            pygame.mixer.music.play()
            trans_sound_active = True

        if plays == 1:
            title_dis()
            card_move()
                       
        if plays > 1:
            alpha_1 -= 2
            alpha_2 -= 2
            alpha_3 -= 2
            alpha_desc -= 2
            alpha_cover += 2

            if alpha_cover > 300:
                if return_trans:
                    card1_rect.x += 1
                    card3_rect.x -= 1
                    if card1_rect.x >= card2_rect.x:
                        return_trans = False
                        alpha_1 = 0
                        alpha_2 = 0
                        alpha_3 = 0
                        alpha_desc = 0
                        alpha_cover = 255
                        pause = 0
                        picks = random.sample([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21], 3)
                if not return_trans:
                    card1_rect.x -= 1
                    card3_rect.x += 1
                    if card1_rect.x <= (400-(800/3)):
                        card1_rect.x = (400-(800/3))
                        game_active = True
                        trans_active = False
                        return_trans = True
                    if card3_rect.x >= ((400+(800/3)-card_width)):
                        card3_rect.x = (400+(800/3)-card_width)

            pygame.Surface.set_alpha(first_font_surf, alpha_1)
            pygame.Surface.set_alpha(second_font_surf, alpha_2)
            pygame.Surface.set_alpha(third_font_surf, alpha_3)

            pygame.Surface.set_alpha(first1_desc_surf, alpha_desc)
            pygame.Surface.set_alpha(first2_desc_surf, alpha_desc)
            pygame.Surface.set_alpha(first3_desc_surf, alpha_desc)

            pygame.Surface.set_alpha(second1_desc_surf, alpha_desc)
            pygame.Surface.set_alpha(second2_desc_surf, alpha_desc)
            pygame.Surface.set_alpha(second3_desc_surf, alpha_desc)

            pygame.Surface.set_alpha(third1_desc_surf, alpha_desc)
            pygame.Surface.set_alpha(third2_desc_surf, alpha_desc)
            pygame.Surface.set_alpha(third3_desc_surf, alpha_desc)

            pygame.Surface.set_alpha(first_card, alpha_card)
            pygame.Surface.set_alpha(second_card, alpha_card)
            pygame.Surface.set_alpha(third_card, alpha_card)

            pygame.Surface.set_alpha(card1_surf, alpha_cover)
            pygame.Surface.set_alpha(card2_surf, alpha_cover)
            pygame.Surface.set_alpha(card3_surf, alpha_cover)

            screen.blit(first_font_surf, first_font_rect)
            screen.blit(second_font_surf, second_font_rect)
            screen.blit(third_font_surf, third_font_rect)

            screen.blit(first1_desc_surf, first1_desc_rect)
            screen.blit(first2_desc_surf, first2_desc_rect)
            screen.blit(first3_desc_surf, first3_desc_rect)

            screen.blit(second1_desc_surf, second1_desc_rect)
            screen.blit(second2_desc_surf, second2_desc_rect)
            screen.blit(second3_desc_surf, second3_desc_rect)

            screen.blit(third1_desc_surf, third1_desc_rect)
            screen.blit(third2_desc_surf, third2_desc_rect)
            screen.blit(third3_desc_surf, third3_desc_rect)

            screen.blit(first_card, (card1_rect))
            screen.blit(second_card,(card2_rect))
            screen.blit(third_card, (card3_rect))
        
            screen.blit(card1_surf, (card1_rect))
            screen.blit(card2_surf, (card2_rect))
            screen.blit(card3_surf, (card3_rect))

    if game_active:
          
        first_card = deck[picks[0]]
        second_card = deck[picks[1]]
        third_card = deck[picks[2]]
        
        first_font_surf = info_font.render(names[picks[0]], False, 'White')
        second_font_surf = info_font.render(names[picks[1]], False, 'White')
        third_font_surf = info_font.render(names[picks[2]], False, 'White')

        first_font_rect = pygame.Surface.get_rect(first_font_surf, center = (180,25))
        second_font_rect = pygame.Surface.get_rect(second_font_surf, center = (402,25))
        third_font_rect = pygame.Surface.get_rect(third_font_surf, center = (622,25))       

        first1_desc_surf = desc_font.render(desc_first1[picks[0]], False, 'White')
        first2_desc_surf = desc_font.render(desc_first2[picks[0]], False, 'White')
        first3_desc_surf = desc_font.render(desc_first3[picks[0]], False, 'White')

        second1_desc_surf = desc_font.render(desc_second1[picks[1]], False, 'White')
        second2_desc_surf = desc_font.render(desc_second2[picks[1]], False, 'White')
        second3_desc_surf = desc_font.render(desc_second3[picks[1]], False, 'White')

        third1_desc_surf = desc_font.render(desc_third1[picks[2]], False, 'White')
        third2_desc_surf = desc_font.render(desc_third2[picks[2]], False, 'White')
        third3_desc_surf = desc_font.render(desc_third3[picks[2]], False, 'White')

        first1_desc_rect = pygame.Surface.get_rect(first1_desc_surf, center = (177, 250))
        first2_desc_rect = pygame.Surface.get_rect(first2_desc_surf, center = (177, 275))
        first3_desc_rect = pygame.Surface.get_rect(first3_desc_surf, center = (177, 300))

        second1_desc_rect = pygame.Surface.get_rect(second1_desc_surf, center = (400, 250))
        second2_desc_rect = pygame.Surface.get_rect(second2_desc_surf, center = (400, 275))
        second3_desc_rect = pygame.Surface.get_rect(second3_desc_surf, center = (400, 300))

        third1_desc_rect = pygame.Surface.get_rect(third1_desc_surf, center = (620, 250))
        third2_desc_rect = pygame.Surface.get_rect(third2_desc_surf, center = (620, 275))
        third3_desc_rect = pygame.Surface.get_rect(third3_desc_surf, center = (620, 300))

        pygame.Surface.set_alpha(first_font_surf, alpha_1)
        pygame.Surface.set_alpha(second_font_surf, alpha_2)
        pygame.Surface.set_alpha(third_font_surf, alpha_3)

        pygame.Surface.set_alpha(first1_desc_surf, alpha_desc)
        pygame.Surface.set_alpha(first2_desc_surf, alpha_desc)
        pygame.Surface.set_alpha(first3_desc_surf, alpha_desc)

        pygame.Surface.set_alpha(second1_desc_surf, alpha_desc)
        pygame.Surface.set_alpha(second2_desc_surf, alpha_desc)
        pygame.Surface.set_alpha(second3_desc_surf, alpha_desc)

        pygame.Surface.set_alpha(third1_desc_surf, alpha_desc)
        pygame.Surface.set_alpha(third2_desc_surf, alpha_desc)
        pygame.Surface.set_alpha(third3_desc_surf, alpha_desc)

        pygame.Surface.set_alpha(first_card, alpha_card)
        pygame.Surface.set_alpha(second_card, alpha_card)
        pygame.Surface.set_alpha(third_card, alpha_card)

        pygame.Surface.set_alpha(card1_surf, alpha_cover)
        pygame.Surface.set_alpha(card2_surf, alpha_cover)
        pygame.Surface.set_alpha(card3_surf, alpha_cover)

        screen.blit(first_font_surf, first_font_rect)
        screen.blit(second_font_surf, second_font_rect)
        screen.blit(third_font_surf, third_font_rect)

        screen.blit(first1_desc_surf, first1_desc_rect)
        screen.blit(first2_desc_surf, first2_desc_rect)
        screen.blit(first3_desc_surf, first3_desc_rect)

        screen.blit(second1_desc_surf, second1_desc_rect)
        screen.blit(second2_desc_surf, second2_desc_rect)
        screen.blit(second3_desc_surf, second3_desc_rect)

        screen.blit(third1_desc_surf, third1_desc_rect)
        screen.blit(third2_desc_surf, third2_desc_rect)
        screen.blit(third3_desc_surf, third3_desc_rect)

        screen.blit(first_card, (card1_rect))
        screen.blit(second_card,(card2_rect))
        screen.blit(third_card, (card3_rect))       

        screen.blit(card1_surf, (card1_rect))
        screen.blit(card2_surf, (card2_rect))
        screen.blit(card3_surf, (card3_rect))
        
        for x in range(255):
            if not appear:
                pygame.mixer.music.load('sound/appear.wav')
                pygame.mixer.music.play()
                appear = True
            alpha_cover -= .01
            if alpha_cover < 0:
                alpha_cover = 0
                break
                  
        if alpha_cover == 0:
            if not appear1:
                    pygame.mixer.music.load('sound/appear1.wav')
                    pygame.mixer.music.play()
                    appear1 = True
            for x in range(255):               
                alpha_1 += .01
                if alpha_1 > 255:
                    alpha_1 = 255
                    break

        if alpha_1 == 255:   
            if not appear2:
                pygame.mixer.music.load('sound/appear2.wav')
                pygame.mixer.music.play()
                appear2 = True
            
            for x in range(255):
                alpha_2 += .01
                if alpha_2 > 255:
                    alpha_2 = 255
                    break

        if alpha_2 == 255: 
            if not appear3:
                    pygame.mixer.music.load('sound/appear3.wav')
                    pygame.mixer.music.play()
                    appear3 = True
            
            for x in range(255):
                alpha_3 += .01
                if alpha_3 > 255:
                    alpha_3 = 255
                    break

        if alpha_3 == 255:
            if not appear_text:
                    pygame.mixer.music.load('sound/text.wav')
                    pygame.mixer.music.play()
                    appear_text = True
            for x in range(255):               
                alpha_desc += .01
                if alpha_desc > 255:
                    alpha_desc = 255      
                    pause += 1
                    break

        if pause == 1:
            pygame.time.delay(6000)

        if pause > 1:
            if not game_music_active:
                pygame.mixer.music.load('sound/intro.wav')
                pygame.mixer.music.play(-1)
                game_music_active = True
                trans_sound_active = False

            return_blink()
            key_active = True

    clock.tick(60)
    pygame.display.update()
