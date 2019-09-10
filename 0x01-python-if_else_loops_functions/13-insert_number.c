#include "lists.h"
#include <stdlib.h>

/**
 * add_nodeint - adds a new node at the beginning of a listint_t list.
 * @head: pointer to first node.
 * @n: given int to be added.
 * Return: the address of the new element, or NULL if it failed.
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *temp;

	temp = malloc(sizeof(listint_t));
	if (temp == NULL)
		return (NULL);
	temp->n = n;
	temp->next = *head;
	*head = temp;
	return (temp);
}

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
	current = *head;
	if (current->n > number)
	{
		new = add_nodeint(head, number);
		return (new);
	}
	for (; current; current = current->next)
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
