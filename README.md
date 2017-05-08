# Microbit Micropython Space Invader


I looked for a space invaders project in microbit in micropython for about 15 minutes and couldn't find anything!  Some folks made this game in other languages like Microsoft Blocks, but being a Python fanatic I wanted a python version. So I made my own : )

### Game Play

The player is represented by a single dot on the bottom of the screen, the enemy is a single dot on top of the screen that slowly falls down.  The player piece is moved by pressing the "a" or "b" buttons (a for left, b for right).

The goal of the game is to shoot down the enemy before it touches the player or the back end of the board, to do this you tilt the microbit forward.  Each time an enemy is killed, the speed of the game increases (my personal best is 18).

In the event the enemy hits your player or the back of the board, the game is over and your score is displayed.  Then the game is reset to play again.



### Lessons Learned

Initially I wanted to use the microbit's touch pads to control the player.  This proved to be inaccurate; often the touch pads would not register or would register more than one touch (because there is only an is_touched function for the touch pads and no was_touched, which means you can only determine if the player is currently touching the pad).
