import pygame
pygame.init()

#will display the sort by distance option result
def display_sort_by_distance(sorted_canteen_list):
    print('Here are the restaurant nearest to you : ')
    for i in sorted_canteen_list:
        print("---------------------------------------------------")
        print()
        print(i['name'] ,':', i['distance_from_user'],'m away!')
        print()
        print("---------------------------------------------------")

        print("food available : ")
        for j in i['food'].keys():
            print('{0} : {1}'.format(j, i['food'][j]))
        
        print()
    
        print('operating hours : {0}'.format(i['operating_hours']))  
    
#will display the sort by rank option result
def display_sort_by_rank(sorted_canteen_list):
    print("Here is the restaurant's ranking in NTU")
    count = 1
    for i in sorted_canteen_list:
        print("---------------------------------------------------")
        print()
        print(str(count)+'.',i['name'])
        print()
        print("---------------------------------------------------")

        print("food available : ")
        for j in i['food'].keys():
            print('{0} : {1}'.format(j, i['food'][j]))
        
        print()
    
        print('operating hours : {0}'.format(i['operating_hours']))
        count += 1
        
#will display the search by price option result        
def display_search_by_price(sorted_canteen_list,minPrice,maxPrice):
    if len(sorted_canteen_list) == 0:
        print("Sorry we cannot find your preferred restaurant")
    else:
        print('Here are the restaurants with your criteria : ')
        for i in sorted_canteen_list:
    
            print("---------------------------------------------------")
            print()
            print(i['name'])
            print()
            print("---------------------------------------------------")

            print("food available : ")
            for j in i['food'].keys():
                if minPrice < i['food'][j] < maxPrice:
                    print('{0} : {1}'.format(j, i['food'][j]))
                else:
                    pass
            print()
        
            print('operating hours : {0}'.format(i['operating_hours']))


#will display the search by food option result        
def display_search_by_food(sorted_canteen_list,food):
    if len(sorted_canteen_list) == 0:
            print("Sorry we cannot find your preferred restaurant")
    else:
        print('Here are the restaurant with your preferred food : ')
        for i in sorted_canteen_list:
            print("---------------------------------------------------")
            print()
            print(i['name'])
            print()
            print("---------------------------------------------------")

            print("food available : ")
            for j in i['food'].keys():
                if j.lower() == food.lower():
                    print('{0} : {1}'.format(j, i['food'][j]))
                else:
                    pass
            print()
        
            print('operating hours : {0}'.format(i['operating_hours']))

def display_map_with_canteen_and_user(window,ntuMap,posX,posY,user,user_location,sorted_canteen_list,canteen_name,nextButton):
    from getting_user_input import mouse_click
    pygame.font.init()
    myText = pygame.font.SysFont('Comic Sans MS', 12)
    print(user_location)
    clk = pygame.time.Clock()
    fps = 120
    keep_run = True
    display_sort_by_distance(sorted_canteen_list)
    while keep_run:
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
        window.blit(user,(posX+user_location[0]-(user.get_rect()[2]//2),posY+user_location[1]-user.get_rect()[3]))
        for i in sorted_canteen_list:
            text = myText.render(i['name'],False,(255,255,255))
            window.blit(canteen_name,(i['coordinate'][0]+posX-(canteen_name.get_rect()[2]//2),i['coordinate'][1]+posY-canteen_name.get_rect()[3]))
            window.blit(text,(i['coordinate'][0]+posX-(canteen_name.get_rect()[2]//2)+2,i['coordinate'][1]+posY-canteen_name.get_rect()[3]))
        window.blit(nextButton,(600-nextButton.get_rect()[2],600-nextButton.get_rect()[3]))            
        pygame.display.update()
        user_click = mouse_click()
        if user_click != None:
            if (600-nextButton.get_rect()[2] < user_click[0] < 600) and (600-nextButton.get_rect()[3] < user_click[1] < 600):
                keep_run = False


        
    