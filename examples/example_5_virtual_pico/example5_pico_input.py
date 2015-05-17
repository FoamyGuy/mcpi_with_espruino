import mcpi.minecraft as minecraft
import mcpi.block as Block
import serial
import mcpi.vec3 as vec3
import time
from mcpi_pin import McPin

# The location where redstone torches needs to spawn.

input_pins = {"A5": vec3.Vec3(-22, 1, -44),
              "A6": vec3.Vec3(-22, 1, -42),
              "A7": vec3.Vec3(-22, 1, -40),
              "B1": vec3.Vec3(-22, 1, -38),
              "B10": vec3.Vec3(-22, 1, -36),
              "B13": vec3.Vec3(-22, 1, -34),
              "B14": vec3.Vec3(-22, 1, -32),
              "B15": vec3.Vec3(-22, 1, -30),
              "B3": vec3.Vec3(-12, 1, -34),
              "B4": vec3.Vec3(-12, 1, -36),
              "B5": vec3.Vec3(-12, 1, -38),
              "B6": vec3.Vec3(-12, 1, -40),
              "B7": vec3.Vec3(-12, 1, -42),
              "A8": vec3.Vec3(-12, 1, -44),
              }

if __name__ == "__main__":

    # My espruino pico was COM29, and I had to use value 28 here.
    port = 28;



    ser = serial.Serial(port, timeout=1)  # open first serial port
    print ser.portstr       # check which port was really used

    # Create mc object.
    mc = minecraft.Minecraft.create()

    mc_pins = {}
    old_vals = {}
    for name in input_pins.keys():
        print (name)
        print(input_pins[name])
        old_vals[name] = 0
        mc_pins[name] = McPin(mc, name, 0, input_pins[name])


    cur_vals = {}

    # Main loop
    try:
        while True:
            # Read the minecraft pins
            for name in mc_pins.keys():
                pin = mc_pins[name]
                cur_vals[name] = pin.read_pin()

                if cur_vals[name] != old_vals[name]:
                    # write the result to the Espruino Pico
                    if int(cur_vals[name]):
                        # turn LED on
                        ser.write("digitalWrite(%s, 1)\n" % (pin.name))
                    else:
                        # turn LED off
                        ser.write("digitalWrite(%s, 0)\n" % (pin.name))

            #update the old_vals dict
            for name in cur_vals.keys():
                old_vals[name] = cur_vals[name]


            time.sleep(.5)  # small sleep
    except KeyboardInterrupt:
        print("stopped")
        ser.close()
