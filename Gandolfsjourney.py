print("Welcome to Gandolfs Journey")
print("""
  ,                      _,-
   (\                  _,-','
    \\              ,-"  ,'
     \\           ,'   ,'
      \\        _:.----__.-."-._,-._
       \\    .-".:--`:::::.:.:'  )  `-.
        \\   `. ::L .::::::'`-._  (  ) :
         \\    ":::::::'  `-.   `-_ ) ,'
          \\.._/_`:::,' `.     .  `-:
          :" _   "\"" `-_    .    `  `.
           "\\"":--\     `-.__ ` .     `.
             \\'::  \    _-"__`--.__ `  . `.     _,--..-
              \\ ::  \_-":)(        ""-._ ` `.-''
               \\`:`-":::/ \\ .   .      `-.  :
               :\\:::::::'  \\     `    .   `. :
                :\\:':':'  . \\           `,  : :
                : \\     .    \\      .       `. :       ,-
               __`:\\      .   \\ .   `  ,'    ,: :   ,-'
        _,---""  :  \\ '        \\  .          :-"  ,'
    ,-""        :    \\:  .  :   \\  `  '     ,'   /
   '            :  :  \       .   \\   .   _,'  ,-'
               :  .   '       :   :`   `,-' ,--'
                :     :   :      ,'-._,' ,-'
                _:     :        :8:  ,--'
               :dd`-._,'-._.__-""' ,'
                             ,----'
                      _.----'
              __..--""
            ""

dd
      
      """)
turn1 = input("You have arrived at the steps of Mordor. Do you want to begin you ascend up the steps or adventure to the left into the Enchanted forest of Elonor? Enter Up or Left\n").lower()
if turn1 == "up":
    turn2 = input("You begin your slow ascend up the steps of Mordor and have come to the deep fires of Mount Doom. Here a giant flame engulfs the path and crumbles the road behind you and begins to split the upcoming path. Do you want to continue left or right?\n ").lower()   
    if turn2 == "left":
        turn3 = input("Immedietly you are faced against Balrog the fire demon of might! Darkness shroudes upon you, would you like to use your invisibility cloak, your staff or the ring to escape death? Enter cloak, staff or ring\n").lower()   
        if turn3 == "cloak":
            print("Balrogs keen sight from hiding in the great depths of mount doom has only enhanced his vision and he has seen right through your cloak. You are demolished by his fiery breath reminding him of the great battle of five armies. Game Over.\n")
        elif turn3 == "staff":
            print("The staff of five wizards slams against the ground and the roof above crushes Balrog and the exit out of the mountain shines bright behind him leading you to your destination! Congratulations!!")
        elif turn3 == "ring":
            print("You have slipped on the ring! Saurons eye instantly points directly towards you and the nearby Nazgul chew you to pieces! Game Over.")
        else:
            print("That is not a valid response")
    elif turn2 == "right":
        print("The road crumbles before you and you are enclosed by the seaping hot lava below you. Mount Doom has claimed another. Game Over")
    else:
        print("That is not a valid response")
elif turn1 == "left":
    print("You have entered the enchanted forest of Elonor! Unfortunately Golum was waiting behind a tree and instantly mauled you!! Game Over.")
else: 
    print("That is not a valid resposne")


