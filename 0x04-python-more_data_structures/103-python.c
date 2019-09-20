#include <Python.h>
#include <stdio.h>
/**
 * _strcmp - compare the strings
 * @s1: the firts input string.
 * @s2: the second input string.
 * Return: if strings are the same 0, if not the difference between both.
 */
int _strcmp(const char *s1, const char *s2)
{
	int i = 0;

	while ((s1[i] != '\0' && s2[i] != '\0') && (s1[i] == s2[i]))
	{
		i++;
	}
	if (s1[i] == s2[i])
	{
		return (0);
	}
	else
	{
		return (s1[i] - s2[i]);
	}
}
/**
 * print_python_bytes - prints some basic info about Python bytes.
 * @p: python object.
 */
void print_python_bytes(PyObject *p)
{
	int size;
	int i;
	char *str;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
		printf("  [ERROR] Invalid Bytes Object\n");
	else
	{
		size = ((PyVarObject *)(p))->ob_size;
		str = ((PyBytesObject *)(p))->ob_sval;

		printf("  Size: %d\n", size);
		printf("  trying string: %s\n", str);
		size++;
		if (size >= 10)
			size = 10;
		printf("  first %d bytes: ", size);
		for (i = 0; i < size - 1; i++)
		{
			if (str[i] < 0)
				printf("%02x ", 256 + str[i]);
			else
				printf("%02x ", str[i]);
		}
		if (str[i] < 0)
			printf("%02x\n", 256 + str[i]);
		else
			printf("%02x\n", str[i]);
	}
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
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < size; i++)
	{
		item = ((PyListObject *)p)->ob_item[i];
		type_name = (item->ob_type)->tp_name;
		printf("Element %d: ", i);
		printf("%s\n", type_name);
		if (_strcmp(type_name, "bytes") == 0)
		{
			print_python_bytes(item);
		}
	}
}
