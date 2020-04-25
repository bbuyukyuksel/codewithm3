#include <stdio.h>
#include <stdlib.h>
unsigned long long prime(unsigned long long);
unsigned long long largestPrimeDivisor(unsigned long long);
int main(){
    system("color a && title Problem 3");
    printf("%llu\n", 600851475143);
    printf("%llu",largestPrimeDivisor(600851475143));
    return 0;
}
unsigned long long largestPrimeDivisor(unsigned long long x){
    unsigned long long i;
    unsigned int counter=1;
    unsigned long long largest = 0,before = 0;

    for(i = 2; i<= (x+1)/2; i++){
        if(x % i == 0){
            if(i > largest && prime(i))
                largest = i;
                if(before != largest){
                    printf("\nSearcing..\n");
                    printf("#%2llu : %10llu\n",counter++,largest);
                    before = largest;
                }
        }
    }
    return largest;
}
unsigned long long prime(unsigned long long x){
    unsigned long long i;
    for(i=2; i <(x+1)/2; i++){
         if(x%i == 0){
            return 0;
         }
    }
    return 1;
}
