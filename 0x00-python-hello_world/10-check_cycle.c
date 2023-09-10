#include "lists.h"
/**
 * check_cycle - a function that checks
 * if a singly linked list has a cycle in it.
 * @list: is a linked list
 * Return: returns 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *head;

	if (!list)
		return (0);

	head = list;
	while (list->next)
	{
		if (head == list->next)
			return (1);
		list = list->next;
	}
	return (0);
}
