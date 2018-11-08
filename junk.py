#this function will display yes no button on window
def display_yes_no(window,windowWidth,windowHeight,buttonWidth,buttonHeight,yesButton,noButton):
    window.blit(yesButton,(windowWidth//2 - buttonWidth - 50, windowHeight//2 - buttonHeight//2))
    window.blit(noButton,(windowWidth//2 + 50, windowHeight//2 - buttonHeight//2))

#this function enables the user to choose yes or no through window
#it will return 2 value, whether the user wants to use location or not
#and the the value to keep the loop running while input has not been received
def user_yes_no(run,window,windowWidth,windowHeight,buttonWidth,buttonHeight,yesButton,noButton):
    display_yes_no(window,windowWidth,windowHeight,buttonWidth,buttonHeight,yesButton,noButton)   

    #position of button in the map
    topLeftYes = (windowWidth//2 - 50 - buttonWidth, windowHeight//2 - buttonHeight//2)
    bottomRightYes = (windowWidth//2 - 50, windowHeight//2 + buttonHeight//2)
    topLeftNo = (windowWidth//2 + 50, windowHeight//2 - buttonHeight//2)
    bottomRightNo = (windowWidth//2 + 50 + buttonWidth, windowHeight//2 + buttonHeight//2)
    
    #getting user input
    position = mouse_click()
    use_location = False 

    #will continue the main loop if not clicked
    if position != None:
        #will go to another loop which starts when yes is inserted
        if (topLeftYes[0] < position[0] < bottomRightYes[0] and topLeftYes[1] < position[1] < bottomRightYes[1]):
            use_location = True
            print("Great!")
            run = False
            return use_location, run
        #will go to another loop which starts when no is inserted
        else:
            print("Okay")
            use_location = False
            run = False
            return use_location, run
    else:
        run = True
        return use_location, run

#this function will determine whether the user is concerned 
#about distance or not
def find_nearest(posX,posY, window, ntuMap, yesButton, noButton, windowWidth, windowHeight, buttonWidth, buttonHeight,background):
    keep_run = True
    use_location = False
    while keep_run:
        window.fill((0,0,0))
        posX, posY = display_map(posX,posY,window,ntuMap)
        window.blit(background,(0,0))
        display_yes_no(window,windowWidth,windowHeight,buttonWidth,buttonHeight,yesButton,noButton)    
        pygame.display.update()
        use_location , keep_run = user_yes_no(keep_run,window,windowWidth,windowHeight,buttonWidth,buttonHeight,yesButton,noButton)
    return use_location