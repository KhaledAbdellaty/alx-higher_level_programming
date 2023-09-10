#include "lists.h"
/**
 * check_cycle - a function that checks
 * if a singly linked list has a cycle in it.
 * @list: is a linked list
 * Return: returns 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *head, fast_p;

	if (!list)
		return (0);

	head = list;
	fast_p = list->next;
	while (head && fast_p && fast_p->next)
	{
		if (head == fast_p)
			return (1);
		head = head->next;
		fast_p = fast_p->next->next;
	}
	return (0);
}
