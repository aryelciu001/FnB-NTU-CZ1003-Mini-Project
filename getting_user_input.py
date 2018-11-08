import pygame
import time 
from math import sqrt
from operator import itemgetter

#this function will generate the map
def display_map(posX,posY,window,ntuMap):   
    clk = pygame.time.Clock()
    fps = 120
    clk.tick(fps)
    if pygame.key.get_pressed()[pygame.K_UP]:
        if posY < 0:
            posY += 5
    elif pygame.key.get_pressed()[pygame.K_DOWN]:
        if posY > 600 - ntuMap.get_rect()[3]:
            posY -= 5
    elif pygame.key.get_pressed()[pygame.K_LEFT]:
        if posX < 0:
            posX += 5
    elif pygame.key.get_pressed()[pygame.K_RIGHT]:
        if posX > 600 - ntuMap.get_rect()[2]:
            posX -= 5
    window.blit(ntuMap,(posX,posY))   
    return posX, posY

#this function will return the coordinate 
#in the window if mouse left button is clicked
def mouse_click():
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
        elif i.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (1,0,0):
                return pygame.mouse.get_pos()

#this function will ask user location through clicking on the map
def get_user_location(posX,posY,window,ntuMap,windowHeight,windowWidth,whereAreYou):
    keep_run = True
    while keep_run:
        posX , posY = display_map(posX,posY,window,ntuMap)
        window.blit(whereAreYou,(0,0))
        pygame.display.update()
        user_location = mouse_click()
        if user_location != None:
            keep_run = False
        else:
            keep_run = True
        window.fill((0,0,0))
    
    return (user_location[0] - posX , user_location[1] - posY)

#will ask the user about the general food criteria (halal, vegetarian, none)
def get_user_preference(window,text,halal,veg,none,buttonXCoordinate,background):
    keep_run = True
    while keep_run:
        window.blit(background,(0,0))
        window.blit(text,(0,0))
        window.blit(halal,(buttonXCoordinate,200))
        window.blit(veg,(buttonXCoordinate,300))
        window.blit(none,(buttonXCoordinate,400))
        pygame.display.update()
        option = mouse_click()
        preference = None
        if option != None:
            if buttonXCoordinate < option[0] < buttonXCoordinate + 200:
                if 200 < option[1] < 280:
                    preference = 'halal'
                    keep_run = False
                elif 300 < option[1] < 380:
                    preference = 'veg'
                    keep_run = False
                elif 400 < option[1] < 480:
                    preference = 'none'
                    keep_run = False
    return preference
        
#will calculate the distance by simply using phytagoras theorem
#will need tuples as parameters
def distance_a_b(user_location, canteen_location):
    difX = user_location[0] - canteen_location[0]
    difY = user_location[1] - canteen_location[1]
    dist = sqrt(difX**2 + difY**2)
    return dist

#will return sorted canteen list based on distance
def sort_distance(user_location, canteen_list, preference):
    for i in canteen_list:
        dist = distance_a_b(user_location, i['coordinate'])
        i['distance_from_user'] = round(dist*1.94)
    sorted_canteen_list = sorted(canteen_list, key = itemgetter('distance_from_user'))
    sorted_with_preference = []
    if preference != 'none':
        for i in sorted_canteen_list:
            if i[preference] == True:
                sorted_with_preference.append(i)
    else:
        sorted_with_preference = sorted_canteen_list
    return sorted_with_preference

#will display menu for the user whether he wants to search by distance, rank, price range, or specific food
def show_menu(window, background, opening, sortByDistance,sortByRank,searchByFood,searchByPrice):
    keep_run = True
    posX = window.get_rect()[2]//2 - sortByDistance.get_rect()[2]//2
    while keep_run:
        window.blit(background,(0,0))
        window.blit(opening,(0,0))
        window.blit(sortByDistance,(posX , 150))
        window.blit(sortByRank,(posX, 250))
        window.blit(searchByPrice,(posX, 350))
        window.blit(searchByFood,(posX, 450))
        pygame.display.update()
        option = mouse_click()
        if option != None:
            if posX < option[0] < posX + sortByDistance.get_rect()[2]:
                if 150 < option[1] < 150 + 80:
                    keep_run = False
                    return 'sort by distance'
                elif 250 < option[1] < 250 + 80:
                    keep_run = False
                    return 'sort by rank'
                elif 350 < option[1] < 350 + 80:
                    keep_run = False
                    return 'search by price'
                elif 450 < option[1] < 450 + 80:
                    keep_run = False
                    return 'search by food'

