//A palindromic number reads the same both ways.
// The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
//Find the largest palindrome made from the product of two 3-digit numbers.

#include <iostream>
#include <vector>
#include <string>

using namespace std;

bool isPalindrome(const string& word, int begin, int end) {
    if(begin >= end) return true;
    if(word[begin]==word[end]) return isPalindrome(word, begin+1, end-1);
    return false;
}

//finds palindromes made from the product of two 3-digit numbers (100-999)
void findPalindrome() {
    string temp;
    int largest = 0;
    for(int i = 100; i <= 999; ++i) {
        for(int j = 100; j <= 999; ++j) {
            temp = to_string(i*j);
            if(isPalindrome(temp, 0, static_cast<int>(temp.length()-1))) {
                if(i*j > largest) largest = i*j;
//                printf("%d * %d = %d :: IS A PALINDROME\n",i,j,i*j);
            }
        }
    }
    printf("%d is the largest PALINDROME", largest);
}

int main() {
//    string foo = to_string(5005005);
//    if(isPalindrome(foo, 0, static_cast<int>(foo.length()-1))){
//        cout << "YES";
//    }
    findPalindrome();

    return 0;
}
