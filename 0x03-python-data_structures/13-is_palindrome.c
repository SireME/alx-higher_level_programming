#include "lists.h"
#include <stdlib.h>
#include <unistd.h>
/**
 * is_palindrome - check if linked list is a pallindrome or not
 * @head: linked list
 *
 * Return: 1 if linked lis 0 if not
 */

int is_palindrome(listint_t **head)
{
	int l_len = 0, *tempa, i = 0;
	int n_len, status = 1;
	listint_t *current, *n_current;

	if (*head == NULL) /*empty list considered pallindrom*/
		return (status);
	/* calculating length for array size*/
	current = *head;
	while (current != NULL)
	{
		l_len++;
		current = current->next;
	}
	/* allocating memory for array*/
	tempa = malloc(sizeof(int) * l_len);
	if (tempa == NULL)
	{
		write(1, "malloc", 6);
		return (-1);
	}
	n_current = *head;
	while (n_current != NULL)
	{
		tempa[i++] = n_current->n;
		n_current = n_current->next;
	}
	n_len = l_len - 1; /*determine if pallindrome or not*/
	for (i = 0; i <= l_len / 2; i++)
	{
		if (tempa[i] != tempa[n_len])
		{
			status = 0;
			break;
		}
		n_len--;
	}
	free(tempa);
	return (status);
}
