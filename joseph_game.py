def next(players, i):
  """Find the next alive player."""
  for shift in range(1, len(players)):
    if players[(i+shift)%len(players)][1]:
      return players[(i+shift)%len(players)][0]

def joesph_game(n):
  """Find the winner of the Joesph game."""
  players = [[i,1] for i in range(n)]
  #print(players)
  active_player = 0
  while sum([player[1] for player in players]) > 1:
    players[next(players, active_player)][1] = 0
    #print(players)
    active_player = next(players, active_player)
  #print(players)
  winner = [player[0] for player in players if player[1]][0]
  #print("There were {} starting players, and player {} won!".format(n, winner))
  return winner

for n in range(1, 33):
  print(n, joesph_game(n))
