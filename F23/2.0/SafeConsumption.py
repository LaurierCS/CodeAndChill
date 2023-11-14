def safeForConsumption(ingredients, calories, plastics, sodium): 
     VEG = ["Lettuce","Tomatoes","Pickles","Onions"] # A list of vegetable constants
     MP = plastics * 100

     safeC = False # for the calories
     safeP = False # for the plastics
     safeS = False # for the sodium

     # Get the amount of vegetables in ingredient list 
     vCount = sum(itm in VEG for itm in ingredients)

     # Monstrous if trees incoming >.<

     # Calorie conditions for it to be safe
     if (calories < 1200):
          safeC = True
     elif (1200 <= calories <= 2300 and vCount >= 1):
          safeC = True
     elif (2300 < calories < 4600 and vCount >= 2):
          safeC = True
     elif (4600 <= calories <= 6800 and vCount >= 3):
          safeC = True

     # Microplastic conditions for it to be safe
     if (MP < 16):
          safeP = True
     elif (16 <= MP <= 23 and vCount >= 1):
          safeP = True
     elif (23 < MP < 46 and vCount >= 1):
          if ("Beef" in ingredients or "Chicken" in ingredients):
               safeP = True
          else:
               safeP = False

     # Sodium conditions for it to be safe
     if (sodium <= 2300):
          safeS = True
     elif (sodium > 2300):
          if ("Beef" in ingredients or "Pork" in ingredients):
               safeS = True
          else:
               safeS = False

     # Return statement
     return (safeC and safeP and safeS)

ingredients = ["Chicken", "Pork", "Lettuce", "Onions", "Cheese"]
calories = 4300
plastics = 0.41
sodium = 2300

print("Safe for human consumption?: " + str(safeForConsumption(ingredients, calories, plastics, sodium)))