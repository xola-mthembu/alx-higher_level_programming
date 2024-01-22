#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>

/**
 * print_python_list - Prints basic info about Python lists
 * @p: PyObject list object
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *item;

	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		fprintf(stderr, "  [ERROR] Invalid List Object\n");
		return;
	}

	size = PyList_Size(p);
	printf("[*] Size of the Python List = %zd\n", size);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

/**
 * print_python_bytes - Prints basic info about Python byte objects
 * @p: PyObject byte object
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *string;

	printf("[*] Python bytes info\n");
	if (!PyBytes_Check(p))
	{
		fprintf(stderr, "  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	string = PyBytes_AsString(p);
	printf("[*] Size of the Python Bytes = %zd\n", size);
	printf("[*] First %zd bytes: ", size < 10 ? size : 10);

	for (i = 0; i < size && i < 10; i++)
		printf("%02x ", (unsigned char)string[i]);

	printf("\n");
}

/**
 * print_python_float - Prints basic info about Python float objects
 * @p: PyObject float object
 */
void print_python_float(PyObject *p)
{
	double value;

	printf("[*] Python float info\n");
	if (!PyFloat_Check(p))
	{
		fprintf(stderr, "  [ERROR] Invalid Float Object\n");
		return;
	}

	value = PyFloat_AsDouble(p);
	printf("[*] Value: %f\n", value);
}
