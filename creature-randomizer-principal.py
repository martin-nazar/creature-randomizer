import random

with open('species.txt', 'r') as f:
    species = f.readlines()

with open('weapon.txt', 'r') as f:
    weapon = f.readlines()

limbs = ["0", "2", "4"]
eye = ["0", "2", "4", "6", "8"]
yes_no = ["No", "Yes"]
live_dead = ["Alive", "Dead"]
type = ["Robot", "Organic", "Mineral"]
status = ["Neutral", "Peaceful", "Angry"]

class creature:
    def __init__(self):
        self.species = random.choice(species)
        self.arm_number = random.choice(limbs)
        self.leg_number = random.choice(limbs)
        self.eye_number = random.choice(eye)
        self.live_dead = random.choice(live_dead)
        self.type = random.choice(type)
        self.status = random.choice(status)
        self.head_armor = random.choice(yes_no)
        self.shoulder_armor = random.choice(yes_no)
        self.chest_armor = random.choice(yes_no)
        self.arms_armor = random.choice(yes_no)
        self.hands_armor = random.choice(yes_no)
        self.legs_armor = random.choice(yes_no)
        self.feet_armor = random.choice(yes_no)
        

        if self.arm_number != "0":
            self.lef_arm = random.choice(weapon)
            self.right_arm = random.choice(weapon)
        else:
            self.lef_arm = "none"
            self.right_arm = "none"
        
    def funcSaludo(self):
        saludo = ("Hi, you've created: " + self.status + " " + self.type + " " + self.species.strip()
        + " with " + self.leg_number.strip() + " legs " 
        + "and " + self.arm_number.strip() + " arms ")

        if self.arm_number != "0":
            saludo = saludo + ("in the left arm a " + self.lef_arm.strip()
            + " and in the right arm a " + self.right_arm.strip())
        
        saludo = (saludo + " " + self.eye_number + " eyes " + self.live_dead + " ")

        if self.head_armor == "Yes" or self.shoulder_armor == "Yes" or self.chest_armor == "Yes" or self.arms_armor == "Yes" or self.hands_armor == "Yes" or self.legs_armor == "Yes" or self.feet_armor == "Yes":
            armor = "Armour on: "

            if self.head_armor == "Yes":
                armor = armor + " head"
            
            if self.shoulder_armor == "Yes":
                armor = armor + " shoulder"

            if self.chest_armor == "Yes":
                armor = armor + " chest"
            
            if self.arms_armor == "Yes":
                armor = armor + " arms"

            if self.hands_armor == "Yes":
                armor = armor + " hands"

            if self.legs_armor == "Yes":
                armor = armor + " legs"

            if self.feet_armor == "Yes":
                armor = armor + " feet"
            
        else: 
            armor = "Without armour"

        print(saludo + armor)

montruito = creature()
montruito.funcSaludo()