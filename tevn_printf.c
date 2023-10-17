#include <stdarg.h>
#include <stdio.h>
#include <stdlib.h>

/**
 * _printf - produces output according to a format
 * @format: character string
 *
 * Return: no. of characters printed (excluding the null byte)
 */

int _printf(const char *format, ...) 
{
	va_list args;
	int chars_printed = 0;
	const char *ptr = format;
	char c;
	char *str;
	int n;

	va_start(args, format);

	while (*ptr) /* iterate the entire string excludig null */
	{
		if (*ptr == '%') /* if there is a format specifier */
		{
			ptr++; /* move to the next character*/
			if (*ptr == 'c')
			{
				c = va_arg(args, int); /* int cause its stored in ASCII*/
				putchar(c);
				chars_printed++;
			}
			else if (*ptr == 's')
			{
				str = va_arg(args, char *);
				while (*str)
				{
					putchar(*str);
					chars_printed++;
					str++;
				}
			}
			else if (*ptr == '%')
			{
				putchar('%');
				chars_printed++;
			}
			else if (*ptr == 'd' || *ptr == 'i')
			{
				n = va_arg(args, int);
				chars_printed += print_integers(n);
			}

		}
		else /* if there is no format specifier print whatever input*/
		{
			putchar(*ptr);
			chars_printed++;
		}
		ptr++;
	}

	va_end(args);
	return (chars_printed); /* no of chars printed */
}

