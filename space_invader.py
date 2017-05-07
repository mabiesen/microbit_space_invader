
# coords given as x
player_coord = 0

# coords given as x y
enemy_coords = [0,2]

high = 9
low = 0

# when the player fires a missile
def missile():
  ctr = 0
  while ctr < 5:
    set_pixel(player_coord,x,high)
    ctr = ctr + 1
    
def move_enemy():
  global enemy_coords
  if enemy_coords[1] == 3 and player_coord == enemy_coords[0]:
      game_over()
  elif enemy_coords[1] == 4:
    game_over()
  else:
    set_pixel(enemy_coords[0],enemy_coords[1],low)
    enemy_coords[1] = enemy_coords[1] + 1
  
      
def game_over():
  display.scroll("game over")
  reset()
  
def start_game():
  display.scroll("press a to start")
  x = "no"
  while x != "pressed":
    if button_a.was_pressed():
      x = "pressed"
  display.scroll("3")
  display.scroll("2")
  display.scroll("1")


