#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Prints basic info about Python lists
 * @p: PyObject pointer to a Python list
 */
void print_python_list(PyObject *p)
{
	long int size, i;
	PyListObject *list;
	PyObject *item;

	setbuf(stdout, NULL);
	printf("[*] Python list info\n");

	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	list = (PyListObject *)p;
	size = list->ob_base.ob_size;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		item = list->ob_item[i];
		printf("Element %ld: %s\n", i, item->ob_type->tp_name);
		if (PyBytes_Check(item))
			print_python_bytes(item);
		else if (PyFloat_Check(item))
			print_python_float(item);
	}
}

/**
 * print_python_bytes - Prints basic info about Python byte objects
 * @p: PyObject pointer to a Python byte object
 */
void print_python_bytes(PyObject *p)
{
	long int size, i;
	PyBytesObject *bytes = (PyBytesObject *)p;

	setbuf(stdout, NULL);
	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = bytes->ob_base.ob_size;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", bytes->ob_sval);

	printf("  first %ld bytes: ", size < 10 ? size + 1 : 10);
	for (i = 0; i < size && i < 10; i++)
	{
		printf("%02hhx", bytes->ob_sval[i]);
		if (i < 9 && i + 1 < size)
			printf(" ");
	}
	printf("\n");
}

/**
 * print_python_float - Prints basic info about Python float objects
 * @p: PyObject pointer to a Python float object
 */
void print_python_float(PyObject *p)
{
	double value;
	char *str;

	setbuf(stdout, NULL);
	printf("[.] float object info\n");

	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	value = ((PyFloatObject *)p)->ob_fval;
	str = PyOS_double_to_string(value, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);

	printf("  value: %s\n", str);
	PyMem_Free(str);
}
