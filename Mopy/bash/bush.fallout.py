
# Default Eyes/Hair -----------------------------------------------------------
#standardEyes = [ob(x) for x in (0x27306,0x27308,0x27309)] + [cobl(x) for x in (0x000821, 0x000823, 0x000825, 0x000828, 0x000834, 0x000837, 0x000839, 0x00084F, )]
standardEyes = [ob(x) for x in (0x4252,0x4253,0x4254,0x4255,0x4256)]
 
defaultEyes = {
    #--fallout3.esm
    ob(0x000019): #--Caucasian
        standardEyes,
    ob(0x0038e5): #--Hispanic
        standardEyes,
    ob(0x0038e6): #--Asian
        standardEyes,
    ob(0x003b3e): #--Ghoul
        [ob(0x35e4f)],
    ob(0x00424a): #--AfricanAmerican
        standardEyes,
    ob(0x0042be): #--AfricanAmerican Child
        standardEyes,
    ob(0x0042bf): #--AfricanAmerican Old
        standardEyes,
    ob(0x0042c0): #--Asian Child
        standardEyes,
    ob(0x0042c1): #--Asian Old
        standardEyes,
    ob(0x0042c2): #--Caucasian Child
        standardEyes,
    ob(0x0042c3): #--Caucasian Old
        standardEyes,
    ob(0x0042c4): #--Hispanic Child
        standardEyes,
    ob(0x0042c5): #--Hispanic Old
        standardEyes,
    ob(0x04bb8d): #--Caucasian Raider
        [ob(0x4cb10)],
    ob(0x04bf70): #--Hispanic Raider
        [ob(0x4cb10)],
    ob(0x04bf71): #--Asian Raider
        [ob(0x4cb10)],
    ob(0x04bf72): #--AfricanAmerican Raider
        [ob(0x4cb10)],
    ob(0x0987dc): #--Hispanic Old Aged
        standardEyes,
    ob(0x0987dd): #--Asian Old Aged
        standardEyes,
    ob(0x0987de): #--AfricanAmerican Old Aged
        standardEyes,
    ob(0x0987df): #--Caucasian Old Aged
        standardEyes,
    }
  