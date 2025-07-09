#ifndef PROJECT2_WITHOUTMONTHLYDEPOSIT_H
#define PROJECT2_WITHOUTMONTHLYDEPOSIT_H


class WithoutMonthlyDeposit // class for no monthly deposit
{
	public:   //public definitions
		WithoutMonthlyDeposit();

		double GetInitialAmount();
		void SetInitialAmount(double amount);

		double GetAnnualInterest();
		void SetAnnualInterest(double interest);

		int GetNumYears();
		void SetNumYears(int years);

	private: //private definitions
		double initialAmount;
		double annualInterest;
		int numYears;
};

#endif

