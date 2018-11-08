# ------initializing------ #

import pygame
import time
from math import sqrt
from operator import itemgetter
from getting_user_input import *
from output_display import *
from canteen_list import canteen_list
from images_for_display import *
pygame.init()

#sizing & initializing
windowWidth, windowHeight = 600,600
buttonWidth, buttonHeight= 100, 70
window = pygame.display.set_mode((windowWidth,windowHeight))
pygame.display.set_caption("FnB NTU")
posX, posY = 0, 0
foodCriteriaButtonX = window.get_rect()[2]//2 - halal.get_rect()[2]//2

# ------mainLoop------ #

run = True
while run:
    print()
    print("----------------------FnB NTU----------------------")
    print()
    option = show_menu(window, background, opening, sortByDistance, sortByRank, searchByFood, searchByPrice)
    if option == 'sort by distance':
        user_location = get_user_location(posX,posY,window,ntuMap,windowHeight,windowWidth,whereAreYou)
        preference = get_user_preference(window,foodCriteria, halal, veg, none, foodCriteriaButtonX, background)
        sorted_canteen_list = sort_distance(user_location, canteen_list, preference)
        display_map_with_canteen_and_user(window,ntuMap,posX,posY,user,user_location,sorted_canteen_list,canteen_name,nextButton)

    elif option == 'sort by rank':
        preference = get_user_preference(window,foodCriteria, halal, veg, none, foodCriteriaButtonX, background)
        sorted_canteen_list = sort_rank(canteen_list, preference)
        display_sort_by_rank(sorted_canteen_list)

    elif option == 'search by price':
        minPrice, maxPrice = display_price(window,background,plusRange,minusRange,numBox,submit)
        preference = get_user_preference(window,foodCriteria, halal, veg, none, foodCriteriaButtonX, background)
        sorted_canteen_list = search_by_price(canteen_list, preference, minPrice, maxPrice)
        display_search_by_price(sorted_canteen_list,minPrice,maxPrice)

    elif option == 'search by food':
        sorted_canteen_list, food = search_by_food_display(window,background,foodPict, canteen_list, submit,empty)
        display_search_by_food(sorted_canteen_list,food)