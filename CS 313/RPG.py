#  File: RPG.py
#  Description: This code creates a very simple role playing game and determines
#               the outcome of a certain scenario of gameplay
#  Student's Name: Brian Smith-Eitches
#  Student's UT EID: bts867
#  Course Name: CS 313E 
#  Unique Number: 51915
#
#  Date Created: February 6, 2017
#  Date Last Modified: February 9, 2017

#create a class for Weapon
class Weapon:

    #create a method to convert the object into a string to print
    def __str__(self):
        return str(self.weaponname)

    #initialize the weapon as an object and find the weaponname
    def __init__(self,weaponname):
        self.weaponname=weaponname

#create a class for Armor       
class Armor:
    
    # define how to convert object as a string    
    def __str__(self):
        return str(self.armorname)
    
    # initialize armor and determine the armor class
    def __init__(self, armorname):
        self.armorname=armorname
        armorstrength={'plate':2,'chain':5,'leather':8,'none':10}
        self.armorclassnum=armorstrength[armorname]

#create a class for RPG Character 
class RPGCharacter:

    # define a method to show the character
    def show(self):
        print('\n ',self.name)
        print('    Current Health:',self.health)
        print('    Current Spell Points:',self.spellpoints)
        print('    Wielding:',self.weapon)
        print('    Wearing:',self.armor)
        print('    Armor Class:', self.armorclassnum)
        print()

    # define a method to check for defeat
    def checkForDefeat(self):
        #see if health is negative or zero
        if self.health<=0:
            print(self.name,"has been defeated!")

    # define a method to fight
    def fight(self, other):
        weaponvalue={'dagger':4,'axe':6,'staff':6, 'sword':10, 'none':1}
        #reduce health by value of the weapon power in dictionary above
        other.health-=weaponvalue[str(self.weapon)]
        # print out statements
        print(self.name,'attacks', other.name,'with a(n)',self.weapon)
        print(self.name,'does',weaponvalue[str(self.weapon)],'damage to',other.name)
        print(other.name,'is now down to',other.health,'health')
        other.checkForDefeat()

#create a class for Fighter
class Fighter(RPGCharacter):

    #initialize a fighter and set initial values to zero
    def __init__(self,name):
        self.name=name
        self.health=40
        self.spellpoints=0
        self.armor='none'
        self.weapon='none'
        self.type='fighter'
        self.armorclass=10

    #find a way to convert object to a string
    def __str__(self):
        return str(self.name)

    # define a method to give the character a weapon
    def wield(self,weapon):
        self.weapon=weapon
        print(self.name, 'is now wielding a(n)', self.weapon)

    # define a method for the character to put on armor
    def putOnArmor(self,armor):
        #update armor name
        self.armor=armor.armorname
        #update armor class value
        self.armorclassnum=armor.armorclassnum
        print(self.name,'is now wearing',armor.armorname)

    # define a method to take off armor
    def takeOffArmor(self):
        self.armor='none'
        print(self.name,"is no longer wearing anything.")
        self.armorclassnum=10

#create a class for Wizard
class Wizard(RPGCharacter):

    #create a method to put on armor
    def putOnArmor(self,armor):
        #disallow armor on wizards and do not do anything
        print('Armor not allowed for this character class.')

    # initialize wizards and set initial values
    def __init__(self,name):
        self.name=name
        self.health=16
        self.spellpoints=20
        self.armor='none'
        self.weapon='none'
        self.type='wizard'
        self.armorclassnum=10

    # determine a way to convert the object to a string
    def __str__(self):
        return str(self.name)

    # create a method to wield a weapon
    def wield(self,weapon):
        #only allow dagger and staff
        if str(weapon)=='dagger' or str(weapon)=='staff':
            #update weapon
            self.weapon=Weapon(weapon)
            print(self.name, 'is now wielding a(n)', self.weapon)
        else:
            print('Weapon not allowed for this character class')

    #create a method to unwield a weapon
    def unwield(self):
        #update weapon
        self.weapon=Weapon('none')
        print(self.name,'is no longer wielding anything.')

    #create a method to cast a spell
    def castSpell(self,name,other):

        #find spell cost and effect
        spellcost={'Fireball':3,'Lightning Bolt':10,'Heal':6}
        spelleffect={'Fireball':5,'Lightning Bolt':10,'Heal':-6}

        #determine if the spell is known
        if name not in spellcost:
            print('Unknown spell name. Spell failed.')
            return

        #see if character has enough spell points
        if self.spellpoints<spellcost[name]:
            print('Insufficient spell points.')
            return

        print(self.name,'casts',name,'at',other.name)
        # update health effect
        originalhealth=other.health
        other.health-=spelleffect[name]

        if name=='Heal':
            #charge the wizard spell points for casting the spell
            self.spellpoints-=spellcost[name]

            # max out the heal effect at max for class types
            if other.health>16:
                if other.type=='wizard':
                    other.health=16
                elif other.health>40:
                    other.health=40

            # calculate and print the value of the spell
            print(self.name,'heals',other.name,'for',other.health-originalhealth,'health points.')
            print(self.name,'is now at', other.health,'health')
            return

        else:
            #charge the wizard spell points for casting the spell
            self.spellpoints-=spellcost[name]
            #calculate damage done
            print(self.name,'does',spelleffect[name],'damage to',other.name)
            print(other.name,'is now down to', other.health,'health')

        return


#run the main function given by Professor Bulko
def main():

    chainMail = Armor("chain")
    sword = Weapon("sword")
    staff = Weapon("staff")
    axe = Weapon("axe")
    
    gandalf = Wizard("Gandalf the Grey")
    gandalf.wield(staff)
    
    aragorn = Fighter("Aragorn")

    aragorn.putOnArmor(chainMail)

    aragorn.wield(axe)

    gandalf.show()
    aragorn.show()

    gandalf.castSpell("Fireball",aragorn)
    aragorn.fight(gandalf)

    gandalf.show()
    aragorn.show()

    gandalf.castSpell("Lightning Bolt",aragorn)
    aragorn.wield(sword)

    gandalf.show()
    aragorn.show()

    gandalf.castSpell("Heal",gandalf)
    aragorn.fight(gandalf)

    gandalf.fight(aragorn)
    aragorn.fight(gandalf)

    gandalf.show()
    aragorn.show()


main()
