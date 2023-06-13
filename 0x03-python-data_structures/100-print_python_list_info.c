#include <Python.h>
#include <listobject.h>
#include <stdio.h>

/**
 * print_python_list_info - print info about python lists
 * @p: pointer to python list
 *
 * Return: nothing
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t list_size, i;
	PyTypeObject *objtype;

	list_size = PyList_Size(p);
	/* print size of python list*/
	printf("[*] Size of the Python List = %ld\n", list_size);

	/* print allocated memory for the list */
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	/* print number of items in list */
	for (i = 0; i < list_size; i++)
	{
		objtype = Py_TYPE(PyList_GetItem(p, i));
		printf("Element %ld: %s\n", i, objtype->tp_name);
	}
}

