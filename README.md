#**mcpi with Espruino**

This project will serve as a holding place for resources related to interacting between the [Espruino](http://www.espruino.com/) and Minecraft using mcpi. Unless otherwise noted all of these projects and sample codes were created and tested using [RaspberryJuice](https://github.com/martinohanlon/CanaryRaspberryJuice/) on [Canarymod](http://canarymod.net/), with the PC Minecraft game. Though it should theoretically work on the Raspberry Pi edition of Minecraft as well.

---
#Getting Started
You need a few things in place to begin. 

 - Canarymod server with RaspberryJuice plugin running
 - Minecraft client running, connected to canarymod server.
 - Python installed on your machine
 - Espruino Web IDE
 - Espruino plugged in to PC
 
#Basic concept
RaspberryJuice exposes an easy to use python API to manipulate things inside of the minecraft world. Espruino exsposes a serial device that accepts and executes JavaScript commands. You can create python scripts that run commands on the Espruino, and then read the results, then use those results to manipulate things inside of minecraft.

#Example 1 - Redstone Button
In this example we will hook up a physical button and have it turn on/off a redstone circuit in Minecraft. We will continually poll the Espruino to find out if the button is being pressed. If it is we'll spawn a redstone torch, it is isn't we'll spawn air.

Physical Circuit:

![image](https://raw.githubusercontent.com/FoamyGuy/mcpi_with_espruino/master/imgs/example1_button.PNG)

Redstone Circut:

![image](https://raw.githubusercontent.com/FoamyGuy/mcpi_with_espruino/master/imgs/example1_redstone.PNG)

Espruino Code:
```
function onInit() {
    // Set the pin to use
    var MY_PIN = A0;
    // Set the mode on the pin.
    pinMode(A0, "input_pulldown");
}
onInit();
```

[Python Code: example1_button.py](https://github.com/FoamyGuy/mcpi_with_espruino/blob/master/example1_button.py)

#To run:
- Paste the espruino code from above into the right half of the Espruino web IDE, then press 'Send to espruino'
- **Important:** Once it is running press the dissconnect button in the top left corner of Espruino web IDE
- Edit example1_button.py to put the location of your "pin" inside of your minecraft world
- run example1_button.py


If everything worked then you should be able to press your physical button and see the red stone torch spawn.

![image](https://raw.githubusercontent.com/FoamyGuy/mcpi_with_espruino/master/imgs/example1_result.PNG)

