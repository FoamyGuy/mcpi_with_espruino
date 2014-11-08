import mcpi.minecraft as minecraft
import serial
import time

# The location where redstone torch needs to spawn.
a0 = (-112, 0, 62)  # <- YOU MUST SET THIS VALUE

"""
Helper method: set_pin(pin,val)

Pass it a location and a value it will spawn the correct block (torch or air) at the given location.
"""
def set_pin(pin, val):
    if val:
        mc.setBlock(pin, 76)
    else:
        mc.setBlock(pin, 0)


if __name__ == "__main__":

    # My espruino was COM23, and I had to use value 22 here.
    port = 22;


    ser = serial.Serial(port, timeout=1)  # open first serial port
    print ser.portstr       # check which port was really used

    # Create mc object.
    mc = minecraft.Minecraft.create()


    # Main loop
    try:
        while True:

            # Send command to read the pin
            ser.write("digitalRead(A0)\n")

            # Read back the result
            print(ser.readline())
            ans = ser.readline().replace('\r\n', '').replace('=', '')
            print(ans)

            # set the minecraft pin according to value read.
            if int(ans):
                set_pin(a0, 1)
            else:
                set_pin(a0, 0)
            time.sleep(.2)

    except KeyboardInterrupt:
        print("stopped")
        ser.close()
