I need to modularize my code better than I already have it
I need to group all my functions together
List all my functions
  draw_out_board
  print_out_board
  decide_who_goes_first
  player_turn
  board_full
  check_winner
  play_game
Ideas on groups
  user_input
    get_user_input
  game_engine
    #store the past moves
    decide_who_goes_first
    board_full
    check_winner
    cycle_through_turns
  pring_game_information
    draw_out_board
    print_out_board
