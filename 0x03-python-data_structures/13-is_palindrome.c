#include "lists.h"

/**
 * is_palindrome - a function that checks
 * if a singly linked list is a palindrome.
 * @head: a linked list that will check it.
 * Return: 0 if it is not a palindrome, otherwise 1.
*/
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head;
	listint_t *prev = NULL, *curr = NULL, *next;
	listint_t *first = *head, *second = prev;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (fast->next != NULL && fast->next-> != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	while (curr != NULL)
	{
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}
	first = *head;
	second = prev;
	while (second != NULL)
	{
		if (first->n != second->n)
			return (0);
		first = first->next;
		second = second->next;
	}

	return (1);
}
