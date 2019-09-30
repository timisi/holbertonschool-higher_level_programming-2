#include <Python.h>
#include <stdio.h>
/**
 * print_python_float - prints some basic info about Python floats.
 * @p: python object.
 */
void print_python_float(PyObject *p)
{
	double num;
	char *num_str;

	num = ((PyFloatObject *)(p))->ob_fval;

	printf("[.] float object info\n");
	if (!PyFloat_Check(p))
		printf("  [ERROR] Invalid Float Object\n");
	else
	{
		num_str = PyOS_double_to_string(num, 'r', 0, Py_DTSF_ADD_DOT_0, Py_DTST_FINITE);
		printf("  value: %s\n", num_str);
	}
	fflush(stdout);
}
/**
 * print_python_bytes - prints some basic info about Python bytes.
 * @p: python object.
 */
void print_python_bytes(PyObject *p)
{
	long int size;
	int i;
	char *str;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
		printf("  [ERROR] Invalid Bytes Object\n");
	else
	{
		size = ((PyVarObject *)(p))->ob_size;
		str = ((PyBytesObject *)(p))->ob_sval;

		printf("  size: %ld\n", size);
		printf("  trying string: %s\n", str);
		size++;
		if (size >= 10)
			size = 10;
		printf("  first %ld bytes:", size);
		for (i = 0; i < size; i++)
		{
			if (str[i] < 0)
				printf(" %02x", 256 + str[i]);
			else
				printf(" %02x", str[i]);
		}
		printf("\n");
	}
	fflush(stdout);
}

/**
 * print_python_list - prints some basic info about Python lists.
 * @p: python object.
 */
void print_python_list(PyObject *p)
{
	int size;
	int alloc;
	int i;
	const char *type_name;
	PyObject *item;

	size = (((PyVarObject *)(p))->ob_size);
	alloc = ((PyListObject *)(p))->allocated;
	printf("[*] Python list info\n");
	if (!PyList_Check(p))
		printf("  [ERROR] Invalid List Object\n");
	else
	{
		printf("[*] Size of the Python List = %d\n", size);
		printf("[*] Allocated = %d\n", alloc);

		for (i = 0; i < size; i++)
		{
			item = ((PyListObject *)p)->ob_item[i];
			type_name = (item->ob_type)->tp_name;
			printf("Element %d: ", i);
			printf("%s\n", type_name);
			if (PyBytes_Check(item))
				print_python_bytes(item);
			if (PyFloat_Check(item))
				print_python_float(item);
		}
	}
	fflush(stdout);
}
