#PythonicXsAndOs
This is a simulation of the game X's and O's on the command line, programed in python
Currently this program only allows two people too play X's and O's

To run the game run the code bellow


python Play.py

Plan:
- Modify the game engine to be able to undo, redo move export, and import games 
Next Steps:
- Store each placement for the ability to undo a placement
    I can make a list and store the order of the moves with the person that did them
- export saved games using JSON
    Store that list as JSON
- replay saved games
    Have commands to open up JSON files with game saves
- CPU Mode aka neural network
    No clue how to do this currently
    google tensorflow tutorials
- Have multiplayer over a network with lobbies
  do this first on command line
- build a web GUI
  have multiplayer and stuff but with a server and a website
- Use Graphics library and render this using images
    Not a fan of python graphics libraries aka need to do more research
- All the same stuff but with Checkers

How the placement works

[0,0] [0,1]

[1,0] [1,1]


Issues:
  top bottom returns an error
  one should be able to type in anything they want and get a proper error
