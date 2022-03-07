grid = [['___', '___', '___'], ['___', '___', '___'], ['___', '___', '___']]
grid_grid = len(grid)
game = True
count_y = 0
for i in grid:
    print(i)

while game == True:

    x_input1 = int(input("Row:"))
    x_input2 = int(input("Column:"))

    x_final_move = grid[x_input1][x_input2]
    if grid[x_input1][x_input2] == "O":
        print("Spot has been taken")
    else:
        grid[x_input1][x_input2] = "X"
        for i in grid:
            print(i)

        if grid[0][0] == "X":
            if grid[0][1] == "X":
                if grid[0][2] == "X":
                    print("X wins!")
                    break
        elif grid[1][0] == "X":
            if grid[1][1] == "X":
                if grid[1][2] == "X":
                    print("X wins!")
                    break

        elif grid[2][0] == "X":
            if grid[2][1] == "X":
                if grid[2][2] == "X":
                    print("X wins!")
                    break

        elif grid[0][0] == "X":
            if grid[1][0] == "X":
                if grid[2][0] == "X":
                    print("X wins!")
                    break

            elif grid[1][1] == "X":
                if grid[2][2] == "X":
                    print("X wins!")
                    break

        elif grid[0][1] == "X":
            if grid[1][1] == "X":
                if grid[2][1] == "X":
                    print("X wins!")
                    break

        elif grid[0][2] == "X":
            if grid[1][2] == "X":
                if grid[2][2] == "X":
                    print("X wins!")
                    break
        elif grid[0][2] == "X":
            if grid[1][1] == "X":
                if grid[2][0] == "X":
                    print("X wins!")
                    break

    y_input1 = int(input("Row:"))
    y_input2 = int(input("Column:"))

    y_final_move = grid[y_input1][y_input2]

    if grid[y_input1][y_input2] == "X":
        print("Spot has been taken")
    else:
        grid[y_input1][y_input2] = "O"
        for i in grid:
            print(i)

        if grid[0][0] == "O":
            if grid[0][1] == "O":
                if grid[0][2] == "O":
                    print("O wins!")
                    break
        elif grid[1][0] == "O":
            if grid[1][1] == "O":
                if grid[1][2] == "O":
                    print("O wins!")
                    break

        elif grid[2][0] == "O":
            if grid[2][1] == "O":
                if grid[2][2] == "O":
                    print("O wins!")
                    break

        elif grid[0][0] == "O":
            if grid[1][0] == "O":
                if grid[2][0] == "O":
                    print("O wins!")
                    break

            elif grid[1][1] == "O":
                if grid[2][2] == "O":
                    print("O wins!")
                    break

        elif grid[0][1] == "O":
            if grid[1][1] == "O":
                if grid[2][1] == "O":
                    print("O wins!")
                    break

        elif grid[0][2] == "O":
            if grid[1][2] == "O":
                if grid[2][2] == "O":
                    print("O wins!")
                    break
        elif grid[0][2] == "O":
            if grid[1][1] == "O":
                if grid[2][0] == "O":
                    print("O wins!")
                    break
