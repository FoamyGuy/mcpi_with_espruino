#www.stuffaboutcode.com
#Raspberry Pi, Minecraft Piano - Different blocks back different tones when hit!

#import the minecraft.py module from the minecraft directory
import mcpi.minecraft as minecraft
#import minecraft block module
import mcpi.block as block
#import time, so delays can be used
import time



if __name__ == "__main__":

    import serial
    ser = serial.Serial(22, timeout=1)  # open first serial port
    print ser.portstr       # check which port was really used

    #Connect to minecraft by creating the minecraft object
    # - minecraft needs to be running and in a game
    mc = minecraft.Minecraft.create()


    #block type to sound obj
    blocksToNotes = {block.STONE.id: 'f3',
                    block.GRASS.id: 'g3',
                    block.WOOD.id: 'a3',
                    block.BOOKSHELF.id: 'b3',  # Changed because dirt was becoming grass.
                    block.SAND.id: 'c4',
                    block.GRAVEL.id: 'd4',
                    block.LEAVES.id: 'e4',
                    block.COBBLESTONE.id: 'f4',
                    block.BRICK_BLOCK.id: 'g4',
                    block.WOOD_PLANKS.id: 'a4',
                    block.WOOL.id: 'b4'}

    #Post a message to the minecraft chat window 
    mc.postToChat("Minecraft Piano, www.stuffaboutcode.com")
    
    #loop until Ctrl C
    try:
        while True:
            #Get the block hit events
            blockHits = mc.events.pollBlockHits()
            # if a block has been hit
            if blockHits:
                # for each block that has been hit
                for blockHit in blockHits:
                    #If the block hit type (DIRT, WOOD, etc) is in the
                    # blocksToWavc dictionary - play the WAV
                    blockType = mc.getBlock(blockHit.pos.x, blockHit.pos.y, blockHit.pos.z)
                    if (blockType in blocksToNotes.keys()):
                        noteToPlay = blocksToNotes[blockType]
                        ser.write("playNote('%s');rest();\n" % noteToPlay)
            #sleep for a short time        
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("stopped")