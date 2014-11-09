import mcpi.minecraft as minecraft
import mcpi.block as Block
import serial
import time

# The location where redstone torch needs to spawn.
a0 = (-112, 0, 62)  # <- YOU MUST SET THIS VALUE (x,y,z)

"""
Helper method: get_pin(pin)

Returns whether the minecraft pin is turned on or off (based on redstone torch type)

Block(76, 1) -> Redstone Toch ON
Block(75, 1) -> Redstone Toch OFF
"""
def get_pin(pin):
    block = mc.getBlockWithData(pin)
    print(block)
    if block.id == 76:
        return 1
    elif block.id == 75:
        return 0
    else:
        return -1


if __name__ == "__main__":

    # My espruino was COM23, and I had to use value 22 here.
    port = 22;
    old_val = 0

    ser = serial.Serial(port, timeout=1)  # open first serial port
    print ser.portstr       # check which port was really used

    # Create mc object.
    mc = minecraft.Minecraft.create()


    # Main loop
    try:
        while True:
            # Read the minecraft pin
            cur_val = get_pin(a0)

            if cur_val != old_val:
                # write the result to the LED1 on Espruino
                if int(cur_val):
                    # turn LED on
                    ser.write("digitalWrite(LED1, 1)\n")
                else:
                    # turn LED off
                    ser.write("digitalWrite(LED1, 0)\n")


            old_val = cur_val
            time.sleep(.5)  # small sleep

    except KeyboardInterrupt:
        print("stopped")
        ser.close()
