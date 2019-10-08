#include <iostream>
using namespace std;

int maj(int x, int y, int z){
    if(x+y+z < 2){
        return 0;
    }else
        return 1;
}
{
int mod2(int x)
    if( (x % 2) != 1){
        return 0;
    }
    else return 1;
}

int a5(int *X, int *Y, int *Z){
    int output = mod2(X[18] + Y[21] + Z[22]);
    int m = maj(X[8], Y[10], Z[10]);
    if (X[8] == m){
        int first = mod2(X[13] + X[16] + X[17] + X[18]);
        for(int i = 18; i > 1; i--){
            X[i+1]= X[i];
        }
        X[0] = first;
    }
    if (Y[10] == m){
        int first = mod2(Y[20] + Y[21]);
        for(int i = 21; i > 1; i--){
            Y[i+1] = Y[i];
        }
        Y[0] = first;
    }
    if (Z[10] == m){
        int first = mod2(Z[20] + Z[21] + Z[22]);
        for(int i = 22; i > 1; i--){
            Z[i+1] = Z[i];
        }
        Z[0] = first;
    }
    return output;
}

int main() {
//    std::cout << "Hello, World!" << std::endl;
    int X[] = {1,1,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1};
    int Y[] = {1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1};
    int Z[] = {1,1,1,0,0,0,0,1,1,1,1,0,0,0,0,1,1,1,1,0,0,0,0};
    for(int i = 0; i < 10; i++) {
        cout << a5(X, Y, Z);
//        cout<< a5(X, Y, Z)<<endl;
//        for(int j =0; j < 19; j++){
//            cout<<X[j] <<" ";
//        }
//        cout<<endl;
    }
}