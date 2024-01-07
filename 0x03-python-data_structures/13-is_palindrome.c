#include "lists.h"
#include <stddef.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to the head of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
    listint_t *current = *head;
    int values[2048];
    int i = 0, j;

    if (!head || !*head || !(*head)->next)
        return (1);

    while (current)
    {
        values[i++] = current->n;
        current = current->next;
    }

    for (j = 0, i--; j <= i; j++, i--)
    {
        if (values[j] != values[i])
            return (0);
    }

    return (1);
}
