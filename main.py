"""
Chris Grady
Spring 2016
CIST 2742 Project
------------------
Pick - a - Politician!
Using Python w/ Pygame
"""

import os
import pygame
import random
import webbrowser
import og, logEntry, logView
from time import sleep

# Positioning window location upon execution
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (400,200)

# Defining Classes
class Target(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('zCrosshair.png').convert_alpha()
        self.rect = self.image.get_rect()
    
# Defining colors
Red = (255, 0, 0)
White = (255, 255, 255)
Blue = (0, 0, 205)
Black = (0, 0, 0)
Green = (34, 139, 34)

#---------------------------------------------------------------------
# Splash Screen Function *********************************************
#---------------------------------------------------------------------
def splashScreen(screen):
    splash = True               # Sentinel for splash screen

    # Loads Splash Screen Logo and background
    splash = pygame.image.load('zFlag.png').convert()
    logo = pygame.image.load('zLogo.png').convert()

    while splash:     
        # Set the screen background
        screen.fill(White)
        screen.blit(splash, (0,0))
        # Drawing and positioning splash screen logo
        splash_rect = logo.get_rect()
        # Centering Text
        splash_x = screen.get_width() / 2 - splash_rect.width / 2
        splash_y = screen.get_height() / 2 - splash_rect.height / 2
        # Blitting to screen
        screen.blit(logo, [splash_x, splash_y])    
        # Updating screen
        pygame.display.flip()
        # Splash screen stops after 5 Seconds
        sleep(3.5)
        splash = False
#---------------------------------------------------------------------  

#---------------------------------------------------------------------
# Instruction Screen Function ****************************************
#---------------------------------------------------------------------
def instructionScreen(screen):
    instructions = True         # Sentinel for Instructions screen
    gameOver = False            # Sentinel for main game loop
    forceQuit = False           # Sentinel for main game loop

    # Font Styling
    fontInit = pygame.font.Font(None, 36)
    fontHeader = pygame.font.Font(None, 75)
    fontFooter = pygame.font.Font(None, 120)

    bush = pygame.image.load('zBush.png').convert()

    # Instruction screen is displayed until user clicks or presses a key
    while instructions:
        # Allows user to quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                instructions = False 
                gameOver = True
                forceQuit = True
                return (gameOver, forceQuit)
            # Allows user to advance to main screen
            elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
                instructions = False
                sleep(0.2)
                return (gameOver, forceQuit)
     
        # Set the screen background
        screen.fill(Black)

        # Positioning image
        bush_rect = bush.get_rect()
        bushX = screen.get_width() / 2 - bush_rect.width / 2
        bushY = 35
        # Bush throwback
        screen.blit(bush, (bushX,bushY))
     
        # Drawing instructions page
        # Text Box 1
        text = fontFooter.render("Instructions:", True, Red)
        text_rect = text.get_rect()
        # Centering Text
        text_x = 560 - text_rect.width / 2
        text_y = 250
        # Blitting to screen
        screen.blit(text, [text_x, text_y])            

        # Text Box 2
        text = fontInit.render("In this game, you will be selecting political statements that you STRONGLY AGREE with.", True, Green)
        text_rect = text.get_rect()
        # Centering Text
        text_x = 560 - text_rect.width / 2
        text_y = 360
        # Blitting to screen
        screen.blit(text, [text_x, text_y])

        # Text Box 3
        text = fontInit.render("At the bottom of the screen, select the one candidate that you like the LEAST.", True, Green)
        text_rect = text.get_rect()
        # Centering Text
        text_x = 560 - text_rect.width / 2
        text_y = 400
        # Blitting to screen
        screen.blit(text, [text_x, text_y])
        
        # Text Box 4
        text = fontInit.render("Click the FINISH button when you are done, and your ideal candidate will be revealed.", True, Green)
        text_rect = text.get_rect()
        # Centering Text
        text_x = 560 - text_rect.width / 2
        text_y = 440
        # Blitting to screen
        screen.blit(text, [text_x, text_y])

        # Text Box 5
        text = fontInit.render("(Click anywhere on the screen or press any key to continue)", True, White)
        text_rect = text.get_rect()
        # Centering Text
        text_x = 560 - text_rect.width / 2
        text_y = 560
        # Blitting to screen
        screen.blit(text, [text_x, text_y])

        # Text Box 6 - Easter Egg Hint
        text = fontInit.render("Easter Egg Hint: Press Spacebar after you see your candidate for some fun :)", True, White)
        text_rect = text.get_rect()
        # Centering Text
        text_x = 560 - text_rect.width / 2
        text_y = 500
        # Blitting to screen
        screen.blit(text, [text_x, text_y])     

        pygame.display.flip()
#---------------------------------------------------------------------  

#---------------------------------------------------------------------  
# Main Game Function *************************************************      
#---------------------------------------------------------------------
def playGame(screen, gameOver, forceQuit):
    # Declaring local variables
    clickToQuit = True
    playCount = 1            # Prevents sound looping

    # Font Styling
    fontInit = pygame.font.Font(None, 36)
    fontHeader = pygame.font.Font(None, 75)
    fontFooter = pygame.font.Font(None, 120)
    clock = pygame.time.Clock()

    # Initializing political score
    score = 0       # 0 = Moderate, Positive = Conservative, Negative = Liberal

    # Loading audio files
    bangbang = pygame.mixer.Sound("zBang.ogg")
    kasich = pygame.mixer.Sound("zKasich.ogg")
    clinton = pygame.mixer.Sound("zClinton.ogg")
    sanders = pygame.mixer.Sound("zSanders.ogg")
    trump = pygame.mixer.Sound("zTrump.ogg")
    cruz = pygame.mixer.Sound("zCruz.ogg")    
    johnson = pygame.mixer.Sound("zJohnson.ogg")
    # Loading images
    # Candidate profile pictures
    Cruz = pygame.image.load('presCruz.png').convert()
    Trump = pygame.image.load('presTrump.png').convert()
    Johnson = pygame.image.load('presJohnson.png').convert()
    Kasich = pygame.image.load('presKasich.png').convert()
    Clinton = pygame.image.load('presClinton.png').convert()
    Sanders = pygame.image.load('presSanders.png').convert()
    # Background images
    backgroundInit = pygame.image.load('zBackground1.png').convert()
    backgroundEnd = pygame.image.load('zBackground2.png').convert()
    # Q1-Q12 represent the different questions that the user has a choice of selecting
    q1 = pygame.image.load('q1.png').convert()
    q2 = pygame.image.load('q2.png').convert()
    q3 = pygame.image.load('q3.png').convert()
    q4 = pygame.image.load('q4.png').convert()
    q5 = pygame.image.load('q5.png').convert()
    q6 = pygame.image.load('q6.png').convert()
    q7 = pygame.image.load('q7.png').convert()
    q8 = pygame.image.load('q8.png').convert()
    q9 = pygame.image.load('q9.png').convert()
    q10 = pygame.image.load('q10.png').convert()
    q11 = pygame.image.load('q11.png').convert()
    q12 = pygame.image.load('q12.png').convert()

    block_list = pygame.sprite.Group()
    sprites = pygame.sprite.Group()
    # Create an object for the user's cursor (also assigns crosshair.png as image)
    user = Target()
    sprites.add(user)


    while not gameOver and not forceQuit:
        # Loop that re-iterates for every "event"
        for event in pygame.event.get(): 
            # If program is closed/exited
            if event.type == pygame.QUIT: 
                gameOver = True
                forceQuit = True

        # This is the normal game loop; assuming user has not exited or clicked finish
        if not gameOver:
            # Blits the background image to the top left position of the screen
            screen.blit(backgroundInit, (0,0))
            # Blitz each statement in its desired position; these are the questions to be selected by user
            screen.blit(q1, (60,5))
            screen.blit(q2, (430,5))
            screen.blit(q3, (820,5))
            screen.blit(q4, (60,140))
            screen.blit(q5, (430,140))
            screen.blit(q6, (820,140))      
            screen.blit(q7, (60,275))
            screen.blit(q8, (430,275))
            screen.blit(q9, (820,275))
            screen.blit(q10, (60,410))
            screen.blit(q11, (430,410))
            screen.blit(q12, (820,410))

            # Get the current mouse position; return coordinates as a list
            pos = pygame.mouse.get_pos()
            # Gets x and y out of the pos[] list; Sets the object to the mouse location (pos)
            user.rect.x = pos[0]
            user.rect.x -= user.image.get_width() / 2
            # ^^Uses get_width function to center image on mouse position
            user.rect.y = pos[1]
            user.rect.y -= user.image.get_height() / 2

            # If-Elif statement that finds user position when they click something
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Abortion
                if pos[0] >= 60 and pos[0] <= 305 and pos[1] < 125:
                    score -= 2
                    sleep(0.2)  
                    bangbang.play()    
                # Corporations             
                elif pos[0] >= 60 and pos[0] <= 305 and pos[1] > 130 and pos[1] < 265:
                    score -= 2
                    sleep(0.2)
                    bangbang.play()  
                # Defense Spending
                elif pos[0] >= 60 and pos[0] <= 305 and pos[1] > 270 and pos[1] < 405:
                    score -= 2
                    sleep(0.2)
                    bangbang.play() 
                # Free College
                elif pos[0] >= 430 and pos[0] <= 680 and pos[1] < 125:
                    score -= 2
                    sleep(0.2)
                    bangbang.play() 
                # Socialism
                elif pos[0] >= 430 and pos[0] <= 680 and pos[1] > 130 and pos[1] < 265:
                    score += 2
                    sleep(0.2)
                    bangbang.play() 
                # Education Reform
                elif pos[0] >= 430 and pos[0] <= 680 and pos[1] > 270 and pos[1] < 395:
                    score -= 1
                    sleep(0.2)
                    bangbang.play() 
                # Healthcare
                elif pos[0] > 800 and pos[1] < 125:
                    score -= 2
                    sleep(0.2)
                    bangbang.play()                                                           
                # Terrorism
                elif pos[0] > 800 and pos[1] > 130 and pos[1] < 265:
                    score += 1
                    sleep(0.2)
                    bangbang.play() 
                # Immigration
                elif pos[0] > 800 and pos[1] > 270 and pos[1] < 395:
                    score += 2
                    sleep(0.2)
                    bangbang.play()                  
                # Bottom Three Issues (Stereotypical Conservative ideologies)
                elif pos[1] > 410 and pos[1] < 535:
                    score += 2
                    sleep(0.2)
                    bangbang.play()  
                # Trump
                elif pos[0] > 2 and pos[0] < 125 and pos[1] > 545:
                    score -= 2
                    sleep(0.2)
                    bangbang.play() 
                # Cruz    
                elif pos[0] > 135 and pos[0] < 250 and pos[1] > 545:
                    score -= 2
                    sleep(0.2)
                    bangbang.play() 
                # Johnson
                elif pos[0] > 260 and pos[0] < 365 and pos[1] > 545:
                    score -= 1
                    sleep(0.2)
                    bangbang.play()  
                # Kasich     
                elif pos[0] > 380 and pos[0] < 495 and pos[1] > 545:
                    score -= 1
                    sleep(0.2)
                    bangbang.play()                                    
                # Clinton
                elif pos[0] > 505 and pos[0] < 620 and pos[1] > 545:
                    score += 2
                    sleep(0.2)
                    bangbang.play()             
                # Bernie                  
                elif pos[0] < 740 and pos[0] > 630 and pos[1] > 545:
                    score += 3
                    sleep(0.2)
                    bangbang.play()
                # User needs help
                elif pos[0] > 750 and pos[0] < 920 and pos[1] > 545:    
                    webbrowser.open_new_tab("http://www.cgfixit.com/help.html")
                    sleep(0.1)       
                # User is finished    
                elif pos[0] > 930 and pos[1] > 545:    
                    gameOver = True      
                    sleep(0.2)    
            # Draw / Display Sprite
            sprites.draw(screen)
            # Update Screen
            pygame.display.update()

        # This is executed after the user clicks the Finish button
        if gameOver and not forceQuit:

            # while user hasn't clicked anything yet:
            while clickToQuit:
                # Get the current mouse position; return coordinates as a list
                pos = pygame.mouse.get_pos()
                # Gets x and y out of the pos[] list; Sets the object to the mouse location (pos)
                user.rect.x = pos[0]
                user.rect.x -= user.image.get_width() / 2
                # ^^Uses get_width function to center image on mouse position
                user.rect.y = pos[1]
                user.rect.y -= user.image.get_height() / 2                

                # Final loop for quitting game; Initiated by user clicking mouse or hitting space bar
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        # If user quits, game over
                        clickToQuit = False
                    elif event.type == pygame.MOUSEBUTTONDOWN and pos[0] > 890 and pos[1] < 60:
                        # If user clicks learn more(top right corner), browser opens
                        viewWebsite(winner)            
                    elif event.type == pygame.MOUSEBUTTONDOWN and pos[0] < 120 and pos[1] < 115:
                        # If user clicks trump icon(top left corner), Trump-Themed mini-game opens
                        og.mini_game()                                                                                  
                    elif event.type == pygame.MOUSEBUTTONDOWN and pos[1] > 590:
                        # Calls logs module; creates new log entry and/or allows logs to be viewed
                        logEntry.main_log(winner)
                    elif event.type == pygame.KEYDOWN:
                        # Calls Trump-Themed mini-game
                        og.mini_game()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        clickToQuit = False                          

                # Clears screen and blits new background image
                screen.blit(backgroundEnd, (0,0))

                # Prints Header
                textHeader = fontHeader.render("You Side With..", True, Blue)
                text_rect = textHeader.get_rect()
                text_x = 560  - text_rect.width / 2
                text_y = screen.get_height() / 30 - text_rect.height / 30
                # Blits header to top of screen
                screen.blit(textHeader, [text_x, text_y])

                # Determines winning candidate
                winner = determineWinner(score)

                # Prints Footer; winning candidate's name is displayed
                # Stores string variable winner as a text object named textWinner
                textWinner = fontFooter.render(format(winner), True, Black)
                textWinner_rect = textWinner.get_rect()
                winnerX = 560 - textWinner_rect.width / 2
                winnerY = 509
                # Blits the name of the winning candidate
                screen.blit(textWinner, [winnerX, winnerY])

                # Blits picture of candidate
                if winner == "Ted Cruz":
                    pres_rect = Cruz.get_rect()
                    presX = screen.get_width() / 2  - pres_rect.width / 2
                    presY = screen.get_height() / 2 - pres_rect.height / 2
                    screen.blit(Cruz, [presX,presY])
                    if playCount < 2:
                        cruz.play()
                        playCount += 1

                elif winner == "Donald Trump":                  
                    pres_rect = Trump.get_rect()
                    presX = screen.get_width() / 2  - pres_rect.width / 2
                    presY = screen.get_height() / 2 - pres_rect.height / 2
                    screen.blit(Trump, [presX,presY])
                    if playCount < 2:
                        trump.play()
                        playCount += 1

                elif winner == "Gary Johnson":                   
                    pres_rect = Johnson.get_rect()
                    presX = screen.get_width() / 2  - pres_rect.width / 2
                    presY = screen.get_height() / 2 - pres_rect.height / 2
                    screen.blit(Johnson, [presX,presY])
                    if playCount < 2:
                        johnson.play()
                        playCount += 1     

                elif winner == "John Kasich":                  
                    pres_rect = Kasich.get_rect()
                    presX = screen.get_width() / 2  - pres_rect.width / 2
                    presY = screen.get_height() / 2 - pres_rect.height / 2
                    screen.blit(Kasich, [presX,presY])
                    if playCount < 2:
                        kasich.play()
                        playCount += 1

                elif winner == "Hillary Clinton":                  
                    pres_rect = Clinton.get_rect()
                    presX = screen.get_width() / 2  - pres_rect.width / 2
                    presY = screen.get_height() / 2 - pres_rect.height / 2
                    screen.blit(Clinton, [presX,presY])
                    if playCount < 2:
                        clinton.play()
                        playCount += 1                    

                elif winner == "Bernie Sanders":                 
                    pres_rect = Sanders.get_rect()
                    presX = screen.get_width() / 2  - pres_rect.width / 2
                    presY = screen.get_height() / 2 - pres_rect.height / 2
                    screen.blit(Sanders, [presX,presY])
                    if playCount < 2:
                        sanders.play()
                        playCount += 1
                # Draw / Display Sprite
                sprites.draw(screen)
                # Final surface update
                pygame.display.flip()
        # Limits CPu Usage; 60 Frames-Per-Second
        clock.tick(60)
#---------------------------------------------------------------------  

#---------------------------------------------------------------------  
# Determine Winner Function ******************************************      
#---------------------------------------------------------------------
def determineWinner(score):
    # Returns candidate that best matches user's beliefs

    # Cruz
    if score > 10:
        return "Ted Cruz"
    # Trump
    elif score >= 5 and score <= 10:
        return "Donald Trump"
    # Kasich
    elif score >= 2 and score <= 4:
        return "John Kasich"
    # Johnson
    elif score >= 0 and score <= 1:
        return "Gary Johnson"   
    # Clinton
    elif score <= -1 and score >= -3:
        return "Hillary Clinton"
    # Sanders
    else:      
        return "Bernie Sanders"
#---------------------------------------------------------------------      

#---------------------------------------------------------------------  
# View Website Function **********************************************   
#---------------------------------------------------------------------
def viewWebsite(winner):
    # Opens browser to that candidate's website
    if winner == "Ted Cruz":
        webbrowser.open_new_tab("https://www.tedcruz.org/home/")
    elif winner == "Donald Trump":
        webbrowser.open_new_tab("https://www.donaldjtrump.com/")
    elif winner == "John Kasich":
        webbrowser.open_new_tab("https://www.johnkasich.com/issues/")
    elif winner == "Gary Johnson":
        webbrowser.open_new_tab("https://garyjohnson2016.com/")  
    elif winner == "Hillary Clinton":
        webbrowser.open_new_tab("https://www.hillaryclinton.com/")
    elif winner == "Bernie Sanders":
        webbrowser.open_new_tab("https://berniesanders.com/about/")        
#---------------------------------------------------------------------  

#---------------------------------------------------------------------  
# Main game function *************************************************   
#---------------------------------------------------------------------
def main():
    # Declaring local variables
    forceQuit = False             # Differentiates between quitting the program and quitting the main game   
    clickToQuit = True            # Final quit sentinel; when user is viewing their Candidate
    gameOver = False              # General Purpose sentinel for various loops in the intro/main game

    # Initializing pygame and configuring screen size
    pygame.init()
    screen_width = 1120
    screen_height = 640
    screen = pygame.display.set_mode([screen_width, screen_height])
    # Sets title for game
    pygame.display.set_caption("Pick-a-Politician!")
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # Initializing pygame music mixer module and loading/playing initial sound file
    pygame.mixer.init()
    # Declaring Sound Objects
    introSong = pygame.mixer.Sound("zInit.ogg")
    introSong.play()      # Plays theme song upon execution
    
    #-----------------------------------
    # Initial Splash Screen: ***********
    #-----------------------------------
    splashScreen(screen)
    #-----------------------------------
    # Instructions screen: *************
    #-----------------------------------
    gameOver, forceQuit = instructionScreen(screen)   
    #-----------------------------------
    # Game Loop: ***********************
    #-----------------------------------
    playGame(screen, gameOver, forceQuit)
    #-----------------------------------
    # Quitting Game ********************
    pygame.quit()   
#---------------------------------------------------------------------
main()
