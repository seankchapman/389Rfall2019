# Writeup 3 - OPSEC and SE

Name: Sean Chapman
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Sean Chapman

## Assignment Writeup

### Part 1 (40 pts)
In the previous writeup I figured out Eric Norman's address by running whois on wattsamp.net. Using this information, I would go to his house posing as a solicitor for a bank and attempt to sell him on our services. In the process, I would ask questions like what bank he currently uses, where he is from, etc. Later, I would  call Eric Norman, using the phone number that I found in the previous writeup, pretending to be from his bank. I would claim that there has been a recent security breach and even though his information has not been affected, he needs to set up new security questions. I would then ask for his card's pin number as "verification" before proceeding to ask what his mother's maiden name is, what browser he uses, and the name of his first pet. Alternatively, to get his pin nunmber I could follow Eric Norman and try to watch him type his pin number at a cash register. To get his web browser, I could ask him to download a chrome extension and monitor his response.

### Part 2 (60 pts)

The first vulnerability that I would ask Eric Norman to patch would be the open port that leads to his back-end login portal.  By closing this port or setting up a firewall, he can limit access to any malicious actors and provide increased security. Next, I would ask him to pick a less vulnerable password, preferrably a random alphanumerical string, or at least something that is not in rockyou.txt and is not solely based on personal information (like birthdays, etc). Lastly, in order to prevent malicious actors from getting his personal information, I would recommend that he uses something like WhoisGuard. Currently, running whois on wattsamp.net provides anyone with lots of his personal information that could be used against him. By protecting this information, he would make it harder for malicious actors to socially engineer more information about him.