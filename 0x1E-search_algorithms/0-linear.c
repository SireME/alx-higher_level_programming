#include "search_algos.h"

/**
 * linear_search - lniear search alogrithm
 * @array: array to search thorugh
 * @size: size of array
 * @value: value to search for in array
 * Return: index of value or -1 on failure
 **/

int linear_search(int *array, size_t size, int value)
{
	size_t i;

	if (array == NULL)
		return (-1);

	for (i = 0; i < size; i++)
	{
		if (array[i]  == value)
		{
			printf("Value checked array[%ld] = [%d]\n", i, array[i]);
			return (i);
		}
		printf("Value checked array[%ld] = [%d]\n", i, array[i]);
	}

	return (-1);
}
