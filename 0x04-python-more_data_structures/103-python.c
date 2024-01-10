#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <listobject.h>
#include <bytesobject.h>
#include <stdio.h>

/**
 * print_python_list - Prints basic info about Python lists
 * @p: Python list object
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, alloc, i;
	PyObject *item;

	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	size = PyList_Size(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", alloc);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

/**
 * print_python_bytes - Prints basic info about Python bytes objects
 * @p: Python bytes object
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *string;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	string = PyBytes_AsString(p);

	printf("  size: %zd\n", size);
	printf("  trying string: %s\n", string);
	printf("  first %zd bytes:", (size < 10) ? size + 1 : 10);

	for (i = 0; i < size && i < 10; i++)
	{
		printf(" %02x", string[i] & 0xff);
	}

	printf("\n");
}

/**
 * main - Entry point for the program
 * Return: Always 0 (Success)
 */
int main(void)
{
	return (0);
}
