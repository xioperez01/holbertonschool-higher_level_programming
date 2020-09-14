#include "lists.h"

/**
 * is_palindrome - function that checks if a singly linked list is a palindrome.
 * @head: Pointer to the head of list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 **/

int is_palindrome(listint_t **head)
{
	listint_t *aux = *head;
	int i = 0, j = 0, array[3000];

	if (head == NULL || *head == NULL)
		return (1);

	while (aux != NULL)
	{
		array[i] = aux->n;
		aux = aux->next;
		i++;
	}
	for (; i > 0; i--)
	{
		if (array[j] != array[i - 1])
		{
			return (0);
		}
		j++;
	}
	return (1);
}
