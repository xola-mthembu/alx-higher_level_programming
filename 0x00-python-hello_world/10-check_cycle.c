#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list has a cycle in it.
 * @list: Pointer to the head of the list.
 *
 * This function uses Floyd's Tortoise and Hare algorithm to detect
 * a cycle in a linked list. It employs two pointers, a slow pointer
 * (the tortoise) and a fast pointer (the hare). The slow pointer
 * moves one node at a time, while the fast pointer moves two nodes.
 * If there's a cycle, these pointers will eventually meet.
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	while (slow && fast && fast->next)
	{
		slow = slow->next;			/* Move slow pointer by one */
		fast = fast->next->next;	/* Move fast pointer by two */

		if (slow == fast)
		{
			return (1);	/* Cycle detected */
		}
	}
	return (0);	/* No cycle found */
}
