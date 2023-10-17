#include "printf.h"

/**
 * main - test the printf function
 *
 * Return: _0 if successful
 */

int main(void)
{
	int n = 98;
	char c = 'C';
	char *s = "This is a printf test";
	int len1, len2;

	printf("Character: [%c]\n", c);
	_printf("Character: [%c]\n", c);

	len1 = printf("String: [%s]\n", s);
	len2 = _printf("String: [%s]\n", s);

	printf("Percent: [%%]\n");
	_printf("Percent: [%%]\n");

	printf("Integer I: [%i]\n", n);
	_printf("Integer I: [%i]\n", n);

	printf("Integer D: [%d]\n", n);
	_printf("Integer D: [%d]\n", n);

	printf("printf %d, _printf %d\n", len1, len2);

	return (0);
}
