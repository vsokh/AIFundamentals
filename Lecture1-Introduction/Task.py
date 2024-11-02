def play_rock_paper_scissors(player_choice, comp_choice):
    valid_choices = {'rock', 'paper', 'scissors'}
    if player_choice == comp_choice:
      return 'Tie'

    if player_choice == 'rock':
      if comp_choice == 'scissors':
        return 'Player 1 wins'
      if comp_choice == 'paper':
        return 'Comp wins'

    if player_choice == 'paper':
      if comp_choice == 'rock':
        return 'Player 1 wins'
      if comp_choice == 'scissors':
        return 'Comp wins'

    if player_choice == 'scissors':
      if comp_choice == 'rock':
        return 'Comp wins'
      if comp_choice == 'paper':
        return 'Player 1 wins'
