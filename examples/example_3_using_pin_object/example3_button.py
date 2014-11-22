import mcpi.minecraft as minecraft
import serial
import time
from mcpi_pin import McPin
import mcpi.vec3 as vec3

# The location where redstone torch needs to spawn.
location = vec3.Vec3(-112, 0, 65)  # <- YOU MUST SET THIS VALUE (x,y,z)


if __name__ == "__main__":

    # My espruino was COM23, and I had to use value 22 here.
    port = 22;


    ser = serial.Serial(port, timeout=1)  # open first serial port
    print ser.portstr       # check which port was really used

    # Create mc object.
    mc = minecraft.Minecraft.create()

    pin_a0 = McPin(mc, 'a0', 1, location)


    # Main loop
    try:

        while True:

            inc_command = ser.readline()

            print(inc_command)



            # Send command to read the pin
            ser.write("digitalRead(A0)\n")

            # Read back the result
            blank_line = ser.readline()
            ans = ser.readline().replace('\r\n', '').replace('=', '')
            print(ans)

            # set the minecraft pin according to value read.
            if int(ans):
                pin_a0.write_pin(1)
            else:
                pin_a0.write_pin(0)



            time.sleep(.2)  # small sleep

    except KeyboardInterrupt:
        print("stopped")
        ser.close()
