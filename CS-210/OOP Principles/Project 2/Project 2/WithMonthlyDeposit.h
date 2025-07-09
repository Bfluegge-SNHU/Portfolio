#ifndef PROJECT2_WITHMONTHLYDEPOSIT_H //Conditional only calls definition once to prevent compiler warnings
#define PROJECT2_WITHMONTHLYDEPOSIT_H //Definition

class WithMonthlyDeposit
{
	public: // public definitions
		WithMonthlyDeposit();

		double GetInitialAmount();
		void SetInitialAmount(double amount);

		int GetMonthlyDeposit();
		void SetMonthlyDeposit(int deposit);

		double GetAnnualInterest();
		void SetAnnualInterest(double interest);

		int GetNumYears();
		void SetNumYears(int years);

	private: // private definitions
		double initialAmount;
		double annualInterest;
		int monthlyDeposit;
		int numYears;
};

#endif

