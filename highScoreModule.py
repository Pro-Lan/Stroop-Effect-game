import pygame


def updateHighScores(userScore, screen):
    """gets the users name and adds their score to the highScore text file"""
    pygame.init()
    # defines what keys are allowed for the user's name
    permittedLetters = "abcdefghijklmnopqrstuvwxyz"
    userName = ""

    # prints the user's score to the screen and asks for their name
    endScreenFont = pygame.font.SysFont("ariel", 50)
    endScreenLine1 = endScreenFont.render("You scored: " + str(userScore), True, (0, 25, 0), (255, 255, 255))
    endScreenLine2 = endScreenFont.render("Please enter your name: ", True, (25, 0, 0), (255, 255, 255))
    endScreenLine1 = endScreenLine1.convert()
    endScreenLine2 = endScreenLine2.convert()
    screen.blit(endScreenLine1, (180, 100))
    screen.blit(endScreenLine2, (93, 150))
    pygame.display.update()

    userIsEnteringName = True
    while userIsEnteringName:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if pygame.key.name(event.key) in permittedLetters:
                    if pygame.key.get_mods() == 1:
                        userName += pygame.key.name(event.key).upper()
                    else:
                        userName += pygame.key.name(event.key)
                    displayUserInputOnScreen(userName, endScreenFont, screen)
                elif pygame.key.name(event.key) == "return":
                    if not (userName == ""):
                        userIsEnteringName = False
                elif pygame.key.name(event.key) == "backspace":
                    userName = userName[:len(userName) - 1]
                    displayUserInputOnScreen(userName, endScreenFont, screen)
            elif event.type == pygame.QUIT:
                quit()

    addUserScoreToTextFile(userScore, userName)


def addUserScoreToTextFile(userScore, userName):
    """adds the user's most recent score to the high score text file"""
    highScoreFile = open("HighScores.txt", "a+")
    highScoreFile.write(userName + "\n")
    highScoreFile.write(str(userScore) + "\n")
    highScoreFile.close()


def displayHighScores(screen, background):
    """displays the top 5 high scores from the text file on the screen"""
    highScoresRaw = []
    highScores = []
    highScoreFile = open("HighScores.txt", "r")
    for line in highScoreFile:
        highScoresRaw.append(line.rstrip())
    for i in range(0, len(highScoresRaw), 2):
        highScores.append((int(highScoresRaw[i + 1]), highScoresRaw[i]))

    highScores.sort(reverse=True)
    background.fill((153, 255, 153))
    background = background.convert()
    screen.blit(background, (0, 0))
    highScoreFont = pygame.font.SysFont("ariel", 50)
    title = highScoreFont.render("High Scores: ", True, (0, 0, 255))
    screen.blit(title, (100, 0))
    scoreText = []
    userNamesText = []
    nameColour = (6, 114, 120)

    for j in range(0, len(highScores)):
        userNamesText.append(highScoreFont.render(highScores[j][1], True, nameColour))
        screen.blit(userNamesText[j], (100, 100 + j * 100))
        scoreText.append(highScoreFont.render(str(highScores[j][0]), True, nameColour))
        screen.blit(scoreText[j], (400, 100 + j * 100))

    pygame.display.update()

    userIsLookingAtScores = True
    while userIsLookingAtScores:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                userIsLookingAtScores = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                userIsLookingAtScores = False


def displayUserInputOnScreen(userName, font, screen):
    """displays the user's input so far to the screen"""
    resetbox = pygame.Surface((600, 37))
    resetbox.fill((255, 255, 255))
    resetbox.convert()
    screen.blit(resetbox, (0, 200))

    userInputText = font.render(userName, True, (0, 0, 25), (255, 255, 255))
    userInputText.convert()
    screen.blit(userInputText, (round((600 - userInputText.get_width()) / 2), 200))
    pygame.display.update()
