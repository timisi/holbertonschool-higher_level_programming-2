#include "lists.h"
/**
 * get_nodeint_at_index - get the given node index in a listin_t list.
 * @head: pointer to first node.
 * @index: node index looked.
 * Return:  returns the nth node of a listint_t linked list.
 */
listint_t *get_nodeint_at_index(listint_t *head, unsigned int index)
{
	unsigned int i;
	listint_t *cursor = NULL;

	if (head == NULL)
		return (NULL);
	cursor = head;
	for (i = 0; cursor != NULL; i++)
	{
		if (index == 0)
			return (cursor);
		cursor = cursor->next;
		if (i == (index - 1) && index != 0)
		{
			return (cursor);
		}
	}
	return (NULL);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	int last_nod, i;
	listint_t *cursor;
	listint_t *last_cursor;

	if (*head == NULL)
		return (1);
	for (last_nod = 0, cursor = *head; cursor != NULL; cursor = cursor->next)
	{
		last_nod++;
	}
	last_nod--;
	for (i = 0; last_nod > 0;)
	{
		last_cursor = get_nodeint_at_index(*head, last_nod);
		cursor = get_nodeint_at_index(*head, i);
		if (i >= last_nod)
			return (1);
		if (last_cursor->n == cursor->n)
		{
			i++;
			last_nod--;
		}
		else
			return (0);
	}
	return (0);
}
