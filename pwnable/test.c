//getsTest.c
#include <stdio.h>
#include <string.h>
int main(){
 char buff[10]; //allocate memory for a character array of size 10
 int flag;
 printf("Enter the password:");
 gets(buff);
 if(!strcmp(buff,"password")) 
    flag = 1;  //if 'password' is entered, set flag=1
 if(flag != 0) printf("Correct!\n Access Granted\n");
 else printf("Incorrect!\n Access Denied\n");
}