#include "lists.h"

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: head of the linked list
 * Return: 1 if it is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
    if (head == NULL || *head == NULL)
        return (1);

    return (aux_palind(head, *head));
}

/**
 * aux_palind - auxiliary function to check palindrome recursively
 * @left: left pointer
 * @right: right pointer
 * Return: 1 if it is a palindrome, 0 otherwise
 */
int aux_palind(listint_t **left, listint_t *right)
{
    if (right == NULL)
        return (1);

    if (aux_palind(left, right->next) && (*left)->n == right->n)
    {
        *left = (*left)->next;
        return (1);
    }

    return (0);
}
