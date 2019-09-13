# Writeup 2 - OSINT

Name: Sean Chapman
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Sean Chapman

## Assignment Writeup

### Part 1 (45 pts)
1. Eric J. Norman

2. Eric Norman works at Wattsamp. Their website is wattsamp.net

3. Using the OSINT framework's username tools, specifically Namechk, we can see that there are some accounts registered under the username ejnorman84. There is a reddit account with the username ejnorman84 that has one comment about Texas in the r/energy subreddit. ejnorman84 is also a registered Instagram account. The Instagram account contains 3 posts, relating to energy and Texas Football. There is also a link on the Instagram account to wattsamp.net, the company where Eric Norman works. Running whois on wattsamp.net returns a lot of personal information about Eric Norman. His phone number is (202)-656-2837. His address is 1300 Adabel Drive, El Paso Texas, and his postal code is 79835. His email is ejnorman84@gmail.com.

4. Typing `ping wattsamp.net` yields 157.230.179.99 as the IP. I then ran this IP address through maxmind.com to get the location, which is  North Bergen, New Jersey, United States, North America, Postal Code 07047, Approximate coordinates 40.793, -74.0247. It is registered under
the organization Digital Ocean. Entering wattsamp.net into DNSDumpster also yields 4 additional IPs, which are 216.239.32.109, 216.239.34.109, 216.239.36.109, and 216.239.38.109.

5. So far the only hidden file I have found is /robots.txt, which contains a bonus flag.

6. I ran the command `nmap -p 1-2000 157.230,179.99` to find out what ports are open on the website's IP address. Ports 22, 80, and 1337 are open.

7. Running `nmap 157.230.179.99 -O` will scan for the server's operating system. By running this command I found that it is running Linux 2.4.x.

8. On the homepage of Wattsamp.net, I looked through the HTML and found the flag `*CMSC389R-{html_h@x0r_lulz}`. Running the website through DNSDumpster also gave me another flag, `*CMSC389R-{Do_you-N0T_See_this}`. There is another flag on wattsamp.net/robots.txt, which is `*CMSC389R-{n0_indexing_pls}`.


*Please use this space to writeup your answers and solutions (and how you found them!) for part 1.*

### Part 2 (75 pts)

From the HTML at the `/views/admin.html` endpoint on wattsamp.net, we can see a hint that indicates there is a backend login portal. We know the IP of the website, and earlier we found a hidden open port. Running the command 'nc 157.230.179.99 1337' takes us to this backend portal. We are immediately prompted with a captcha - a simple math problem. Then, the system prompts the user for a username and password to login. We assume that the username is `ejnorman84`, but the password could be anything. However, we have a massive list of 14 million possible passwords. With this information, we can write a Python script called `brute.py` that:
    ..1. Connects to the backend login portal
    ..2. Reads in the captcha, solves it, and sends it back to the server
    ..3. Enters a username and a possible password
    ..4. Repeats this process until the correct password is found.

We run the script with `python3 brute.py` and after waiting a while, we find the password: `hello1`. We can now login to the backend server
and navigate the system shell. The flag can `CMSC389R-{!enough_nrg_4_a_str0ng_Pa$$wrd}` can be found in `/home/flag.txt`.
