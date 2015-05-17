Virtual Espruino Pico clone:

This is a clone of the (most of) Espruino Pico that is built inside of minecraft. Each IO pin has a corresponding redstone torch that will control the actual IO pin on the attached Pico.

![image](https://raw.githubusercontent.com/FoamyGuy/mcpi_with_espruino/master/imgs/example5_pico.PNG)


[Python Code: example5_pico_input.py](example5_pico_input.py)

#To run:
- At this time the script doesn't build the Pico for you. So you'll have to do that yourself.
- Edit example5_pico_input.py to put the location of each of the pins inside of your minecraft world (note you can use as many or as few of the pico pins as you want)
- run example5_pico.py
- wire up a lever to each pin.


If everything worked then as you flip the lever the pico should flip the corresponding IO pin to either HIGH, or LOW.

![image](https://raw.githubusercontent.com/FoamyGuy/mcpi_with_espruino/master/imgs/example5_result.PNG)