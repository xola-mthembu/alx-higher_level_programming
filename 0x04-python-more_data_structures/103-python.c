#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <listobject.h>
#include <bytesobject.h>
#include <stdio.h>

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

int main(void)
{
	return (0);
}
