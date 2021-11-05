def Snake_Area_Filling (n):
    game_screen= n*n
    Length = 1 
    food= 0
    while Length < game_screen:
        food = food+ 1
        Length = Length *2
    else : 
        return food-1

print(Snake_Area_Filling(6))