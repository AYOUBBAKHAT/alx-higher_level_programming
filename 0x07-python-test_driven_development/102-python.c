#include "Python.h"

/**
 * print_python_string - Prints information about Python strings.
 * @p: A PyObject string object.
 */
void print_python_string(PyObject *p)
{
	long int length;
	const char *type_description = PyUnicode_IS_COMPACT_ASCII(p)
		? "compact ascii" : "compact unicode object";

	fflush(stdout);
	printf("[.] string object info\n");

	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	length = ((PyASCIIObject *)(p))->length;
	printf("  type: %s\n", type_description);
	printf("  length: %ld\n", length);
	printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &length));
}
