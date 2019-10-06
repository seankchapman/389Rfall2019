# Writeup 2 - Pentesting

Name: Sean Chapman
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Sean Chapman

## Assignment Writeup

### Part 1 (45 pts)

The flag CMSC389R-{p1ng_as_a_$erv1c3} is found by running the command  `1 & cat /home/flag.txt`. To find the flag I first connected to the server and ran the command `1 & ls` to see what directories I could navigate to. I then ran the command `1  & ls /home/` to see what was in the home directory, and that is where I found the flag.txt file. Running `cat` on that file produced the flag. The key mistake that Eric Norman made was assuming that the input to his program would not be malicious. To protect himself from this vulnerability, he should utilize **input sanitization** by removing any unexpected characters from the input before passing it to the `ping` command. Since the `ping` command only expects either an IP address or a URL, Eric Norman should filter out any characters that would not normally appear in these two formats. For instance, &, |, and ; should all be  filtered from the  original input before being processed.

### Part 2 (55 pts)

We have gained access to Eric Norman's system, but navigating it is inconvenient because the server kicks you off after executing one command. A side effect of this is that path states are not saved in between commands (ie. the  `cd` command will not work). In order to make it easier to navigate the system that we have gained access to, we can write an interactive shell that will maintain the path state in between connections. Any time we run a command in our shell, the program will connect to Eric Norman's server and execute that command with the appropriate path. The shell that I wrote waits for user input and, upon receiving said input, checks if it is an `exit` or `quit` command. if the user uses the `shell` command, they will drop into an interactive shell that can be used to navigate Eric Norman's server. This works by taking in a new command, connecting to the server, and then running that command by using the command injection exploit that we found in Part 1. The shell keeps track of the user's path, so that if the user uses the `cd` command, the next command they run will use the appropriate path.