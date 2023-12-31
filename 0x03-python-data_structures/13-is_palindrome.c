#include "lists.h"

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: head list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);

	return (aux_palind(head, *head));
}

/**
 * aux_palind - function to check if a linked list is a palindrome recursively
 * @head: head list
 * @end: end list
 * Return: 1 if it is a palindrome, 0 otherwise
 */
int aux_palind(listint_t **head, listint_t *end)
{
	if (end == NULL)
		return (1);

	if (aux_palind(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}

	return (0);
}
