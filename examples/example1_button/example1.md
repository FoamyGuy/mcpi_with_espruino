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