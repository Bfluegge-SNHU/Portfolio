#ifndef PROJECT2_PRINTFORMAT_H
#define PROJECT2_PRINTFORMAT_H

class PrintFormat // formats tables
{
	public:
		void PrintData(double amount, int deposit, double interest, int years);

		void PrintTablesNoDeposit(double amount, double interest, int year);

		void PrintTablesDeposit(double amount, double interest, int deposit, int years);
};

#endif

