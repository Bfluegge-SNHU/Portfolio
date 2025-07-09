#include "WithoutMonthlyDeposit.h"

WithoutMonthlyDeposit::WithoutMonthlyDeposit() {
	initialAmount = 1.00;
	annualInterest = 5.0;
	numYears = 5;
}

double WithoutMonthlyDeposit::GetInitialAmount() {
	return initialAmount;
}
void WithoutMonthlyDeposit::SetInitialAmount(double amount) {
	initialAmount = amount;
}

double WithoutMonthlyDeposit::GetAnnualInterest() {
	return annualInterest;
}
void WithoutMonthlyDeposit::SetAnnualInterest(double interest) {
	annualInterest = interest;
}

int WithoutMonthlyDeposit::GetNumYears() {
	return numYears;
}
void WithoutMonthlyDeposit::SetNumYears(int years) {
	numYears = years;
}
