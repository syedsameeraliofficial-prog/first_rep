age = int(input("Your Age : "))

gender = (input("Male \nFemale \nEnter your Gender: ")).lower()

category1 = "Kid"
category2 = "Adult"

# Kids
if age < 18 and (gender == "male" or gender == "female"):
    print("\n                   ", gender.upper(), category1)
    print("\n                     Welcome to Kids section")
    
    cloth = (input("\nWhat are you looking for ? \n1) Casual  \n2) Formal ?\n")).lower()
    
    if cloth == "casual" or cloth == "1":
        cloth_type = "Casual"
    elif cloth == "formal" or cloth == "2":
        cloth_type = "Formal"
    else:
        print("Type Correct Number")
        
        
    color = input("\nWhat type of color are you looking for ? \n1) Cool \n2) Dark \n3) Light? \n   ").lower()
    
    if color == "cool" or color == "1":
        color_type = "cool"
        print("\n", cloth_type, color_type.capitalize())
    elif color == "dark" or color == "2":
        color_type = "dark"
        print("\n", cloth_type, color_type.capitalize())
    elif color == "light" or color == "3":
        color_type = "light"
        print("\n", cloth_type, color_type.capitalize())
    else:
        print("Invalid Input")
        
    if (cloth == "casual" or cloth == "1") and color_type == "cool":
        print("\nYou're Recommended to buy Jeans and T-Shirt")
    
    if (cloth == "casual" or cloth == "1") and color_type == "dark":
        print("\nYou're Recommended to buy Dark Jeans and Dark T-Shirt")
    
    if (cloth == "casual" or cloth == "1") and color_type == "light":
        print("\nYou're Recommended to buy Light Jeans and Light T-Shirt")
    
    if (cloth == "formal" or cloth == "2") and color_type == "cool":
        print("\nYou're Recommended to buy Formal Cool Colored Jeans and Button Downed Cool Shirt")
    
    if (cloth == "formal" or cloth == "2") and color_type == "dark":
        print("\nYou're Recommended to buy Formal Dark Colored Jeans and Button Downed Dark Shirt")
    
    if (cloth == "formal" or cloth == "2") and color_type == "light":
        print("\nYou're Recommended to buy Formal Light Colored Jeans and Button Downed Light Shirt")    


# Adults
elif age >= 18 and (gender == "male" or gender == "female"):
    print("\n       ", gender.upper(), category2)
    print("\n         Welcome to Adults section")
    
    cloth = (input("What are you looking for ? \n1) Casual  \n2) Formal ?\n")).lower()
    
    if cloth == "casual" or cloth == "1":
        cloth_type = "Casual"
    elif cloth == "formal" or cloth == "2":
        cloth_type = "Formal"
    else:
        print("Type Correct Number")
        
        
    color = input("\nWhat type of color are you looking for ? \n1) Cool \n2) Dark \n3) Light? \n").lower()
    
    if color == "cool" or color == "1":
        color_type = "cool"
        print("\n", cloth_type, color_type.capitalize())
    elif color == "dark" or color == "2":
        color_type = "dark"
        print("\n", cloth_type, color_type.capitalize())
    elif color == "light" or color == "3":
        color_type = "light"
        print("\n", cloth_type, color_type.capitalize())
    else:
        print("Invalid Input")
        
    if (cloth == "casual" or cloth == "1") and color_type == "cool":
        print("\nYou're Recommended to buy Adult Jeans and Adult T-Shirt")
        
    if (cloth == "casual" or cloth == "1") and color_type == "dark":
        print("\nYou're Recommended to buy Adult Dark Jeans and Adult Dark T-Shirt")
        
    if (cloth == "casual" or cloth == "1") and color_type == "light":
        print("\nYou're Recommended to buy Adult Light Jeans and Adult Light T-Shirt")
        
    if (cloth == "formal" or cloth == "2") and color_type == "cool":
        print("\nYou're Recommended to buy Adult Formal Cool Colored Jeans and Adult Button Downed Cool Shirt")
        
    if (cloth == "formal" or cloth == "2") and color_type == "dark":
        print("\nYou're Recommended to buy Adult Formal Dark Colored Jeans and Adult Button Downed Dark Shirt")
        
    if (cloth == "formal" or cloth == "2") and color_type == "light":
        print("\nYou're Recommended to buy Adult Formal Light Colored Jeans and Adult Button Downed Light Shirt")
