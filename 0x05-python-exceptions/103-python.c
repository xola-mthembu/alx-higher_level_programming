#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>

/**
 * print_python_bytes - Prints basic info about Python byte objects
 * @p: PyObject byte object
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
	printf("  first %zd bytes:", size < 10 ? size + 1 : 10);

	for (i = 0; i < size && i < 10; i++) {
		printf(" %02x", (unsigned char)string[i]);
	}
	if (size < 10) {
		printf(" %02x", 0);
	}
	printf("\n");
}

/**
 * print_python_float - Prints basic info about Python float objects
 * @p: PyObject float object
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
	printf("  value: %f\n", value);
}

/**
 * print_python_list - Prints basic info about Python lists
 * @p: PyObject list object
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