#will return a list of canteen sorted based on rank
def sort_rank(canteen_list, preference):
    sorted_canteen_list = sorted(canteen_list, key = itemgetter('rank'))
    sorted_with_preference = []
    if preference != 'none':
        for i in sorted_canteen_list:
            if i[preference] == True:
                sorted_with_preference.append(i)
    else:
        sorted_with_preference = sorted_canteen_list
    return sorted_with_preference

#will display the clicker to change the price range of the food
def display_price(window, background,plusRange,minusRange,numBox,submit):
    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS',30)
    minPrice = 0.00
    maxPrice = 0.00
    keep_run = True
    posX = window.get_rect()[2]//2 - ((2*plusRange.get_rect()[2]) + numBox.get_rect()[2]+10)//2
    while keep_run:
        priceRance = myfont.render('Price Range',False,(255,255,255))
        minRange = myfont.render('Min',False,(255,255,255))
        maxRange = myfont.render('Max',False,(255,255,255))
        minPriceRender = myfont.render(str(minPrice),False,(255,255,255))
        maxPriceRender = myfont.render(str(maxPrice),False,(255,255,255))
        print(minRange.get_rect())

        window.blit(background,(0,0))
        window.blit(numBox,(window.get_rect()[2]//2 - numBox.get_rect()[2]//2,50))
        window.blit(numBox,(posX,170))
        window.blit(numBox,(posX,290))
        window.blit(priceRance,(window.get_rect()[2]//2 - numBox.get_rect()[2]//2 + 30,50+20))
        window.blit(minRange,(posX + 30,170+20))
        window.blit(maxRange,(posX +30,290+20))
        window.blit(minPriceRender,(posX+100,170+20))
        window.blit(maxPriceRender,(posX+100,290+20))
        window.blit(plusRange,((posX+10+numBox.get_rect()[2]),170))
        window.blit(minusRange,((posX+20+numBox.get_rect()[2]+plusRange.get_rect()[2]),170))
        window.blit(plusRange,((posX+10+numBox.get_rect()[2]),290))
        window.blit(minusRange,((posX+20+numBox.get_rect()[2]+plusRange.get_rect()[2]),290))
        window.blit(submit,(window.get_rect()[2]//2 - numBox.get_rect()[2]//2,400))
        pygame.display.update()
        plusMinus = mouse_click()
        if plusMinus != None:
            if (posX+10+numBox.get_rect()[2]) < plusMinus[0] < (posX+10+numBox.get_rect()[2] + plusRange.get_rect()[2]):
                if 170 < plusMinus[1] < (170+ plusRange.get_rect()[3]):
                    minPrice += 0.50
                elif 290 < plusMinus[1] < (290+ plusRange.get_rect()[3]):
                    maxPrice += 0.50
            elif (posX+20+numBox.get_rect()[2]+plusRange.get_rect()[2]) < plusMinus[0] < (posX+20+numBox.get_rect()[2]+(2*plusRange.get_rect()[2])):
                if 170 < plusMinus[1] < (170+ plusRange.get_rect()[3]):
                    if minPrice == 0.00:
                        pass
                    else:
                        minPrice -= 0.50
                elif 290 < plusMinus[1] < (290+ plusRange.get_rect()[3]):
                    if maxPrice == 0.00:
                        pass
                    else:
                        maxPrice -= 0.50
            if 400 < plusMinus[1] < (400 + numBox.get_rect()[3]):
                if (window.get_rect()[2]//2 - numBox.get_rect()[2]//2) < plusMinus[0] < (window.get_rect()[2]//2 + numBox.get_rect()[2]//2):
                    if minPrice>maxPrice:
                        minPrice = 0.00
                        maxPrice = 0.00
                    else:
                         keep_run = False
    return minPrice,maxPrice           

#will search the food based on price range
def search_by_price(canteen_list, preference, minPrice, maxPrice):
    sorted_canteen_list = []
    for i in canteen_list:
        for j in i['food'].values():
            if minPrice <= j <= maxPrice:
                sorted_canteen_list.append(i)
                break
    sorted_with_preference = []
    if preference != 'none':
        for i in sorted_canteen_list:
            if i[preference] == True:
                sorted_with_preference.append(i)
    else:
        sorted_with_preference = sorted_canteen_list
    return sorted_with_preference

#will search a specific food and return a list of canteen having the searched food
def search_by_food(canteen_list, theFood):
    canteen_with_food = []
    for i in canteen_list:
        for j in i['food']:
            if j.lower() == theFood:
                canteen_with_food.append(i)
                break
    return canteen_with_food

#will show a text box in which the user can input the food name
def search_by_food_display(window,background,foodPict,canteen_list,submit,empty):
    keep_run = True
    food = ''
    while keep_run:
        pygame.font.init()
        myfont = pygame.font.SysFont('Comic Sans MS',30)
        food_display = myfont.render(food,False,(255,255,255))
        window.blit(background,(0,0))
        window.blit(foodPict,(0,0))
        window.blit(empty,(0,250))
        window.blit(food_display,(0,300))
        keyboard_pressed = pygame.key.get_pressed()
        if keyboard_pressed != None:
            time.sleep(0.09)
            if keyboard_pressed[pygame.K_a]:
                food = food + 'a'
            elif keyboard_pressed[pygame.K_b]:
                food = food + 'b'
            elif keyboard_pressed[pygame.K_c]:
                food = food + 'c'
            elif keyboard_pressed[pygame.K_d]:
                food = food + 'd'
            elif keyboard_pressed[pygame.K_e]:
                food = food + 'e'
            elif keyboard_pressed[pygame.K_f]:
                food = food + 'f'
            elif keyboard_pressed[pygame.K_g]:
                food = food + 'g'
            elif keyboard_pressed[pygame.K_h]:
                food = food + 'h'
            elif keyboard_pressed[pygame.K_i]:
                food = food + 'i'
            elif keyboard_pressed[pygame.K_j]:
                food = food + 'j'
            elif keyboard_pressed[pygame.K_k]:
                food = food + 'k'
            elif keyboard_pressed[pygame.K_l]:
                food = food + 'l'
            elif keyboard_pressed[pygame.K_m]:
                food = food + 'm'
            elif keyboard_pressed[pygame.K_n]:
                food = food + 'n'
            elif keyboard_pressed[pygame.K_o]:
                food = food + 'o'
            elif keyboard_pressed[pygame.K_p]:
                food = food + 'p'
            elif keyboard_pressed[pygame.K_q]:
                food = food + 'q'
            elif keyboard_pressed[pygame.K_r]:
                food = food + 'r'
            elif keyboard_pressed[pygame.K_s]:
                food = food + 's'
            elif keyboard_pressed[pygame.K_t]:
                food = food + 't'
            elif keyboard_pressed[pygame.K_u]:
                food = food + 'u'
            elif keyboard_pressed[pygame.K_v]:
                food = food + 'v'
            elif keyboard_pressed[pygame.K_w]:
                food = food + 'w'
            elif keyboard_pressed[pygame.K_x]:
                food = food + 'x'
            elif keyboard_pressed[pygame.K_y]:
                food = food + 'y'
            elif keyboard_pressed[pygame.K_z]:
                food = food + 'z'
            elif keyboard_pressed[pygame.K_BACKSPACE]:
                food = food[0:-1]
            elif keyboard_pressed[pygame.K_SPACE]:
                food = food + ' '
        window.blit(submit,(window.get_rect()[2]//2 - submit.get_rect()[2]//2,500))
        pygame.display.update()
        submitButton = mouse_click()
        if submitButton != None:
            if 500 < submitButton[1] < 600:
                if window.get_rect()[2]//2 - submit.get_rect()[2]//2 < submitButton[0] < window.get_rect()[2]//2 + submit.get_rect()[2]//2:
                    keep_run = False

    return search_by_food(canteen_list,food), food

