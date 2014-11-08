#**mcpi with Espruino**

This project will serve as a holding place for resources related to interacting between the [Espruino](http://www.espruino.com/) and Minecraft using mcpi. Unless otherwise noted all of these projects and sample codes were created and tested using [RaspberryJuice](https://github.com/martinohanlon/CanaryRaspberryJuice/) on [Canarymod](http://canarymod.net/), with the PC Minecraft game. Though it should theoretically work on the Raspberry Pi edition of Minecraft as well.

---
#Getting Started
You need a few things in place to begin. 

 - Canarymod server with RaspberryJuice plugin running
 - Minecraft client running, connected to canarymod server.
 - Python installed on your machine + mcpi python module (included with RaspberryJuice project)
 - Espruino Web IDE
 - Espruino plugged in to PC
 
#Basic concept
RaspberryJuice exposes an easy to use python API to manipulate things inside of the minecraft world. Espruino exsposes a serial device that accepts and executes JavaScript commands. You can create python scripts that run commands on the Espruino, and then read the results, then use those results to manipulate things inside of minecraft.

#[Example 1 - Redstone Button](https://github.com/FoamyGuy/mcpi_with_espruino/blob/master/examples/example1_button/example1.md)
In this example we will hook up a physical button and have it turn on/off a redstone circuit in Minecraft. We will continually poll the Espruino to find out if the button is being pressed. If it is we'll spawn a redstone torch, it is isn't we'll spawn air.

#[Example 2 - Redstone Switch LED](https://github.com/FoamyGuy/mcpi_with_espruino/blob/master/examples/example2_led/example2.md)
In this example we will hook up a redstone switch inside of Minecraft to control a physical LED on the espruino board.
