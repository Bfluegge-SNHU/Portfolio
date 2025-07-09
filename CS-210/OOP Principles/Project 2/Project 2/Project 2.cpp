/*06/06/25
* Brandon Fluegge
* Project 2
* CS-210
*/

#include <iostream>
#include "WithoutMonthlyDeposit.h"
#include "WithMonthlyDeposit.h"
#include "PrintFormat.h"
using namespace std;


int main()
{
	double initialAmount;
	double annualInterest;
	int monthlyDeposit;
	int numYears;
	char temp;
	char menuInput = '0';

	//Input prompts
	cout << "Enter initial investment amount: " << endl;
	cin >> initialAmount;
	cout << "Enter annual interest rate: " << endl;
	cin >> annualInterest;
	cout << "Enter your monthly deposit " << endl;
	cin >> monthlyDeposit;
	cout << "Enter the number of years: " << endl;
	cin >> numYears;
	cout << "Press any key to continue...";
	cin >> temp;

	//while loop for menu options
	while  (menuInput != '5') {

	//prints user data
		PrintFormat Data1;
		Data1.PrintData(initialAmount, monthlyDeposit, annualInterest, numYears);

		//assigns user data to table with no monthly deposit
		WithoutMonthlyDeposit Table1;
		Table1.SetInitialAmount(initialAmount);
		Table1.SetAnnualInterest(annualInterest);
		Table1.SetNumYears(numYears);

		//assigns user data to table with monthly deposit
		WithMonthlyDeposit Table2;
		Table2.SetInitialAmount(initialAmount);
		Table2.SetAnnualInterest(annualInterest);
		Table2.SetMonthlyDeposit(monthlyDeposit);
		Table2.SetNumYears(numYears);


		//Prints tables
		Data1.PrintTablesNoDeposit(Table1.GetInitialAmount(), Table1.GetAnnualInterest(), Table1.GetNumYears());
		cout << endl;
		Data1.PrintTablesDeposit(Table2.GetInitialAmount(), Table2.GetAnnualInterest(), Table2.GetMonthlyDeposit(), Table2.GetNumYears());
		
		// menu options
		cout << endl;
		cout << "Would you like to change information?" << endl;
		cout << "1 - Initial investment" << endl;
		cout << "2 - Monthly deposit" << endl;
		cout << "3 - Interest rate" << endl;
		cout << "4 - Number of years" << endl;
		cout << "5 - Quit" << endl;
		cin >> menuInput;

		switch (menuInput) {   //switch for input for changes by user
		case '1':
			cout << "Enter initial investment amount: " << endl;
			cin >> initialAmount;
			Table1.SetInitialAmount(initialAmount);
			Table2.SetInitialAmount(initialAmount);
			break;

		case '2':
			cout << "Enter your monthly deposit " << endl;
			cin >> monthlyDeposit;
			Table2.SetMonthlyDeposit(monthlyDeposit);
			break;

		case '3':
			cout << "Enter annual interest rate: " << endl;
			cin >> annualInterest;
			Table1.SetAnnualInterest(annualInterest);
			Table2.SetAnnualInterest(annualInterest);
			break;

		case '4':
			cout << "Enter the number of years: " << endl;
			cin >> numYears;
			Table1.SetNumYears(numYears);
			Table2.SetNumYears(numYears);
			break;
		}

	}

	return 0;
}

