#include <iostream>
#include <fstream>
#include "math.h"
#include "locale.h"

using namespace std;
const int n1 = 30;
const int n2 = 31;
const int n3 = 32;
int register_L1[n1];
int register_L2[n2];
int register_L3[n3];

int work_of_L1()
{
	int a = 0;
	a = (register_L1[0] + register_L1[1] + register_L1[4] + register_L1[6]) % 2;
	int b = register_L1[0];
	for (int i = 0; i < n1 - 1; i++)
	{
		register_L1[i] = register_L1[i + 1];
	}
	register_L1[n1 - 1] = a;
	return b;
}
int work_of_L2()
{
	int a = 0;
	a = (register_L2[0] + register_L2[3]) % 2;
	int b = register_L2[0];
	for (int i = 0; i < n2 - 1; i++)
	{
		register_L2[i] = register_L2[i + 1];
	}
	register_L2[n2 - 1] = a;
	return b;
}
int work_of_L3()
{
	int a = 0;
	a = (register_L3[0] + register_L3[1] + register_L3[2] + register_L3[3] + register_L3[5] + register_L3[7]) % 2;
	int b = register_L3[0];
	for (int i = 0; i < n3 - 1; i++)
	{
		register_L3[i] = register_L3[i + 1];
	}
	register_L3[n3 - 1] = a;
	return b;
}
int Geffe()
{
	int z = 0;
	int x = work_of_L1();
	int y = work_of_L2();
	int s = work_of_L3();
	if (s == 0)
		z = y;
	else
		z = x;
	return z;
}



