#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to the head of the list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
    listint_t *fast = *head, *slow = *head;
    listint_t *prev = NULL, *temp = NULL, *second_half;

    if (head == NULL || *head == NULL || (*head)->next == NULL)
        return (1);

    /* Find the middle and reverse the second half */
    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;
        temp = slow->next;
        slow->next = prev;
        prev = slow;
        slow = temp;
    }

    second_half = (fast == NULL) ? slow : slow->next;
    temp = (fast == NULL) ? prev : slow;

    /* Compare the first half and the reversed second half */
    while (temp != NULL && second_half != NULL)
    {
        if (temp->n != second_half->n)
        {
            /* Not a palindrome, restore the list and return 0 */
            slow->next = prev;
            return (0);
        }
        temp = temp->next;
        second_half = second_half->next;
    }

    /* Restore the list */
    slow->next = prev;

    return (1);
}
