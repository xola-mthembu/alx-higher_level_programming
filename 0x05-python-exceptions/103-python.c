#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>

/**
 * print_python_bytes - Prints basic info about Python byte objects
 * @p: PyObject byte object
 *
 * Description: Prints the size of the bytes object, attempts to print
 * the string representation if it's a valid string, and prints the first
 * 10 bytes of the bytes object.
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *string;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p)) {
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	string = PyBytes_AsString(p);
	printf("  size: %zd\n", size);
	printf("  trying string: %s\n", string);
	printf("  first %zd bytes:", size < 10 ? size : 10);

	for (i = 0; i < size && i < 10; i++) {
		printf(" %02x", (unsigned char)string[i]);
	}
	printf("\n");
}

/**
 * print_python_float - Prints basic info about Python float objects
 * @p: PyObject float object
 *
 * Description: Prints the value of the float object with a precision of 1
 * decimal place.
 */
void print_python_float(PyObject *p)
{
	double value;

	printf("[.] float object info\n");
	if (!PyFloat_Check(p)) {
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	value = PyFloat_AsDouble(p);
	printf("  value: %.1f\n", value);
}

/**
 * print_python_list - Prints basic info about Python lists
 * @p: PyObject list object
 *
 * Description: Prints the size and allocated size of the list, and
 * iterates through each element to print its type. Calls
 * print_python_bytes and print_python_float for bytes and float objects.
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, allocated, i;
	PyObject *item;

	printf("[*] Python list info\n");
	if (!PyList_Check(p)) {
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	size = PyList_Size(p);
	allocated = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", allocated);

	for (i = 0; i < size; i++) {
		item = PyList_GetItem(p, i);
		printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
		if (PyBytes_Check(item))
			print_python_bytes(item);
		else if (PyFloat_Check(item))
			print_python_float(item);
	}
}
