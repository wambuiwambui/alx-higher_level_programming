#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: linked list in question
 * Return: 0 if there is no cycle, 1 if there is a cycle
*/
int check_cycle(listint_t *list)
{
	listint_t *z1 = NULL, *z2 = NULL;

	z1 = z2 = list;
	while (list && z1 && z2 && z1->next && z2->next)
	{
		z1 = z1->next;
		z2 = z2->next->next;
		if (!z2 || !z1)
			return (0);
		if (z2->next == z1)
			return (1); 
	}
	return (0);
}
