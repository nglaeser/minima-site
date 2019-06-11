---
layout:	post
title:	A Computer from the Ground Up II
lang: en
ref: µ611
date:	2019-03-12 10:53:37 -0400
audience: everyone
excerpt:
---

This project is in a similar vein to the [previous post of the same name](../../../2018/11/30/A-Computer-from-the-Ground-Up.html), but a little less fine-grained and more abstracted.  

After last semester's final exams, my friends James Coman, William Edwards, Brady O'Leary, and I gathered at my friend [Charles Daniels](http://cdaniels.net)'s house for a couple of days to work through the curriculum of the University of South Carolina's Advanced Digital Design course (CSCE 611); we called it "micro-611". We tried to complete six projects on FPGAs, leading up to the construction of a fully functional MIPS processor. I took pictures and videos of each final product along the way, and I'll go into some detail in this post. The raw notes from those couple of days can be found [here](https://github.com/nglaeser/Notes/tree/master/µ611) or [here](https://keybase.pub/nglaeser/Notes/µ611/).

### Background

Unlike the [previous post of the same name](../../../2018/11/30/A-Computer-from-the-Ground-Up.html), these projects aren't circuits that I physically built with wires and other components. Instead, we used a hardware description language (HDL) called Verilog to program field programmable gate arrays (FPGAs) to essentially simulate circuits. This sort of setup is becoming increasingly desireable in research and industry because of its flexibility, among other reasons. S(See my notes for more details.)

### Project 1: Hello World

This first project is a very simple one, sort of a "hello world" for working with FPGAs and Verilog. All I did here is short (i.e. connect) the switches to the LEDs. Here's a video of  the board in action:  

![Video of Project 1](../../../files/µ611/mu611-Project1.mp4)

### Project 2: ALU

Next, we are provided with a MIPS arithmetic logic unit (ALU). Here are its specifications:  

* 32-bit inputs and outputs
* 5-bit shift amount input (see SLL, SRL, SRA)
* 1-bit zero flag
* 13 operations with 4-bit opcodes:
    * ADD (addition)
    * SUB (subtraction)
    * MULT (multiplication)
    * MULTU (unsigned multiplication)
    * AND
    * OR
    * NOR
    * XOR
    * SLT (set less than flag)
    * SLTU (set less than flag - unsigned)
    * SLL (shift left logical - this fills the rightmost bit by looping around from the left)
    * SRL (shift right logical - this fill the leftmost bit by looping around from the right)
    * SRA (shift right arithmetic - this fills the leftmost bit with 0's)

You may notice some opcodes are missing, namely NAND and NOT. This is because NAND is not recognized in the MIPS assembler, so it has to be written as a macro, while NOT is similarly unrecognized and is implemented by NORing with `$0` (the register which always contains zero).

The goal of this project is to implement a simple calculator based on the provided ALU. Two 9-bit numbers can be entered on the 18 switches of the FPGA, and one of four operations - AND, OR, ADD, SUB - can be selected by pressing the corresponding button on the FPGA. The result is then displayed on the hex displays. 

Essentially all we have to do is use Verilog to add virtual wires that connect the switches to the ALU inputs and connect the buttons to a lookup table that will feed the corresponding opcode into the ALU. The output of the ALU is then used to turn on the correct portions of the hex display (the hex driver module was provided) and thus display the result. Note that the inputs are entered by the user in binary on the switches but the output is displayed in hexadecimal on the display (in the rightmost 4 digits). As a bonus, I display the two 2-digit inputs in hex in the first 4 digits of the display. The buttons are, from left to right: AND, OR, ADD, SUB.

Here is a video of the board at work:  

![Video of Project 2](../../../files/µ611/mu611-Project2.mp4)

### Project 3: Register File

In this next project, we implement a 32-bit by 32-bit register file. This means there will be 32 registers capable of storing 32 bits of data each. A couple of the registers are special: **register 0** will always contain zero and returns zero whenever it is read. For user interaction, we will also be implementing register-mapped I/O, so reading **register 30** will return the value entered on the switching while writing to it will update the value stored within and display this value on thhe hex displays. 

The register has the following inputs:  

* 2 5-bit read addresses
* 5-bit write address
* 1-bit clock signal (either high or low)
* 1-bit write enable signal (`we`)
* 32-bit write data
* 32-bit register 30 in (to be read from the switches)

...and has these outputs:  

* 2 32-bit read data values
* 32-bit register 30 out (to be displayed on the hex displays)

Here's a diagram illustrating the register file and its inputs and outputs:  

![Register file diagram](../../../files/µ611/Project3-diagram.png)

This project is a lot more complicated than the previous two because it requires clocked logic: we will write to a register on the rising edge of the clock, but we also want to make sure that when we read we get the most updated value, i.e. write bypasses read. This means that if we write and read to the same register simultaneously, the read should return what is being written in that cycle. I won't go into detail in the implementation, but I plan to commit all my code to a GitHub repo in the future so anyone who is curious enough can look into it (at your own risk).

Because most of the register values are simply stored internally, the video below only shows how the switches are connected to the hex display (presumably through register 30). The clock is connected as usual to a clock signal, but `readaddr1` is hardcoded to 0 and `readaddr2` is hardcoded to the decimal value 30. The `write enable` bit is also hardcoded to 1. `readdata2` is connected to `writedata` so that the hex displays are immediately updated upon the switches being flipped. 

I technically could have cheated and gotten the same video by simply hooking the switches up to the display in a manner similar to project 2, but you can take my word for it that the value is being stored in the register file as well.

![Video of Project 3](../../../files/µ611/mu611-Project3.mp4)

### Projects 4-6

To be completed...

### Conclusion

In the end, we have a fully functioning MIPS processor! This is capable of executing instructions in the form of an assembly program, so we can safely brag that we've essentially built a (very minimal) computer from scratch!

I didn't go into much of the nitty gritty detail here, so if you're confused, don't worry - check out [my more detailed post](../../../2018/11/30/A-Computer-from-the-Ground-Up.html), which aims to explain the inner workings of computers starting from essentially zero knowledge. I hope to also upload my code for these projects once completed (and polished a bit so it's more presentable) which will hopefully shed light into the implementations.
