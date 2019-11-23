# Writeup 10 - Crypto I

Name: Sean Chapman
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Sean Chapman


## Assignment details

### Part 1 (45 Pts)
1. The structure of the ledger file format can be found on lines  34-37 of the `ledger.c` file. From these lines we can deduce that the first 16 bytes contain the key hash, the next 16 bytes contain the cipher text hash. After that, the next 16 bytes are the initialization vector text, and the rest contains the cipher text.

2. The cipher text is encrypted using AES128 encryption, and then hashed using MD5 hashing. Wattsamp should not have used MD5 hashing, as it is susceptible to collisions, and has been deemed unstable and insecure since 2010. Since MD5 does not produce very long hashes, it can be cracked with brute force attacks.

3. By examining the properties of the ledger.bin file, we can see that it is 656 bytes. We determined in question 1 that the file format uses the first 48 bytes for the key hash, cipher text hash, and initialization vector, and the rest is the cipher text. This means that the cipher text must be 608 bytes. I wasn't able to derive anything else from the ledger.bin file before decrypting.

4. To ensure confidentiality, Wattsamp used AES128 to encrypt the cipher text. They then used MD5 hashing to hash the encrypted cypher text. For additional confidentiality, they took the first 2 bytes of the hashed cipher text and hashed them again using MD5. 

5. The application encrypts the cipher text using AES128, and then hashes it using MD5 to ensure integrity. The application establishes integrity because if the cipher text hash stored in the ledger does not match with the user's hashed cipher text input, the program will know that there was tampering. However, this is vulnerable because the hashed cipher text is stored in the ledger itself. We can bypass the program's integrity measures my modifying the cipher text hash stored in the ledger to match a modified cipher text.

6. The application ensures authenticity by comparing the key hashes of the ledger and the user input. This is executed on line 82 of the program, with the call to `memcmp`. The program is vulnerable here, because the key only uses 2 bytes. Since the key that the program uses is only 2 bytes, we can crack it by using a simple brute force attack.

7. To generate the initialization vector, the program randomly generates 16 bytes, and then stores it in the ledger. Since the initialization vector is generated randomly, it ensures that it will not be reused.

### Part 2 (45 Pts)

The code included in `crack.c` implements a brute force attack to get the ledger password. We iterate through every possible 4 digit key, hash it, and rehash the first 2 bytes. We then compare the key that we have generated to the one stored in the first 16 bytes of the ledger program. If the keys match, the program will print out the password. Running the program tells us that the password is `ajTF`. We can then run `./ledger` to get the flag, `CMSC389R-{k3y5p4c3_2_sm411}`.

### Part 3 (10 Pts)

Many modern systems are responsible for handling the personal information of millions, sometimes billions of people. Knowing this, it is incredibly important for programmers to protect their code by any means necessary, including additional layers of obfuscation. I believe that obfuscation is an important measure to prevent malicious actors from gaining access to sensitive personal information and company records. People in the open source community might argue in favor of Kerckhoff's principle, claiming that code should be open and free for all. This outlook is respectable, but the fact is that *not* utilizing obfuscation makes it much easier for hackers to gain access to sensitve information. Sharing code with the community is generally a good thing, but developers must draw a line in the sand when that code can help malicious actors gain unauthorized access to personal data or company records.