int main()
{
	setlocale(LC_ALL, "Russian");
	double alpha = 0.01;

	for (int i = 0; i < n1; i++)
	{
		register_L1[i] = 0;
	}
	register_L1[0] = 1;
	for (int i = 0; i < n2; i++)
	{
		register_L2[i] = 0;
	}
	register_L2[0] = 1;
	for (int i = 0; i < n3; i++)
	{
		register_L3[i] = 0;
	}
	register_L3[0] = 1;

	double N = (2 * 6.013 + sqrt(3) * 2.326) * (2 * 6.013 + sqrt(3) * 2.326);
	double C = N / 4 + 2.326 * sqrt(3 * N) / 4;

	int n = ceil(N);
	int c = round(C);
	cout << "N* = " << n << endl;
	cout << "c = " << c << endl;

	int* z = new int[2048];
	ifstream in("text.txt");
	if (!in.is_open())
	{
		cout << "Файл невозможно открыть" << endl;
		return -1;
	}
	char a;
	for (int i = 0; i < 2048; i++)
	{
		z[i] = 0;
	}
	int t = 0;
	while (in.get(a))
	{
		if (a == '0')
		{
			z[t] = 0;
			t++;
		}
		if (a == '1')
		{
			z[t] = 1;
			t++;
		}
	}
	in.close();

	long long int coun = pow(2, n2);
	long long int coun1 = pow(2, n1);

	int* X = new int[n];
	for (int i = 0; i < n; i++)
	{
		X[i] = work_of_L1();
	}
	cout << endl;
	for (int i = 0; i < n; i++)
	{
		cout << X[i];
	}
	cout << endl;
	int* Y = new int[n];
	for (int i = 0; i < n; i++)
	{
		Y[i] = work_of_L2();
	}
	cout << endl;
	ofstream outL1;
	outL1.open("l1.txt");
	ofstream outL2;
	outL2.open("l2.txt");
	int L1_var_count = 0;
	int L2_var_count = 0;
	while (coun >= 0)
	{
		int R1 = 0;
		int R2 = 0;
		for (int i = 0; i < n; i++)
		{
			R2 += (Y[i] + z[i]) % 2;
			if (coun >= coun1)
			{
				R1 += (X[i] + z[i]) % 2;
			}
		}
		if (R2 < c)
		{
			for (int i = 0; i < n; i++)
			{
				outL2 << Y[i];
			}
			outL2 << "\n-\n";
			L2_var_count++;
		}
		if (R1 < c && coun >= coun1)
		{
			for (int i = 0; i < n; i++)
			{
				outL1 << X[i];
			}
			outL1 << "\n-\n";
			L1_var_count++;
		}
		for (int i = 0; i < n - 1; i++)
		{
			if (coun >= coun1)
			{
				X[i] = X[i + 1];
			}
			Y[i] = Y[i + 1];
		}
		if (coun >= coun1)
		{
			X[n - 1] = work_of_L1();
		}
		Y[n - 1] = work_of_L2();
		coun--;
	}
	outL1.close();
	outL2.close();
	cout << "Для первого регистра найдено  " << L1_var_count << "  кандидата" << endl;
	cout << "Для второго регистра найдено  " << L2_var_count << "  кандидата" << endl;
	ifstream inL("l1.txt");
	if (!inL.is_open())
	{
		cout << "Невозможно открыть файл!" << endl;
		return -1;
	}
	int** L1_variants = new int* [L1_var_count];
	for (int i = 0; i < L1_var_count; i++)
	{
		L1_variants[i] = new int[n];
		for (int j = 0; j < n; j++)
		{
			inL.get(a);
			if (a == '1')
				L1_variants[i][j] = 1;
			else
				L1_variants[i][j] = 0;
		}
		inL.get(a);
		inL.get(a);
		inL.get(a);
	}
	inL.close();
	inL.open("l2.txt");
	if (!inL.is_open())
	{
		cout << "Невозможно открыть файл!" << endl;
		return -1;
	}
	int** L2_variants = new int* [L2_var_count];
	for (int i = 0; i < L2_var_count; i++)
	{
		L2_variants[i] = new int[n];
		for (int j = 0; j < n; j++)
		{
			inL.get(a);
			if (a == '1')
				L2_variants[i][j] = 1;
			else
				L2_variants[i][j] = 0;
		}
		inL.get(a);
		inL.get(a);
		inL.get(a);
	}
	inL.close();
	int* S = new int[n];
	for (int i = 0; i < n; i++)
	{
		S[i] = work_of_L3();
	}

	int temp = L1_var_count * L2_var_count;
	int* difference = new int[temp];
	int** L3_var = new int* [temp];
	for (int i = 0; i < temp; i++)
	{
		L3_var[i] = new int[n];
		for (int j = 0; j < n; j++)
		{
			L3_var[i][j] = -1;
		}
		difference[i] = 0;
	}
	int l = 0;
	for (int i = 0; i < L1_var_count; i++)
	{
		for (int j = 0; j < L2_var_count; j++)
		{
			for (int k = 0; k < n; k++)
			{
				if (L1_variants[i][k] != L2_variants[j][k])
				{
					if (z[k] == L1_variants[i][k])
					{
						L3_var[l][k] = 1;
					}
					if (z[k] == L2_variants[j][k])
					{
						L3_var[l][k] = 0;
					}
					if (k < n3)
					{
						difference[l]++;
					}
				}
				else
				{
					if (z[k] != L1_variants[i][k])
					{
						k = n;
						difference[l] = 0;
					}
				}
			}
			l++;
		}
	}

	for (int l = 0; l < temp; l++)
	{
		if (difference[l] != 0)
		{
			coun = pow(2, n3 - difference[l]);
		}
		else
		{
			coun = 0;
		}
		for (int i = 0; i < coun; i++)
		{
			for (int j = 0; j < n; j++)
			{
				S[j] = 0;
			}
			t = 0;
			int q = 0;
			int div = 0;
			q = i % 2;
			div = i / 2;
			while (L3_var[l][t] != -1)
			{
				register_L3[t] = L3_var[l][t];
				t++;
			}
			register_L3[t] = q;
			while (div != 0)
			{
				q = div % 2;
				div /= 2;
				t++;
				while (L3_var[l][t] != -1)
				{
					register_L3[t] = L3_var[l][t];
					t++;
				}
				register_L3[t] = q;
			}
			for (int j = t; j < n3; j++)
			{
				if (L3_var[l][j] == -1)
				{
					register_L3[j] = 0;
				}
				else
				{
					register_L3[j] = L3_var[l][j];
				}
			}
			int k = 0;
			for (int j = 0; j < n; j++)
			{
				S[j] = work_of_L3();
				if (L3_var[l][j] == -1)
				{
					k++;
				}
				if (S[j] == L3_var[l][j])
				{
					k++;
				}
			}
			if (k == n)
			{
				int y1 = l / L2_var_count;
				int y2 = l % L2_var_count;
				for (int k = 0; k < n1; k++)
				{
					register_L1[k] = L1_variants[y1][k];
				}
				for (int k = 0; k < n2; k++)
				{
					register_L2[k] = L2_variants[y2][k];
				}
				for (int k = 0; k < n3; k++)
				{
					register_L3[k] = S[k];
				}
				for (int j = 0; j < 2048; j++)
				{
					if (z[j] == Geffe())
					{
						if (j == 2047)
						{
							cout << endl << endl;
							cout << "Начальное заполнения регистра L1:     ";
							for (int k = 0; k < n1; k++)
							{
								register_L1[k] = L1_variants[y1][k];
								cout << register_L1[k] << " ";
							}
							cout << endl << endl;
							cout << "Начальное заполнения регистра L2:     ";
							for (int k = 0; k < n2; k++)
							{
								register_L2[k] = L2_variants[y2][k];
								cout << register_L2[k] << " ";
							}
							cout << endl << endl;
							cout << "Начальное заполнения регистра L3:     ";
							for (int k = 0; k < n3; k++)
							{
								register_L3[k] = S[k];
								cout << register_L3[k] << " ";
							}
							cout << endl << endl;
							//i = coun;
							//l = temp;
						}
					}
					else
					{
						j = 2048;
					}
				}
			}
		}
	}


	for (int i = 0; i < L1_var_count; i++)
	{
		delete[] L1_variants[i];
	}
	delete[] L1_variants;
	for (int i = 0; i < L2_var_count; i++)
	{
		delete[] L2_variants[i];
	}
	delete[] L2_variants;
	delete[] difference;
	delete[] X;
	delete[] Y;
	delete[] S;
	return 0;
}