#include <Python.h>
#include <object.h>
#include <unicodeobject.h>

/**
 * print_python_string - Prints information about a Python string object
 * @p: A pointer to a Python object
 * Description: This function checks if the passed object is a valid Python
 * Unicode string. If valid, it prints the type, length, and value of the
 * string. If not valid, it prints an error message.
 */
void print_python_string(PyObject *p)
{
	const char *type;
	Py_ssize_t length;
	const char *value;

	printf("[.] string object info\n");

	if (!PyUnicode_Check(p))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	if (PyUnicode_IS_COMPACT_ASCII(p))
		type = "compact ascii";
	else if (PyUnicode_IS_COMPACT(p))
		type = "compact unicode object";
	else
		type = "unicode object";

	length = PyUnicode_GET_LENGTH(p);
	value = PyUnicode_AsUTF8(p);

	printf("  type: %s\n", type);
	printf("  length: %zd\n", length);
	printf("  value: %s\n", value);
}
