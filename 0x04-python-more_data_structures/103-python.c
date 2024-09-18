#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>

void print_python_bytes(PyObject *p);
void print_python_list(PyObject *p);

/**
 * print_python_bytes - Prints basic info about Python byte objects
 * @p: PyObject byte object
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

	printf("  first %zd bytes: ", size < 10 ? size : 10);
	for (i = 0; i < size && i < 10; i++)
	{
		printf("%02x", (unsigned char)string[i]);
		if (i + 1 < 10 && i + 1 < size)
			printf(" ");
	}
	printf("\n");
}

/**
 * print_python_list - Prints basic info about Python lists
 * @p: PyObject list object
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, alloc, i;
	PyObject *item;
	const char *type;

	size = PyList_Size(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", alloc);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		type = Py_TYPE(item)->tp_name;
		printf("Element %zd: %s\n", i, type);
		if (PyBytes_Check(item))
			print_python_bytes(item);
	}
}
