# Writeup 9 - Forensics II

Name: Sean Chapman
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Sean Chapman


## Assignment details

### Part 1 (45 Pts)
1. Warmup: what IP address has been attacked?

142.93.136.81

2. What kind of assessment tool(s) were the attackers using against the victim machine? List the name(s) of the tool(s) as well.

The attackers used nmap to scan for open ports. We can tell tell they did this because in the pcap file we see many packets that were sent with no data. The only thing changing between these packets are the ports, indicating they were testing for an open port.

3. What are the hackers' IP addresses, and where are they connecting from?

159.203.113.181. The hackers are attacking from Clifton, US.

4. What port are they using to steal files on the server?

The hackers are communicating with the server on port 21, and the server is communicating with the hackers on port 55914.

5. Which file did they steal? What kind of file is it? Do you recognize the file?

The hackers stole the file `find_me.jpeg`. It is a JPEG image file. I do not recognize this file.

6. Which file did the attackers leave behind on the server?

The hackers stored the file greetz.fpff on the server. After downloading the file using Wireshark, we can run the command `strings greetz.fpff` to find the flag, `CMSC389R-{h0pefully_y0u_didnt_grep_CMSC389R}`.

7. What is a countermeasure to prevent this kind of intrusion from happening again? Note: disabling the vulnerable service is *not* an option.

The attack was carried out by using nmap to discover open ports. This is a form of active reconnaissance, which can be detected by the server being attacked. To prevent this attack from being carried out in the future, they can build in active reconnaissance detection, and blacklist any IPs that they find trying search for open ports.

### Part 2 (55 Pts)

When was `greetz.fpff` generated?

2019-03-27 00:15:05

 Who authored `greetz.fpff`?

 fl1nch

 List each section, giving us the data in it *and* its type.

 Section 1:
 - Type: 1
 - Length: 24
 - Data: 'Hey you, keep looking :)'
 
 Section 2:
 - Type: 6
 - Length: 16
 - Data: (52.336035, 4.880673)

 Section 3: 
 - Type: 8
 - Length: 202776
 - Data: PNG saved to embedded_png.png

 Section 4:
 - Type: 1
 - Length: 44
 - Data: '}R983CSMC_perg_tndid_u0y_yllufep0h{-R983CSMC'

 Section 5:
 - Type: 1
 - Length: 89
 - Data: 'Q01TQzM4OVIte2hleV9oM3lfeTBVX3lvdV9JX2RvbnRfbGlrZV95b3VyX2Jhc2U2NF9lbmNvZGluZ30='

Flags:
- `CMSC389R-{h0pefully_y0u_didnt_grep_CMSC389R}`
- `CMSC389R-{w3lc0me_b@ck_fr0m_spr1ng_br3ak}`