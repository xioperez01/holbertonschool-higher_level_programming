#include "lists.h"

/**
 * check_cycle - function  that checks if a singly linked list has a cycle in it
 * @list: Pointer to the list.
 * Return: 0 if there is no cycle, 1 if there is a cycle.

 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	if (list == NULL)
		return (0);

	slow = slow->next;
	fast = slow->next;

	while (slow && fast && fast->next)
	{
		if (slow == fast)
			return (1);

		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}
