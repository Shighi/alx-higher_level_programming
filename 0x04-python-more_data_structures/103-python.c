#include <Python.h>

/**
 * print_python_bytes - Prints info about Python bytes objects
 * @p: Python object
 *
 * This function prints size, string representation, and first bytes of a
 * Python bytes object. It handles error cases for invalid objects.
 */
void print_python_bytes(PyObject *p)
{
	long int size;
	int i;
	char *trying_str = NULL;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	PyBytes_AsStringAndSize(p, &trying_str, &size);

	printf("  size: %li\n", size);
	printf("  trying string: %s\n", trying_str);

	if (size > 10)
		size = 10;
	else
		size++;

	printf("  first %li bytes: ", size);
	for (i = 0; i < size; i++)
	{
		printf("%02hhx", trying_str[i]);
		if (i == (size - 1))
			printf("\n");
		else
			printf(" ");
	}
}

/**
 * print_python_list - Prints info about Python lists
 * @p: Python object
 *
 * This function prints size, allocated space, and element types of a
 * Python list. It also calls print_python_bytes for bytes objects.
 */
void print_python_list(PyObject *p)
{
	long int size = PyList_Size(p);
	int i;
	PyListObject *list = (PyListObject *)p;
	const char *type;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		type = (list->ob_item[i])->ob_type->tp_name;
		printf("Element %i: %s\n", i, type);
		if (!strcmp(type, "bytes"))
			print_python_bytes(list->ob_item[i]);
	}
}
