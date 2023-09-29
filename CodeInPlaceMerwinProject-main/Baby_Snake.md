# Baby Snake Game

This is a simplified version of the classic Atari game of Snake, where you control a snake-like creature on a canvas. Your objective is to move the player
(represented by a blue rectangle) to reach the goal (represented by a red rectangle). The player and the goal are both 20 pixels by 20 pixels in size.

## Game Mechanics

- The player moves in steps of 20 pixels in the directions left, right, up, or down.
- You can control the player's direction using the arrow keys on your keyboard.
- The goal randomly moves to a new location on the canvas whenever the player reaches it.
- If the player goes out of bounds and hits the canvas boundaries, the game is over.

Let's take a closer look at the code for the Baby Snake Game:

```python
# Import necessary modules
from graphics import Canvas
import time
import random

# Define constants
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
SIZE = 20
DELAY = 0.1

# Define global variables
direction = 'Right'

def main():
    global direction
    
    # Create a canvas object and initialize player and goal rectangles
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    player = canvas.create_rectangle(10, 10, SIZE, SIZE, 'blue')
    goal = canvas.create_rectangle(360, 360, 360 + SIZE, 360 + SIZE, 'red')
    
    while True:
        # Handle key press events
        handle_key_press(canvas)
        
        # Update the world based on player movement
        update_world(canvas, player, goal)
        
        # Pause the program for a short duration
        time.sleep(DELAY)

def handle_key_press(canvas):
    # Get the last key press from the canvas
    key = canvas.get_last_key_press()
    
    # Update direction based on the key pressed
    if key == 'ArrowLeft':
        direction = 'Left'
    elif key == 'ArrowRight':
        direction = 'Right'
    elif key == 'ArrowUp':
        direction = 'Up'
    elif key == 'ArrowDown':
        direction = 'Down'

def update_world(canvas, player, goal):
    # Move the player based on the current direction
    if direction == 'Right':
        canvas.move(player, SIZE, 0)
    elif direction == 'Left':
        canvas.move(player, -SIZE, 0)
    elif direction == 'Up':
        canvas.move(player, 0, -SIZE)
    elif direction == 'Down':
        canvas.move(player, 0, SIZE)
    
    # Check if the player reaches the goal, and move the goal to a random position
    if (canvas.get_left_x(player) == canvas.get_left_x(goal) and
        canvas.get_top_y(player) == canvas.get_top_y(goal)):
        canvas.move(goal, random.randint(0, CANVAS_WIDTH // SIZE) * SIZE,
                    random.randint(0, CANVAS_HEIGHT // SIZE) * SIZE)
    
    # Check if the player goes out of bounds and end the game
    player_left_x = canvas.get_left_x(player)
    player_top_y = canvas.get_top_y(player)
    player_right_x = player_left_x + SIZE
    player_bottom_y = player_top_y + SIZE
    
    if (player_left_x < 0 or player_right_x > CANVAS_WIDTH or
        player_top_y < 0 or player_bottom_y > CANVAS_HEIGHT):
        print('Game over!')
        exit()
        
if __name__ == '__main__':
    main()
```

To play the Baby Snake Game, follow these steps:

1. Make sure you have Python installed on your system.
2. Save the above code in a file named `main.py`.
3. Open a terminal or command prompt and navigate to the directory where you saved `main.py`.
4. Run the following command to start the game:

   ```
   python main.py
   ```

5. Use the arrow keys to control the player and try to reach the goal.
6. Have fun playing the Baby Snake Game!

## Explanation of the Python code

The code is divided into several parts to perform different tasks. Let's go through each part and understand what it does.

### Imports and Constants

The code begins with importing the necessary modules and defining some constants. 

```python
from graphics import Canvas
import time
import random

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
SIZE = 20
DELAY = 0.1
```

The `graphics` module is imported to create and manipulate graphical elements on a canvas. The `time` module is imported to pause the program for a short duration. The `random` module is imported to generate random numbers for the goal's position.

The `CANVAS_WIDTH` and `CANVAS_HEIGHT` constants define the dimensions of the canvas. The `SIZE` constant defines the size of the player and goal rectangles. The `DELAY` constant defines the time delay between each update of the game world.

