import mcpi.minecraft as minecraft
import serial
import time

a0 = (-112, 0, 62)

def set_pin(pin, val):
    if val:
        mc.setBlock(pin, 76)
    else:
        mc.setBlock(pin, 0)



if __name__ == "__main__":

    ser = serial.Serial(22, timeout=1)  # open first serial port
    print ser.portstr       # check which port was really used
    mc = minecraft.Minecraft.create()
    try:
        while True:
            ser.write("digitalRead(A0)\n")
            print(ser.readline())
            ans = ser.readline().replace('\r\n', '').replace('=', '')
            print(ans)
            if int(ans):
                set_pin(a0, 1)
            else:
                set_pin(a0, 0)
            time.sleep(.2)

    except KeyboardInterrupt:
        print("stopped")
        ser.close()
