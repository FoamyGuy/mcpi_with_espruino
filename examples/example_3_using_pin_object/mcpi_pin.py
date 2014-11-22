import mcpi.vec3 as vec3
import mcpi.minecraft as minecraft


class McPin:

    # When reading value LOW will be a redstone torch turned off.
    READ_LOW = 75

    # When writing value LOW will be air.
    WRITE_LOW = 0

    # HIGH is always redstone torch turned on.
    HIGH = 76

    # Optional name for the pin
    name = ""

    # Value of the pin
    value = 0

    # location inside of the minecraft world.
    location = vec3.Vec3()

    def __init__(self, mc, name, value, location):
        self.name = name
        self.value = value
        self.location = location
        self.mc = mc
        self.mc.setBlock(self.location)

    """
    Returns the current value from the pin inside of minecraft.
    """
    def read_pin(self):
        block = self.mc.getBlockWithData(self.location)
        print(block)
        if block.id == self.HIGH:
            self.value = 1
        elif block.id == self.READ_LOW:
            self.value = 0
        else:
            self.value = -1

        return self.value


    """
    Writes a new value to the pin inside of minecraft.
    """
    def write_pin(self, new_val):
        self.value = new_val
        if new_val:
            self.mc.setBlock(self.location, 76)
        else:
            self.mc.setBlock(self.location, self.WRITE_LOW)

        self.value = new_val


"""
Normally we will use McPin from another script. But you can put code to test it here if you like.
"""
if __name__ == "__main__":
    mc = minecraft.Minecraft.create()
    test_pin = McPin(mc, "test", 1, vec3.Vec3(-112, 0, 65))
    test_pin.write_pin(0)
