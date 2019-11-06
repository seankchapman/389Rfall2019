Binaries II
======

## Assignment details

This assignment has one part. It is due 11/4 at 11:59pm.
To submit your homework, please follow the guidelines on the front page to edit the README in the /writeup folder and push your completed work to GitHub.


**There will be a late penalty of 5% off per day late!**

### Part 1 (100 pts)
Answer the following questions regarding the server executable (for which source is provided).

1. How is the per-session administrator password generated? Are there any inherent weaknesses in this implementation?

The password is generated at runtime, using the time at which the program is run. This method of security is vulnerable because malicious actors may be able to read the password from memory.

2. Describe two vulnerabilities in this program. Provide specific line numbers and classifications of the vulnerability. Explain potential ramifications as well as ways to avoid these vulnerabilities when writing code.

One vulnerability is found in the printf statement on line 46 of the program. This print statement is vulnerable as it allows the user to format the input string in any way they like. This allows users to print memory addresses from the stack by using format specifiers such as %d, %x, %f, and others. This can be avoided by having an explicit format specifier in the print statement. An example would be to change the print statement to something like `printf(%s, input_string)'. 

Another vulnerability is that a buffer overflow attack is possible on line 68 of the program. The programmer does not specify the number of bytes that are to be read, allowing an attacker to compromise the program by inputting more bytes than the buffer size. To fix this, the programmer should use `fgets` which allows a restriction on the maximum number of bytes to be read.

3. What is the flag?

CMSC389R-{expl017-2-w1n}

4. Describe the process you followed to obtain the flag: vulnerabilities exploited, your inputs to the server in a human-readable format, etc. If you create any helper code please include it.

I first utilized the format string attack that I mentioned in Part 2 in order to find out the password that I could use to gain authentication. To do this, I used the format '%29$s' on the `printf` statement in the cipher function. Doing this yielded the password. I then was able to authenticate the password and gain access to the server with admin privileges. I then explored the server using the command line. Running the `ls` command revealed a file called `flag` in the current directory. I then attempted to run `cat flag` on the file to read its contents, but this was unsuccessful. In order to gain access to the file, I exploited the buffer overflow attack that I mentioned in Part 2. Using the input `cat flag cat flag cat flag` overloaded the buffer and allowed me to read the contents of the flag file.


### Tips
Before even bothering to connect to the remote host, try running and attacking
the binary locally. Determine the steps that you would have to follow to locate
and dump a flag from the remote server. You are given both the source and the
compiled binaries: it will be immensely helpful to you to either a) run
program in GDB to get an idea of what's going on or b) add print statements
to the binary to confirm your idea of what's going on. If you edit / recompile
the file, it may not produce the exact same binary. As such, you should make
sure that any attack you execute works on the original binary.

Break the problem down into subcomponents. What is my objective? How can I get closer to that?
What functions will I have to call to do so? What inputs will I have to provide to these functions?

Good luck!
