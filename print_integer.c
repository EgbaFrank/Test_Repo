#include "printf.h"

/**
 * print_integer - prints integer in decimal, hexadecimal and octal
 * @n: input integer
 * @base: base for n to be converted to
 *
 * Return: no. of printed integers
 */

int print_integer(int n)
{
	int digits_printed;

	if (n == 0) /* base case when n is 0 */
	{
		putchar('0');
		return (1);
	}
	if (n < 0)
	{
		putchar('-');
		n = -n;
		digits_printed++;
	}
	if (n >= 10)
	{
		print_number(n / 10);
		digits_printed++;
	}

	putchar((n % 10) + '0');
	return (digits_printed + 1);
}
