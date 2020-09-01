#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: linkedlist
 * @number: number to add
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;

	current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;

	if (*head == NULL || (*head)->n > number)
	{
		new->next = new;
		*head = new;
		return (new);
	}
	while (current->next)
	{
		if ((current->next)->n > number)
		{
			new->next = current->next;
			current->next = new;
			return (new);
		}
		current = current->next;
	}

	return (new);
}
