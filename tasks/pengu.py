
def penguInfoOut(penguin):
    if penguin > 0:
        print(f"it is a known penguin {penguin}")

    if penguin %2 == 0:
        print("it is a male penguin and i am very sad")
        print("")
    if penguin %2 != 0:
        print("it is a female penguin and i am very sad")
        print("")
    
    if penguin < 0:
        print(f" {penguin} is not a known penguin")

penguInfoOut(2)
penguInfoOut(3)
penguInfoOut(0xFFFFFFFFFFFFFFFFFFFF)

def check_square_to_2(penguin):
    fish = True
    while fish:
        if penguin%2 == 0:
            
            penguin = penguin / 2

            if penguin == 1.0:
                return True
            

        if penguin%2 != 0:
            return False

def penguinEvolution(penguin,years):
    counter_female_skip = 1
    years_counter = 0
    penguin_skip = 1
    penguin_skip_counter = True
    counter = True
    counter_loop = 0
    female_penguin_skip = 0
    n = 2
    while  counter:
        if penguin > 0:
            year_counter = 0
            male_skip = False
            
            if year_counter == 0:
                if penguin %2 == 0:
                    x = check_square_to_2(penguin)
                    if x:
                        penguin = 1 
                        male_skip = True
                        
                    if male_skip == False:
                        penguin = penguin / 2
                    year_counter = 1



            if year_counter == 0:
                
                if penguin %2 != 0:
                    if penguin_skip_counter == True:
                        if penguin %7 == 0:
                            penguin_skip = 7
                            counter_female_skip += 1
                            if counter_female_skip == 7:
                                penguin = penguin * 3 +1
                        if penguin_skip != 7:
                            penguin = penguin * 3 + 1
                            year_counter = 1
                        
                    
                    if penguin_skip == 7:
                        penguin_skip_counter = False
                        female_penguin_skip +=1
                        if female_penguin_skip == penguin_skip:
                            penguin_skip_counter = True
                            


                    

           



        
            counter_loop += 1
            if counter_loop == years:
                counter = False

            years_counter += 1

            print(f"{years_counter}: {penguin}")
            print("")

    





penguinEvolution(128,2)
penguinEvolution(9,9)
penguinEvolution(9,10)