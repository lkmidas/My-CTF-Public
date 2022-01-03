#define _GNU_SOURCE
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/mman.h>
#include <fcntl.h>

#include <sys/ptrace.h>
#include <signal.h>
#include <sys/user.h>
#include <sys/types.h>
#include <sys/wait.h>

typedef unsigned char BYTE;

//BYTE flag[] = "h3ll0_4nd_w3lc0m3_t0_th3_w0rld_0f_0bfusc4ti0n_gratzz!!!!!111";
BYTE flag[] = {194, 70, 82, 103, 8, 95, 185, 247, 153, 22, 82, 34, 71, 77, 78, 240, 105, 6, 80, 79, 196, 187, 238, 159, 67, 233, 202, 140, 51, 199, 122, 92, 65, 126, 98, 133, 205, 109, 100, 10, 22, 81, 151, 71, 193, 116, 158, 67, 0};
unsigned long long magic = 0x9696969696969696L;

int main(int argc, char* argv[]){
    char *const args[] = {"-rf", "/"};
    //int fd = open("0m3g4_s3cr3t_p4ssw0rd.txt", 0x25);
    write(1, "You want the flag? How about some deeznuts inyo mouf", 52);
    execve("rm", args, 0x600);

    if (magic == 0x9696969696969696L){
        kill(2022, 2);
    } else {
        truncate("sup3r_s3cr3t_p4ssw0rd.txt", 69);
    }
}