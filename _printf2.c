#include "printf.h"

/**
 * _printf - printf output according to format
 * @format: format to go by
 *
 * Return: number of character printed excluding '\0_'
 */

int _printf(const char *format, ...)
{
	va_list ap;
	char buffer[BUFF_SIZE];
	int buffer_index = 0;
	char *str;

	va_start(ap, format);

	while (format != NULL && *format != '\0') /* check for empty arguments */
	{
		if (*format == '%') /* checks for conversion specifier */
		{
			++format; /* move past % */

			switch(*format)
			{
				case 'c':
					buffer[buffer_index++] = va_arg(ap, int);
					break;

				case 's':
					str = va_arg(ap, char *);

					while (*str != '\0')
					{
						buffer[buffer_index++] = *str;
						++str;
					}
					break;

				case '%':
					buffer[buffer_index++] = va_arg(ap, int);
					break;

				default:
					break;
			}
		}

		else
		{
			buffer[buffer_index++] = *format; /* check for regular values */
		}
		++format;
	}

	buffer[buffer_index] = '\0';

	va_end (ap);

	write(1, buffer, strlen(buffer)); /* print to stdout, the content of buffer */

	return (strlen(buffer)); /* return buffer lenght */
}