### Global Variables

The code defines a global variable `direction` to keep track of the player's direction. The initial direction is set to `'Right'`.

```python
direction = 'Right'
```

### The `main` Function

The `main` function is the entry point of the game. It creates a canvas object, initializes the player and goal rectangles, and starts the game loop.

```python
def main():
    global direction
    
    # Create a canvas object and initialize player and goal rectangles
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    player = canvas.create_rectangle(10, 10, SIZE, SIZE, 'blue')
    goal = canvas.create_rectangle(360, 360, 360 + SIZE, 360 + SIZE, 'red')
    
    while True:
        # Handle key press events
        handle_key_press(canvas)
        
        # Update the world based on player movement
        update_world(canvas, player, goal)
        
        # Pause the program for a short duration
        time.sleep(DELAY)
```

The `global` statement is used to indicate that the `direction` variable being accessed inside the function is the same global variable defined earlier. This allows the function to modify the `direction` variable.

Inside the loop, the `handle_key_press` function is called to handle key press events. Then, the `update_world` function is called to update the game world based on the player's movement. Finally, the program pauses for a short duration using `time.sleep` to control the speed of the game.

### The `handle_key_press` Function

The `handle_key_press` function is responsible for updating the player's direction based on the key pressed.

```python
def handle_key_press(canvas):
    # Get the last key press from the canvas
    key = canvas.get_last_key_press()
    
    # Update direction based on the key pressed
    if key == 'ArrowLeft':
        direction = 'Left'
    elif key == 'ArrowRight':
        direction = 'Right'
    elif key == 'ArrowUp':
        direction = 'Up'
    elif key == 'ArrowDown':
        direction = 'Down'
```

The function first gets the last key pressed using the `get_last_key_press` method of the canvas object.

Then, it updates the `direction` variable based on the key pressed. If the left arrow key is pressed, the `direction` is updated to `'Left'`. If the right arrow key is pressed, the `direction` is updated to `'Right'`. Similarly, for the up and down arrow keys.

### The `update_world` Function

The `update_world` function is responsible for updating the game world based on the player's movement.

```python
def update_world(canvas, player, goal):
    # Move the player based on the current direction
    if direction == 'Right':
        canvas.move(player, SIZE, 0)
    elif direction == 'Left':
        canvas.move(player, -SIZE, 0)
    elif direction == 'Up':
        canvas.move(player, 0, -SIZE)
    elif direction == 'Down':
        canvas.move(player, 0, SIZE)
    
    # Check if the player reaches the goal, and move the goal to a random position
    if (canvas.get_left_x(player) == canvas.get_left_x(goal) and
        canvas.get_top_y(player) == canvas.get_top_y(goal)):
        canvas.move(goal, random.randint(0, CANVAS_WIDTH // SIZE

    ) * SIZE,
                    random.randint(0, CANVAS_HEIGHT // SIZE) * SIZE)
    
    # Check if the player goes out of bounds and end the game
    player_left_x = canvas.get_left_x(player)
    player_top_y = canvas.get_top_y(player)
    player_right_x = player_left_x + SIZE
    player_bottom_y = player_top_y + SIZE
    
    if (player_left_x < 0 or player_right_x > CANVAS_WIDTH or
        player_top_y < 0 or player_bottom_y > CANVAS_HEIGHT):
        print('Game over!')
        exit()
```

The function first moves the player rectangle based on the current direction. If the direction is `'Right'`, the `canvas.move` method is called to move the player rectangle to the right. Similarly, for other directions.

Next, it checks if the player has reached the goal. If the left x-coordinate and top y-coordinate of the player are equal to the left x-coordinate and top y-coordinate of the goal, it means the player has reached the goal. In this case, the `canvas.move` method is called to move the goal rectangle to a random position within the bounds of the canvas.

Then, it checks if the player has gone out of bounds. If the left x-coordinate of the player is less than 0 or the right x-coordinate of the player is greater than the canvas width or the top y-coordinate of the player is less than 0 or the bottom y-coordinate of the player is greater than the canvas height, it means the player has gone out of bounds. In this case, the game is over, and the program terminates using `exit()`.

