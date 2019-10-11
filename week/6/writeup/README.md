# Writeup 6 - Binaries I

Name: Sean Chapman
Section: 115319957

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Sean  Chapman

## Assignment Writeup

### Part 1 (50 pts)

CMSC389R-{di5a55_0r_d13}

### Part 2 (50 pts)
The first thing I did was run the program with no arguments. Doing this gave me the output `"Did you even try to dissassemble?"`. I then ran the program with one or two arguments, which gave me the output `"Multi-word arguments can be quoted"`. These were the only two outputs I could get from the program without dissassembling. The first thing I did in the dissassembly process was open up the example.c file and understand it. I then used Binary Ninja to compare the C code to the assembly while looking at the lecture slides, in order to familiarize myself with x86 assembly. Once I felt comfortable, I opened the crackme program in Binary Ninja. The first function I focused on was `main`. Looking at this function gave me an overall view  of the program that I was looking at. I could see that the program was taking input and running 3 checks on it; `check1`, `check2`, and `check3`. Looking at `check1`, I noticed that the program was comparing the input to the string `"Oh God"`. I then ran the crackme program with "Oh God" as the input and got `"I wish you cared more about the environment"`. I then moved on to `check2`. Here, I noticed that the program was using the strings "FOOBAR" and "seye ym ". I also noticed that this function was calling `getenv`, which means it must be looking for an environment variable. I created an environment variable `FOOBAR = "seye ym "` and ran the program again with "Oh God" as the input, which gave me `"You've almost got this!"`. I then tried again, this time setting FOOBAR = " my eyes", which gave me the output `"open sesame"`. With that, I moved on to `check3`. I saw that `check3` was using the string "sesame" and using the `open` system call. This told me that the program was trying to open a file called "sesame". So in the week 6 directory I ran the command `touch sesame`, then ran the executable with "Oh God", which gave me `"I like that, but more"`. I then noticed that the program was doing a string comparison, so it must have been comparing the content of the sesame file to some string. Clicking on the memory addresses being compared and pressing "R" revealed the actual character values. I could see that the program was comparing the content of sesame to " they burn". So, I added " they burn" to the sesame file and ran the executable again, which finally produced the flag.
