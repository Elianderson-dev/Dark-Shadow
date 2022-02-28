import random
import data

print("Make an password.")

enter_password = input("""Press enter for generate
a automatic password: """)

def print_bars (bars=str):
        for values in password:
            print("-")   

if enter_password == "":

    abc = data.select_the_letters("a")

    num = data.select_the_numbers("b") 

    password = abc + num

    save_password = password

else: 
            
    save_password = enter_password
    print(f"""Your password:{enter_password}
                             {print_bars}""")                