### The `main` Execution

The following code block ensures that the `main` function is only executed when the script is run directly, not when it is imported as a module.

```python
if __name__ == '__main__':
    main()
```

This is a common practice in Python to allow modules to be both imported and executed.

That's it! You now have a detailed understanding of the Baby Snake Game code. Have fun playing the game!
https://davidmerwin.pieces.cloud/?p=45fe4994fa  
https://gist.github.com/1fd1c7274fa938f2fd3daceed31bbe88# Import necessary modules

#Snake Game
from graphics import Canvas
import time
import random

# Define constants
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
SIZE = 20
DELAY = 0.1

# Define global variables
direction = 'Right'

def main():
    global direction
    
    # Create a canvas object and initialize player and goal rectangles
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    player = canvas.create_rectangle(10, 10, SIZE, SIZE, 'blue')
    goal = canvas.create_rectangle(360, 360, 360 + SIZE, 360 + SIZE, 'red')
    
    while True:
        # Handle key press events
        handle_key_press(canvas)
        
        # Update the world based on player movement
        update_world(canvas, player, goal)
        
        # Pause the program for a short duration
        time.sleep(DELAY)

def handle_key_press(canvas):
    global direction
    
    # Get the last key press from the canvas
    key = canvas.get_last_key_press()
    
    # Update direction based on the key pressed
    if key == 'ArrowLeft':
        direction = 'Left'
    elif key == 'ArrowRight':
        direction = 'Right'
    elif key == 'ArrowUp':
        direction = 'Up'
    elif key == 'ArrowDown':
        direction = 'Down'

