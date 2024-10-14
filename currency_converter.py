# Functions for converting
def convert_naira ():
    while True:
        # currency rate
        dollar_rate = 1600
        pound_rate = 2183
        euro_rate = 1829
        # conversion for each currency
        convert_1 = input("\nConvert naira to which currency?: " + "\n1.Dollar" + "\n2.Pound"
                        + "\n3.Euro\n" + "\nType Here: ")
        if convert_1 == "1":
            naira_info = int(input ("Naira Amount: #"))
            currency_cal = str(naira_info / dollar_rate)
            print ("Your Dollar amount is: $" + currency_cal)
            repeat = input ("Do you still want to convert Naira to other currency? y/n: ")
            if repeat == 'y':
                print (convert_1)
            else:
                break
        elif convert_1 == "2":
            naira_info = int(input ("Naira Amount: #"))
            currency_cal = str(naira_info / pound_rate)
            print ("Your Pound amount is: £" + currency_cal)
            repeat = input ("Do you still want to convert Naira to other currency? y/n: ")
            if repeat == 'y':
                print (convert_1)
            else:
                break
        elif convert_1 == "3":
            naira_info = int(input ("Naira Amount: #"))
            currency_cal = str(naira_info / euro_rate)
            print ("Your Euro amount: €" + currency_cal)
            repeat = input ("Do you still want to convert Naira to other currency? y/n: ")
            if repeat == 'y':
                print (convert_1)
            else:
                break
        else:
            print ("Invalid Input...")

def convert_dollars ():
    while True:
        # currency rate
        naira_rate = 1600
        pound_rate = 0.76643
        euro_rate = 0.83708
        # conversion for each currency
        convert_2 = input("Convert Dollar to which currency?: " + "\n1.Naira" + "\n2.Pound"
                        + "\n3.Euro\n" + "\nType Here: ")
        if convert_2 == "1":
            dollar_info = int(input ("Dollar Amount: $"))
            currency_cal = str(dollar_info * naira_rate)
            print ("Your Naira amount is: #" + currency_cal)
            repeat = input ("Do you still want to convert Naira to other currency? y/n: ")
            if repeat == 'y':
                print (convert_2)
            else:
                break
        elif convert_2 == "2":
            dollar_info = int(input ("Dollar Amount: $"))
            currency_cal = str(dollar_info * pound_rate)
            print ("Your Pound amount is: £" + currency_cal)
            repeat = input ("Do you still want to convert Naira to other currency? y/n: ")
            if repeat == 'y':
                print (convert_2)
            else:
                break
        elif convert_2 == "3":
            dollar_info = int(input ("Dollar Amount: $"))
            currency_cal = str(dollar_info * euro_rate)
            print ("Your Euro amount: €" + currency_cal)
            repeat = input ("Do you still want to convert Naira to other currency? y/n: ")
            if repeat == 'y':
                print (convert_2)
            else:
                break
        else:
            print ("Invalid Input")

def convert_pound ():
    while True:
        # currency rate
        naira_rate = 2180
        dollar_rate = 1.305
        euro_rate = 1.195
        # conversion for each currency
        convert_3 = input("Convert Dollar to which currency?: " + "\n1.Naira" + "\n2.Dollar"
                        + "\n3.Euro\n" + "\nType Here: ")
        if convert_3 == "1":
            pound_info = int(input ("Pound Amount: £"))
            currency_cal = str(pound_info * naira_rate)
            print ("Your Naira amount is: #" + currency_cal)
            repeat = input ("Do you still want to convert Naira to other currency? y/n: ")
            if repeat == 'y':
                print (convert_3)
            else:
                break
        elif convert_3 == "2":
            pound_info = int(input ("Pound Amount: £"))
            currency_cal = str(pound_info * dollar_rate)
            print ("Your Pound amount is: £" + currency_cal)
            repeat = input ("Do you still want to convert Naira to other currency? y/n: ")
            if repeat == 'y':
                print (convert_3)
            else:
                break
        elif convert_3 == "3":
            pound_info = int(input ("Pound Amount: £"))
            currency_cal = str(pound_info * euro_rate)
            print ("Your Euro amount: €" + currency_cal)
            repeat = input ("Do you still want to convert Naira to other currency? y/n: ")
            if repeat == 'y':
                print (convert_3)
            else:
                break
        else:
            print ("Invalid Input")
    
def convert_euro ():
    while True:
        # currency rate
        naira_rate = 1825
        dollar_rate = 1.12
        pound_rate = 0.893
        # conversion for each currency
        convert_4 = input("Convert Dollar to which currency?: " + "\n1.Naira" + "\n2.Dollar"
                        + "\n3.Pound\n" + "\nType Here: ")
        if convert_4 == "1":
            euro_info = int(input ("Euro Amount: €"))
            currency_cal = str(euro_info * naira_rate)
            print ("Your Naira amount is: #" + currency_cal)
            repeat = input ("Do you still want to convert Naira to other currency? y/n: ")
            if repeat == 'y':
                print (convert_4)
            else:
                break
        elif convert_4 == "2":
            euro_info = int(input ("Euro Amount: €"))
            currency_cal = str(euro_info * dollar_rate)
            print ("Your Pound amount is: £" + currency_cal)
            repeat = input ("Do you still want to convert Naira to other currency? y/n: ")
            if repeat == 'y':
                print (convert_4)
            else:
                break
        elif convert_4 == "3":
            euro_info = int(input ("Euro Amount: €"))
            currency_cal = str(euro_info * pound_rate)
            print ("Your Euro amount: €" + currency_cal)
            repeat = input ("Do you still want to convert Naira to other currency? y/n: ")
            if repeat == 'y':
                print (convert_4)
            else:
                break
        else:
            print ("Invalid Input")  

# Ask which currency you want to convert
while True:
    print ("\nConvert your chosen currency to other currency")
    print ("Which Currency do you want to convert?")
    print ("\nPlease type from the number corresponding to the list below: " + "\n1.Naira" + "\n2.Dollar" + "\n3.Pound" + "\n4.Euro")
    print ("\nType 'quit' to quit the program...")
    prompt = "\nType here: "

    convert = input(prompt)
    
    if convert == "quit":
        print("Do you really want to quit? y/n")
        convert = input ('\nTpe here: ')
        if convert == "y":
            break
        elif convert == "n":
            print ("....")
    if convert == "1":
        convert_naira ()
    elif convert == "2":
        convert_dollars ()
    elif convert == "3":
        convert_pound ()
    elif convert == "4":
        convert_euro ()