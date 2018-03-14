//Justin Johnson
//A01936095
//Big Integer Part2
#include <iostream>
#include "BigInteger.hpp"
#include <iomanip>
// ------------------------------------------------------------------
// 
// Site to compare long factorial results: http://www.dcode.fr/factorial 
// 
// ------------------------------------------------------------------

using namespace std;

BigInteger factorial(BigInteger value) {
    BigInteger result(1);
    for (BigInteger next = 1; next <= value; next++) {
        result *= next;
    }
    
    return result;
}

int main() {
    BigInteger one(1234); 
    BigInteger two(9999); 
    BigInteger result = one + two; 
    cout << "one + two = " << result << endl; 
    cout << "one + two (as double) = " << static_cast<double>(result) <<  endl;
    one += two;
    cout << "one += two = " << one << endl;
    BigInteger three("1234567890");
    BigInteger four("123456789");
    BigInteger result2 = three * four;
    cout << "three * four = "  << result2 << endl;
    three *= four;
    cout << "three *= four = " << three << endl;
    BigInteger f = factorial(123);
    cout << "factorial of 123 is: " << f << endl; 
    BigInteger factorialFromWeb("12146304367025329675766243241881295855454217088483382315328918161829235892362167668831156960612640202170735835221294047782591091570411651472186029519906261646730733907419814952960000000000000000000000000000");
    if (f == factorialFromWeb) {
    cout << "My factorial result matches!!" << endl;
    } else {
    cout << "Still work left to do..." << endl;
    } 

    return 0;
}
