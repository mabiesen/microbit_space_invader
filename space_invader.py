
# coords given as x
player_coord = 0

# coords given as x y
enemy_coords = [0,2]

# when the player fires a missile
def missile():
  ctr = 0
  while ctr < 5:
    set_pixel(player_coord,x,9)
    ctr = ctr + 1
    
def move_enemy():
  global enemy_coords
  if enemy_coords[1] == 3:
    if player_coord == enemy_coords[0]:
      game_over()
  elif enemy_coords[1] == 4:
    game_over()
      
def game_over():
  display.scroll("game over")
  
def start_game():


