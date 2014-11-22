import mcpi.minecraft as minecraft
import mcpi.block as Block
import serial
import mcpi.vec3 as vec3
import time
from mcpi_pin import McPin

# The location where redstone torch needs to spawn.
location = vec3.Vec3(-112, 0, 62)  # <- YOU MUST SET THIS VALUE (x,y,z)

if __name__ == "__main__":

    # My espruino was COM23, and I had to use value 22 here.
    port = 22;
    old_val = 0

    ser = serial.Serial(port, timeout=1)  # open first serial port
    print ser.portstr       # check which port was really used

    # Create mc object.
    mc = minecraft.Minecraft.create()

    pin_led1 = McPin(mc, 'a0', 0, location)

    # Main loop
    try:
        while True:
            # Read the minecraft pin
            cur_val = pin_led1.read_pin()

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
