# Writeup 2 - Pentesting

Name: Sean Chapman
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: *PUT YOUR NAME HERE*

## Assignment Writeup

### Part 1 (45 pts)

The flag CMSC389R-{p1ng_as_a_$erv1c3} is found by running the command  `1 & cat /home/flag.txt`. To find the flag I first connected to the server and ran the command `1 & ls` to see what directories I could navigate to. I then ran the command `1  & ls /home/` to see what was in the home directory, and that is where I found the flag.txt file. Running `cat` on that file produced the flag.

### Part 2 (55 pts)

*Please use this space to detail your approach and solutions for part 2. Don't forget to upload your completed source code to this /writeup directory as well!*
