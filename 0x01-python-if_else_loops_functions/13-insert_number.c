#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: pointer to head of list.
 * @number: number to be inserted.
 * Return: the address of the new node, or NULL if it failed.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;

	if (head ==  NULL)
		return (NULL);
	if (*head == NULL)
	{
		new = add_nodeint_end(head, number);
		return (new);
	}
	for (current = *head; current; current = current->next)
	{
		if (current->next == NULL)
		{
			new = add_nodeint_end(head, number);
			return (new);
		}
		if ((current->next)->n >= number)
		{
			new = malloc(sizeof(listint_t));
			if (new == NULL)
				return (NULL);
			new->n = number;
			new->next = current->next;
			current->next = new;
			return (new);
		}
	}
	return (NULL);
}
