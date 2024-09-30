#include <Python.h>
#include <floatobject.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Prints info about Python lists
 * @p: PyObject pointer to a Python list
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, alloc, i;
	PyObject *item;

	if (!PyList_Check(p))
	{
		fprintf(stderr, "[*] Python list info\n");
		fprintf(stderr, "  [ERROR] Invalid List Object\n");
		return;
	}

	size = PyList_GET_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", alloc);

	for (i = 0; i < size; i++)
	{
		item = PyList_GET_ITEM(p, i);
		printf("Element %ld: %s\n", i, item->ob_type->tp_name);
		if (PyBytes_Check(item))
			print_python_bytes(item);
		else if (PyFloat_Check(item))
			print_python_float(item);
	}
}

/**
 * print_python_bytes - Prints info about Python bytes objects
 * @p: PyObject pointer to a Python bytes object
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *str;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_GET_SIZE(p);
	str = PyBytes_AsString(p);

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);

	printf("  first %ld bytes: ", (size < 10) ? size + 1 : 10);
	for (i = 0; i < size && i < 10; i++)
		printf("%02hhx ", str[i]);
	printf("\n");
}

/**
 * print_python_float - Prints info about Python float objects
 * @p: PyObject pointer to a Python float object
 */
void print_python_float(PyObject *p)
{
	double value;
	char *str;

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
