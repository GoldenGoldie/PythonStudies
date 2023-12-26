def check_square_to_2(penguin):
    fish = True
    while fish:
        if penguin%2 == 0:
            
            penguin = penguin / 2

            if penguin == 1.0:
                return True
            

        if penguin%2 != 0:
            return False
    

x = check_square_to_2(128)

print(x)