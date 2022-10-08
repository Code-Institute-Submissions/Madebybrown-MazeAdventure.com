# Maze Adventure
**The Maze Adventure!** is a python terminal game, the user can emerse themselves in this textbased short story and try to find a way out of the maze, but beware, something may be lurking around the corner.

[Live Site - Maze Adventure](https://mazeadventure.herokuapp.com/)

[Repository - Maze Adventure](https://github.com/Madebybrown/MazeAdventure.com)

![amiresponsive](assets/images/amiresponsive.png)

## How to play
The player has the ability to choose what actions they want to take in every scene, they have the options to move in different directions and to flee or fight. don't forget to take a look around, you may find a hidden weapon if you go where you shouldnt.

## Features
### Existing Features

**Welcome Message**
- Welcomes the player and sets the scenery of the story.
- Asks for the players name.
![welcome](assets/images/featureone.png)

**Options!**
- Presents the player with up to four options.
![options](assets/images/featuretwo.png)

**Restart Game!**
- Promts the player to restart the game and play again if the win or die.
![restart](assets/images/featurethree.png)

**Invalid Option!**
- Tells the player that the option they've chosen was invalid.
![invalid](assets/images/featurefour.png)

### Future Features
- Expanding the storyline
- Placing more weapons around the game
- Using riddles to escape rooms

## Testing
I have manually tested the project by:
- Giving invalid inputs
- Tested with my local terminal and the Code Institute terminal
- Letting other people play the game with the intention to "brake" it

## Bugs
### Solved bugs
- In the beginning when I wrote the code and ran the progrem, the terminal got spammed with print messages, I relized I missed using a "Else statement" in the "While loop".

### Reamining bugs
- No known bugs!

Validator

## Deployment
The project was deployd using Heroku.
 - Steps for deployment:
    - First, when on the Heroku dashboard, click new up to your right hand side, this will toggle a drop down.
![dashboardnew](assets/images/dashboardnew.png)
    - Click on "Create new app", this will take you to a new page.
![createnewapp](assets/images/createnewapp.png)
    - Here you choose your app name, your region and then you click "Create app" down to the left hand side, this will take you to a new page.
![namecountry](assets/images/namecountry.png)
    - On this page you first click on the settings tab.
![settings](assets/images/settings.png)
    - Here you scroll down until you see the button with "Reveal Config Vars" on it, click it!
![configvars](assets/images/configvars.png)
    - Write PORT and 8000 and then press "Add". 
![portconfig](assets/images/portconfig.png)
    - Scroll down to Buildpacks, and click it.
![buildpacks](assets/images/buildpacks.png)
    - Click python to check it and then save changes, click add buildpack again.
![pythonpack](assets/images/pythonpack.png)
    - Now scroll up to the top of the page and press the "Deploy" tab and then press github.
![deploygithub](assets/images/deploygithub.png)
    - Search for the repository you want to deploy.
![repository](assets/images/repository.png)
    - Press connect.
![connect](assets/images/connect.png)
    - Scroll down until you find "Enable Automatic Deploys" and "Deploy Branch", press them and wait while your app is building.
![deploy](assets/images/deploy.png)
    - Building app
![loading](assets/images/loading.png)
    - App build is finished
![finished](assets/images/finished.png)

## Credits
- Deployment Terminal - Code Institute