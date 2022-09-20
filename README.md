# Engineering_4_Notebook

&nbsp;

## Table of Contents
* [Launch_Pad_1](#launch_pad_1)
* [Launch_Pad_2](#launch_pad_2)
* [Launch_Pad_3](#launch_pad_3)
* [Launch_Pad_4](#launch_pad_4)
* [Crash Avoidance 1](#Crash_Avoidance_1)
* [Crash Avoidance 2](#Crash_Avoidance_2)
* [Onshape_Assignment_Template](#onshape_assignment_template)

&nbsp;

## Launch_Pad_1

### Description 

The goal of this assignment was to use a for loop to make a rasberry pie serial moniter countdown from 10 and then say liftoff. 

### Evidence 

![Launch Pad](images/ezgif.com-gif-maker.gif)

### Code

[Launch Pad 1 Code](raspberry-pi/Launch_1.py )

### Reflection 

The main thing I needed help on for this assignment was how to make thew for function count down instead of up. I needed to change the last value of the for function and make it -1 to count down instead of 1 to count up.

## Launch_Pad_2

### Description 

The goal of of this assignment was to add on to the code used in the previous assignment and make a LED flash green everytime it counted down and make another LED flash red when it got to liftoff.

### Evidence 

![Launch Pad 2](images/Launch_2.gif)

### Code

[Launch Pad 2 Code](raspberry-pi/Launch_2.py )

### Wiring 

![Launch Pad](images/image_123927839.JPG)

### Reflection 

The one thing that I was stuck on was how to make two seperate LEDs so the green can blink seperatly from the red. You have to make a led1 and led2 to make this work. 

## Launch_Pad_3

### Description

The goal of this project was to have the code do exactly what it did in launch 2 but have you control when the countdown starts with the press of a button. 

### Evidence 

![Launch Pad](images/Launch_3.gif)

### Code

[Launch Pad 3 Code](raspberry-pi/Launch_3.py )

### Wiring 

![Launch Pad](images/Launch_3_Wire.JPG)

### Reflection 

If you use the 3V3 pin on your Pico you have to use button.pull = digitalio.Pull.UP rather than pulling down. This means when you press the button it will read as button value equals true so you put your liftoff code under a while true function rather than a while false function. 

## Launch_Pad_4

### Description

The goal of this assignment was to build on Launch 3 and make a servo move 180 degrees simultaniously with the green light blinking and the moniter printing liftoff at the end of the countdown. 

### Evidence 

![Launch Pad](images/Launch_4.gif)

### Code

[Launch Pad 4 Code](raspberry-pi/Launch_4.py )

### Wiring 

![Launch Pad](images/Launch_4_Wire.JPG)

### Reflection 

One key to this assignment was to set the servo to zero before your while true loop runs so when you run your loop and it tells the servo to move to 180 degrees it won't already be there.

## Crash_Avoidance_1

### Description

The goal of this assignment was to print off the Y, X, and Z coordinates of an accelerometer 

### Evidence

![Crash 1](images/Crash_1.gif)

### Code

[Crash 1 Code](raspberry-pi/Crash_1.py)

### Wiring 

![Crash 1](images/image_50406145.JPG)

### Reflection 

One thing hard with this assignment was making it read off the right coordinates for each axis. For instance, having it read off the x coordinates when it moves in the x direction. You have to use {mpu.gyro[0]} for the x axis, {mpu.gyro[1]} for Y, and {mpu.gyro[2]} for Z.

## Crash_Avoidance_2

### Description



### Evidence

![Crash 2](images/Crash_2.gif)

### Code

[Crash 2 Code](raspberry-pi/Crash_2.py)

### Wiring 

![Crash 2](images/Crash_2_Wire.JPG)

### Reflection 




### Assignment Description

Write your assignment description here. What is the purpose of this assignment? It should be at least a few sentences.

### Evidence 

Pictures / Gifs of your work should go here. You need to communicate what your thing does. 

### Wiring

This may not be applicable to all assignments. Anything where you wire something up, include the wiring diagram here. The diagram should be clear enough that I can recreate the wiring from scratch. 

### Code
Give me a link to your code. [Something like this](https://github.com/millerm22/Engineering_4_Notebook/blob/main/Raspberry_Pi/hello_world.py). Don't make me hunt through your folders, give me a nice link to click to take me there! Remember to **COMMENT YOUR CODE** if you want full credit. 

### Reflection

What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience? Your goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person. Think about your audience for this one, which may be "future you" (when you realize you need some of this code in three months), me, or your college admission committee!

&nbsp;


## Onshape_Assignment_Template

### Assignment Description

Write your assignment description here. What is the purpose of this assignment? It should be at least a few sentences.

### Part Link 

[Create a link to your Onshape document](https://cvilleschools.onshape.com/documents/003e413cee57f7ccccaa15c2/w/ea71050bb283bf3bf088c96c/e/c85ae532263d3b551e1795d0?renderMode=0&uiState=62d9b9d7883c4f335ec42021). Don't forget to turn on link sharing in your Onshape document so that others can see it. 

### Part Image

Take a nice screenshot of your Onshape document. 

### Reflection

What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience? Your goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person. Think about your audience for this one, which may be "future you" (when you realize you need some of this code in three months), me, or your college admission committee!

&nbsp;

## Media Test

Your readme will have various images and gifs on it. Upload a test image and test gif to make sure you've got the process figured out. Pick whatever image and gif you want!

### Test Link

[Google](http://www.google.com)

### Test Github

[Code](raspberry-pi)

### Test Image

![Liverpool](images/01champions19-superJumbo.jpg)  

### Test GIF

![Elmo](images/giphy.gif)
