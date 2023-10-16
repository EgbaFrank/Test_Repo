#include <stdio.h>
#include "printf.h"

/**
 * main - test for custom printf function
 *
 * Return: void
 */

int main(void)
{
	char char_test = 'T';
	char *str_test = "This is a printf test";
	int count1, count2;

	count1 = printf("String: [%s]\n", str_test);
	count2 = _printf("String: [%s]\n", str_test);

	printf("%d %d\n", count1, count2);

	count1 = printf("Character: [%c]\n", char_test);
	count2 = _printf("Character: [%c]\n", char_test);

	printf("%d %d\n", count1, count2);

	return (0);
}
