#ifndef PRINTF_H
#define PRINTF_H

#include <stdarg.h>
#include <unistd.h>
#include <string.h>
#include <stdio.h>

#define BUFF_SIZE 1024
int _printf(const char *format, ...);
int print_integer(int n);

#endif /* PRINTF_H */
