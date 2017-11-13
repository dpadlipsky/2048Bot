#include <iostream>
#include <string>
#include <cmath>
#include <fstream>
using namespace std;

const double increaseMulti = 0;
const double sameMulti = 50;
const double cornerMulti = 100;
const double emptyMulti = 1000;
const size_t MAX = pow(2,16);

int main(){
    int count =  0;
    ofstream out;
    out.open("./Cases.txt");
    for (size_t i = 1; i <= MAX; i = 2*i){
        for (size_t j = 1; j <= MAX; j = 2*j){
            for (size_t k = 1; k <= MAX; k = 2*k){
                for (size_t l = 1; l <= MAX; l = 2*l){
                    count++;
                    //BASE TO SCALE ALL VALUES OFF OF
                    double base = log2(i)+log2(j)+log2(k)+log2(l);
                    double value = 0;
                    //INCREASING LEFT TO RIGHT
                    if (i<=j&&j<=k&&k<=l){
                        if (!(i==1&&i==j&&i==k)){
                            value += base*increaseMulti;
                        }
                    }
                    //INCREASING RIGHT TO LEFT
                    if (i>=j&&j>=k&&k>=l){
                        if (!(l==1&&l==j&&l==k)){
                            value += base*increaseMulti;
                        }
                    }
                    //CHECKS TO SEE IF IT IS THE SAME AS IN A ROW
                    if ((i==j||(i==k&&j==1)||(i==l&&j==1&&k==1))&&i!=1){
                        value +=base*sameMulti;
                    }
                    //SEE ABOVE
                    if ((j==k||(j==l&&k==1))&&j!=1){
                        value += base*sameMulti;
                    }
                    //SEE ABOVE
                    if ((k==l&&k!=1)){
                        value += base*sameMulti;
                    }
                    //CHECKS FOR EMPTY SPACE
                    if (i==1){
                        value += emptyMulti;
                    }
                    //SEE ABOVE
                    if (j==1){
                        value += emptyMulti;
                    }
                    //SEE ABOVE
                    if (k==1){
                        value += emptyMulti;
                    }
                    //SEE ABOVE
                    if (l==1){
                        value += emptyMulti;
                    }
                    //CHECKS FOR BIGGEST NUMBER ON LEFT SIDE
                    if (i > j&& i > k&& i > l){
                        value += log2(i)*cornerMulti;
                    }
                    //CHECKS FOR BIGGEST NUMBER ON RIGHT SIDE
                    if (l>j&&l>k&&l>i){
                        value += log2(l)*cornerMulti;
                    }
                    value += base;
                    out<<value<<endl;
                }
            }
        }
    }
}