def update_world(canvas, player, goal):
    global direction
    
    # Move the player based on the current direction
    if direction == 'Right':
        canvas.move(player, SIZE, 0)
    elif direction == 'Left':
        canvas.move(player, -SIZE, 0)
    elif direction == 'Up':
        canvas.move(player, 0, -SIZE)
    elif direction == 'Down':
        canvas.move(player, 0, SIZE)
    
    # Check if the player reaches the goal, and move the goal to a random position
    if (canvas.get_left_x(player) == canvas.get_left_x(goal) and
        canvas.get_top_y(player) == canvas.get_top_y(goal)):
        canvas.move(goal, random.randint(0, CANVAS_WIDTH // SIZE) * SIZE,
                    random.randint(0, CANVAS_HEIGHT // SIZE) * SIZE)
    
    # Check if the player goes out of bounds and end the game
    player_left_x = canvas.get_left_x(player)
    player_top_y = canvas.get_top_y(player)
    player_right_x = player_left_x + SIZE
    player_bottom_y = player_top_y + SIZE
    
    if (player_left_x < 0 or player_right_x > CANVAS_WIDTH or
        player_top_y < 0 or player_bottom_y > CANVAS_HEIGHT):
        print('Game over!')
        exit()
        
if __name__ == '__main__':
    main()
'''
from graphics import Canvas
import time
import random

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
SIZE = 20
DELAY = 0.1

def main():
    global direction
    direction = 'Right'

    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    player = canvas.create_rectangle(0, 0, SIZE, SIZE, "blue")
    goal = canvas.create_rectangle(360, 360, 360 + SIZE, 360 + SIZE, "red")

    while True:
        handle_key_press(canvas)
        update_world(canvas, player, goal)
        time.sleep(DELAY)

def handle_key_press(canvas):
    global direction
    key = canvas.get_last_key_press()

    if key == 'ArrowLeft':
        direction = 'Left'
    elif key == 'ArrowRight':
        direction = 'Right'
    elif key == 'ArrowUp':
        direction = 'Up'
    elif key == 'ArrowDown':
        direction = 'Down'

def update_world(canvas, player, goal):
    global direction

    if direction == 'Right':
        canvas.move(player, SIZE, 0)
    elif direction == 'Left':
        canvas.move(player, -SIZE, 0)
    elif direction == 'Up':
        canvas.move(player, 0, -SIZE)
    elif direction == 'Down':
        canvas.move(player, 0, SIZE)

    if (canvas.get_left_x(player) == canvas.get_left_x(goal) and 
        canvas.get_top_y(player) == canvas.get_top_y(goal)):
        canvas.move(goal, random.randint(0, CANVAS_WIDTH // SIZE) * SIZE, 
                          random.randint(0, CANVAS_HEIGHT // SIZE) * SIZE)

    player_left_x = canvas.get_left_x(player)
    player_top_y = canvas.get_top_y(player)
    player_right_x = player_left_x + SIZE
    player_bottom_y = player_top_y + SIZE

    if (player_left_x < 0 or player_right_x > CANVAS_WIDTH or 
        player_top_y < 0 or player_bottom_y > CANVAS_HEIGHT):
        print('Game over!')
        exit(0)

if __name__ == '__main__':
    main()
'''
https://codeinplace.stanford.edu/cip3/share/zctW0g9poLtetCgpDR0L

IDE | Baby Snake

Instructions
In this assignment we are going to make a baby version of the classic Atari game of Snake. It was famously shipped on the original Apple II computers as well as Nokia phones. Here is a demo with a few extensions: Baby Snake Demo  

Milestone #1: Set up the World
Draw the following world! It has a blue square is the "player" the red square is the "goal". The player and the goal are both 20 pixels by 20 pixels. 

The player should start in the top left corner of the world. You can place the goal anywhere you like as long as its x and y values are both multiplies of 20. Here is a reasonable configuration where the goal is at (360, 360):


Keep in mind that later on, your animation loop will need to access the player and the goal variables (the values returned when you call create_rectangle). Speaking of which, it is time to animate!

Milestone #2: Animate
Each time through the animation loop you should move your player 20 pixels (this size of the player) in the direction it is traveling. The directions are either left, right, up or down. At the start the player should be traveling to the right:



A gif of the animation (which loops)

Recall the standard animation loop:
def main():
    # TODO: setup the world

    # animation loop
    while True:
        # TODO: update the world for one heartbeat

        # sleep
        time.sleep(DELAY)

Once you have completed this milestone your program only animates the player moving right. 

Milestone #3: Handle Key Press
the direction that the player is traveling can either be Left, Right, Up or Down and should be controlled by the keyboard. 

We haven't seen the keyboard in Code in Place. It works just like the mouse! At any point in a graphics program you can ask the canvas for the last key press 
key = canvas.get_last_key_press()

The key variable will then hold the name of the key which was last pressed (or None if no key has been pressed). If the name of the key is "ArrowLeft" that means the last key the user pressed was the left arrow. Here is an example of printing arrow keys:
key = canvas.get_last_key_press()
if key == 'ArrowLeft':
    print('left arrow pressed!')
if key == 'ArrowRight':
    print('right arrow pressed!')
if key == 'ArrowUp':
    print('up arrow pressed!')
if key == 'ArrowDown':
    print('down arrow pressed!')

You should process canvas.get_last_key_press() inside the animation loop. We strongly encourage you to keep a variable which stores the current direction of travel.

Milestone #4: Detecting collisions
If the player goes out of bounds, the game is over. Write code that checks for, and handles, out of bounds cases. You will likely benefit from using:
x = canvas.get_left_x(obj)
y = canvas.get_top_y(obj)
where the obj parameter can be either the player variable, or the goal variable. The return type is always an integer, so you can compare the value of say the player x and the goal x.

Milestone #5: Moving the goal
When the player hits the goal, you should randomly move the goal to a new location, anywhere on the board. Write code that detects if the user has hit the goal, and randomly places the goal in a new location. You will need to use the randint function which returns an integer in the given range:
random.randint(0, max_value)
Recall that the new x and y of the goal should be multiples of 20, otherwise it may be hard to detect if the player and the goal touch. There are many algorithms which you could come up with to get a random value which is a multiple of 20. Also recall that randint is inclusive, which means it can return 0 and it can also return max_value. 

Extensions
You did it! Congratulations, that was a huge program. If you want to keep going, awesome. Add any extension you like. Here are a few that we think are fun:
Get faster each time the player touches the goal.
Keep track of points
Add obstacles

Full Snake?
If you are feeling very adventurous you could try and implement the full game of snake. Here is a link to an online version: https://playsnake.org/. The full game of snake is a hard challenge even for a well seasoned programmer. If you do go down this path, here are a few pro tips:
Program your snake in a new project (leave this one as baby snake)
Represent your snake using a list of rectangles (where the rectangles are the shapes returned by create_rect). This will make it much easier to move your snake. You will only need to change the head and the tail.
Us the find_overlapping function to tell if you have hit yourself.

The code snippet creates a simple game where the player moves a blue rectangle on a canvas using arrow keys. The goal is to reach a red rectangle, which randomly moves to a new location when the player reaches it. If the player goes off the canvas https://davidmerwin.pieces.cloud/?p=45fe4994fa
Canvas Game: Moving Player to Reach Goal.md
Canvas Game: Moving Player to Reach Goal

Preview:

# main.py

# Import necessary modules
from graphics import Canvas
import time
import random

# Define constants
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
SIZE = 20
DELAY = 0.1

# Define global variables
direction = 'Right'

def main():
    global direction
    
    # Create a canvas object and initialize player and goal rectangles
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    player = canvas.create_rectangle(10, 10, SIZE, SIZE, 'blue')
    goal = canvas.create_rectangle(360, 360, 360 + SIZE, 360 + SIZE, 'red')
    
    while True:
        # Handle key press events
        handle_key_press(canvas)
        
        # Update the world based on player movement
        update_world(canvas, player, goal)
        
        # Pause the program for a short duration
        time.sleep(DELAY)

def handle_key_press(canvas):
    global direction
    
    # Get the last key press from the canvas
    key = canvas.get_last_key_press()
    
    # Update direction based on the key pressed
    if key == 'ArrowLeft':
        direction = 'Left'
    elif key == 'ArrowRight':
        direction = 'Right'
    elif key == 'ArrowUp':
        direction = 'Up'
    elif key == 'ArrowDown':
        direction = 'Down'

def update_world(canvas, player, goal):
    global direction
    
    # Move the player based on the current direction
    if direction == 'Right':
        canvas.move(player, SIZE, 0)
    elif direction == 'Left':
        canvas.move(player, -SIZE, 0)
    elif direction == 'Up':
        canvas.move(player, 0, -SIZE)
    elif direction == 'Down':
        canvas.move(player, 0, SIZE)
    
    # Check if the player reaches the goal, and move the goal to a random position
    if (canvas.get_left_x(player) == canvas.get_left_x(goal) and
        canvas.get_top_y(player) == canvas.get_top_y(goal)):
        canvas.move(goal, random.randint(0, CANVAS_WIDTH // SIZE) * SIZE,
                    random.randint(0, CANVAS_HEIGHT // SIZE) * SIZE)
    
    # Check if the player goes out of bounds and end the game
    player_left_x = canvas.get_left_x(player)
    player_top_y = canvas.get_top_y(player)
    player_right_x = player_left_x + SIZE
    player_bottom_y = player_top_y + SIZE
    
    if (player_left_x < 0 or player_right_x > CANVAS_WIDTH or
        player_top_y < 0 or player_bottom_y > CANVAS_HEIGHT):
        print('Game over!')
        exit()
        
if __name__ == '__main__':
    main()
Associated Context	
Type	Code Snippet ( .py )
Associated Tags	random Graphics Library pygame wxpython Canvas Arrow Left/Right Motion CANVAS_HEIGHT Arrow Right Motion update_world Player Moveing handle_key_press SIZE CANVAS_WIDTH Key Pressivation DELAY Framework: graphics Random Function time Canvas SDK Game Development tkinter-canvas tkinter turtle-graphics Time Module Game over!
💡 Smart Description	This code creates a canvas that moves the player and goal of an arrow in between two different modes. It also handles key-press events to update their worlds, with random values based on direction
The code snippet creates a simple game where the player moves a blue rectangle on a canvas using arrow keys. The goal is to reach a red rectangle, which randomly moves to a new location when the player reaches it. If the player goes off the canvas
'''
