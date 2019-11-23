#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <sys/stat.h>
#include <fcntl.h>

#include <openssl/rand.h>

#include "crypto.h"

#define LEDGER_FILE "ledger.bin"
#define PERMISSIONS (S_IRUSR | S_IWUSR)

// This program implements a brute force attack to crack the ledger file
int main(int argc, char **argv) {
    int fd = open(LEDGER_FILE, O_RDONLY, PERMISSIONS);
    unsigned char fd_key_hash[16];
    read(fd, fd_key_hash, 16);



   // First we create a string that contains all the possible characters
   char chars[] = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
   
   char key[] = "    "; //The test key that we will use to iterate through all possible keys
   char* hash;
   for (int i = 0; i < 62; i++) {
       key[0] = chars[i];
       for (int j = 0; j < 62; j++) {
           key[1] = chars[j];
           for (int k = 0; k < 62; k++) {
               key[2] = chars[k];
               for (int l = 0; l < 62; l++) {
                   key[3] = chars[l];

                    //Hash the key with MD5
                    hash = md5_hash(key, 4); 
                    //Rehash the first 2 bytes as is done in the ledger code
                    memset(hash+ 2, 0, 14);
                    hash = md5_hash(hash, 2);

                   //Verify key -> If it matches print the key
                   if (memcmp(hash, fd_key_hash, 16) == 0) {
                       printf("%s\n", key);
                       return 1;
                   }
               } 
           }
       }
   }
   printf("Failed");
    return 0;

}