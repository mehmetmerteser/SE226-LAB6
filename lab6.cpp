#include <iostream>
 
 using namespace std;
 
 
 double harmonicSeries(int n) {
     if (n == 1)
         return 1.0;
     return 1.0 / n + harmonicSeries(n - 1);
 }
 
 
 double harmonicSeries() {
     int n;
     cout << "Enter n: ";
     cin >> n;
     return harmonicSeries(n);
 }
 
 int main() {
     cout<<"Enter n for first operation: ";
     int n;
     cin>>n;
     cout << "Harmonic Series H() = " << harmonicSeries(n) << endl;
     cout << "Harmonic Series H(n) = " << harmonicSeries() << endl;
     return 0;
 }
