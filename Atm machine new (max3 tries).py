import sys

pass_code="0303"
pass_code1="2486"
attempt=0


while True:

    customer=(input(" Enter your PIN  \n "))
    
    if customer not in [pass_code , pass_code1]:
        attempt+=1
        print("Enter Correct PIN")
        
    
        if attempt>=3:
            print("Your Card has been blocked")
            sys.exit()
        continue
                
    else:
        attempt=0
    
    while True:
        selection1=input("\nYour Account Type \n1) Current \n2) Saving \n").lower()

   
            
        if selection1!="1" and selection1!="current" and selection1!="2" and selection1!="saving":
            print("\nSelect Again")
            continue
        else:
            break
                       
                       
            
        
                    
    while True:
        sel2=input("\n1) Fast Cash \n2)Cash Withdrawal \n3)Balance Inquiry \n4)Transfer \n5)Bill payment \n").lower()

        if sel2!="1" and sel2!="2" and sel2!="3" and sel2!="4" and sel2!="5" and sel2!="fast cash" and sel2!="cash withdrawal" and sel2!="balance inquiry" and sel2!="transfer" and sel2!="bill payment":
            print("\nSelect Again")
            continue
        else:
            break
        
    
            
    while True:
        receipt=input("\nDo you want Receipt \nYes \nNo \n").lower()

        if receipt not in ["yes" , "y" , "no" , "n"]:
            print("\nSelect Again , Wrong Input")
            continue
        else:
            break
    ########################################################################
        
        
    if receipt in ["yes", "y"]:
        print("\nYour balance is ******")     
        ask=input("\nDo you want to do another transaction\nYes\\No\n").lower()


    elif receipt in ["no" , "n"]:
        ask=input("\nDo you want to do another transaction\nYes\\No\n").lower()

        
    while ask not in ["yes", "y"] and ask not in ["no" , "n"]:
        print("Wrong input")
        ask=input("\nDo you want to do another transaction\nYes\\No\n").lower()

    if ask=="yes" or ask=="y":
        continue
        
        
        
    elif ask=="no" or ask=="n":
        print("Thank you")
        exit()
    
    


