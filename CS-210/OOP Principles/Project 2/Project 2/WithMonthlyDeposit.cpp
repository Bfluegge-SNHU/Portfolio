#include "WithMonthlyDeposit.h"

//constructor
WithMonthlyDeposit::WithMonthlyDeposit() {
	initialAmount = 1.00;
	annualInterest = 5.0;
	monthlyDeposit = 50;
	numYears = 5;
}

//mutators and accessors

double WithMonthlyDeposit::GetInitialAmount() {
	return initialAmount;
}
void WithMonthlyDeposit::SetInitialAmount(double amount) {
	initialAmount = amount;
}

double WithMonthlyDeposit::GetAnnualInterest() {
	return annualInterest;
}
void WithMonthlyDeposit::SetAnnualInterest(double interest) {
	annualInterest = interest;
}

int WithMonthlyDeposit::GetMonthlyDeposit() {
	return monthlyDeposit;
}
void WithMonthlyDeposit::SetMonthlyDeposit(int deposit) {
	monthlyDeposit = deposit;
}

int WithMonthlyDeposit::GetNumYears() {
	return numYears;
}
void WithMonthlyDeposit::SetNumYears(int years) {
	numYears = years;
}
