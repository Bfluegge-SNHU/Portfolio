#include "PrintFormat.h"
#include <iostream>
#include <iomanip>
using namespace std;

//Formats user data
void PrintFormat::PrintData(double amount, int deposit, double interest, int years) {
	cout << "-------------------------------------" << endl;
	cout << "------------- Data Input ------------" << endl;
	cout << "Initial investment amount:   $ " << amount << endl;
	cout << "Monthly deposit:             $ " << deposit << endl;
	cout << "Annual interest:             % " << interest << endl;
	cout << "Number of years:               " << years << endl;
	cout << endl;
}

//Prints tables without monthly deposit
void PrintFormat::PrintTablesNoDeposit(double amount, double interest, int years) {
	interest = interest / 100.0;

	cout << "   Yearly Total Without Monthly Deposits:   " << endl;
	cout << "--------------------------------------------" << endl;
	cout << "|   Year:   |   Balance:   |   Interest:    |" << endl;
	cout << "--------------------------------------------" << endl;
	
	for (int i = 0; i < years; ++i) {
		cout << "|     " << i + 1 << "     |      " << fixed << setprecision(2) << amount << "    |      " << fixed << setprecision(2) << interest << "      |" << endl;
		interest = amount * interest;
		amount = amount + interest;
		cout << "--------------------------------------------" << endl;
	}
}

// Prints tables with monthly deposit
// FIXME: I could not get the interest math to work correctly on this portion
void PrintFormat::PrintTablesDeposit(double amount, double interest, int deposit, int years) { 
	double monthlyInterest = (amount + deposit) * ((interest / 100) / 12);

	cout << "    Yearly Total With Monthly Deposits:   " << endl;
	cout << "--------------------------------------------" << endl;
	cout << "|   Year:   |   Balance:   |   Interest:    |" << endl;
	cout << "--------------------------------------------" << endl;

	for (int i = 0; i < years; ++i) {												//for loop to print each year
		for (int v = 0; v < 12; ++v) {
			double interestCalc = (amount + deposit) * ((interest / 100) / 12);     //for loop to calculate monthly compound interest
			monthlyInterest = monthlyInterest + interestCalc;
			amount = amount + deposit + interestCalc;
		}
		cout << "|     " << i + 1 << "     |     " << fixed << setprecision(2) << amount << "    |     " << fixed << setprecision(2) << monthlyInterest << "      |" << endl;
		cout << "--------------------------------------------" << endl;
	}
}