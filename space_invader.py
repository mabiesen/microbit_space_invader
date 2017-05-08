from microbit import *
import random


# coords given as x
player_coord = 0

# coords given as x y
enemy_coords = [2,0]

# Leds can actually be termed on in a dimmed fashion using numbers 1-8
# In this code, we only want the leds to be on (high) or off (low)
high = 9
low = 0

# Speed is the speed of the enemy which increments after each kill
speed = 1

# hit_count, also incrememnts after each kill
hit_count = 0

# when the player fires a missile by tilting the microbit forward
def missile():
  global enemy_coords
  global enemy_start_time
  global speed
  global hit_count
  ctr = 0
  while ctr < 4:
    display.set_pixel(player_coord,ctr,high)
    ctr = ctr + 1
  sleep(500)
  display.clear()
  if enemy_coords[0] == player_coord:
    enemy_coords[1] = 0
    enemy_coords[0] = random.randint(0,4)
    enemy_start_time = running_time()
    speed = speed + 1
    hit_count = hit_count + 1
  display.set_pixel(enemy_coords[0],enemy_coords[1],high)
  display.set_pixel(player_coord, 4,high)
    
  
# Moves the enemy down an led, checks to see if player or backwall is hit   
def move_enemy():
  global enemy_coords
  global enemy_start_time
  if enemy_coords[1] == 3 and player_coord == enemy_coords[0]:
      game_over()
  elif enemy_coords[1] == 4:
    game_over()
  else:
    display.set_pixel(enemy_coords[0],enemy_coords[1],low)    # Turn off the led where "enemy was"
    enemy_coords[1] = enemy_coords[1] + 1                     # Change enemy y coordinate to 1 led lower
    display.set_pixel(enemy_coords[0],enemy_coords[1],high)   # Turn on led at enemy current coordinates
    enemy_start_time = running_time()

# End game alers displayed, game is reset
def game_over():
  display.scroll("game over")
  display.scroll("hit count")
  display.scroll(str(hit_count))
  reset()

# Waits for player to start game
# UNUSED.  Because default scroll speed is slow, I commented out the call to this function
def start_game():
  display.scroll("press a to start")
  x = "no"
  while x != "pressed":
    if button_a.was_pressed():
      x = "pressed"
  display.scroll("3")
  display.scroll("2")
  display.scroll("1")

# Move the player left or right based on button press
def move_player(direction):
  global player_coord
  if player_coord == 4 and direction == 1:
    return
  if player_coord == 0 and direction == -1:
    return
  display.set_pixel(player_coord,4,low)
  player_coord = player_coord + direction
  display.set_pixel(player_coord,4,high)

# Provide the initial setup for the board
def set_board():
  display.set_pixel(player_coord,4,high)
  display.set_pixel(enemy_coords[0],enemy_coords[1],high)
###################################################################################################################################

#start_game()
set_board()
enemy_start_time = running_time()

while True:
  current_time = running_time()
  time_diff = current_time - enemy_start_time
  if time_diff > 1500 - (speed * 50):
    move_enemy()
  y = accelerometer.get_y()
  if y < -200:
    missile()
  if button_a.was_pressed():
    move_player(-1)
  if button_b.was_pressed():
    move_player(1)
