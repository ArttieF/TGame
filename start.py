import lib.rtsystems as rts
import lib.rtstoryteller as rtst

def main():
    # get name stored for later use.s
    name = char_naming()
    
    # create character sheet
    sheet = char_creation(name)
    
    # give the ending screen time to be fully read. 5 seconds default?
    rtst.scs(sheet)
    rts.sleep(5)
    rts.clear()


# get name for character
def char_naming():
    name = input("What is your name? ")
    return name


#create a character
def char_creation(name):
    
    #assign rolled points to character sheet loop till 0
    points = rtst.dice(6) + 3
    stat1 = rtst.sedit(points, 'STR')
    points = rtst.dice(6) + 3
    stat2 = rtst.sedit(points, 'AGI')
    points = rtst.dice(6) + 3
    stat3 = rtst.sedit(points, 'INT')
        
    #pass stats to sheet, and return them
    sheet = {'Name': name, 'STR': stat1, 'AGI': stat2,'INT': stat3}
    return sheet


main()