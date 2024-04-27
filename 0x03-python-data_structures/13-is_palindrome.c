#include "lists.h"
#include <stddef.h>
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to the head of the list
 * Return: 1 if palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow = *head, *fast = *head, *prev_slow = *head;
    listint_t *second_half = NULL;
    int is_palindrome = 1;

    if (*head != NULL && (*head)->next != NULL)
    {
        while (fast != NULL && fast->next != NULL)
        {
            fast = fast->next->next;
            prev_slow = slow;
            slow = slow->next;
        }

        if (fast != NULL) // odd number of nodes
            slow = slow->next;

        second_half = slow;
        prev_slow->next = NULL;
        reverse_list(&second_half);
        is_palindrome = compare_lists(*head, second_half);
        reverse_list(&second_half);
        prev_slow->next = second_half;
    }

    return is_palindrome;
}

/**
 * reverse_list - reverses a linked list
 * @head_ref: double pointer to the head of the list
 */
void reverse_list(listint_t **head_ref)
{
    listint_t *prev = NULL, *current = *head_ref, *next = NULL;

    while (current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    *head_ref = prev;
}

/**
 * compare_lists - compares two linked lists
 * @head1: pointer to the head of the first list
 * @head2: pointer to the head of the second list
 * Return: 1 if lists are equal, 0 otherwise
 */
int compare_lists(listint_t *head1, listint_t *head2)
{
    listint_t *temp1 = head1;
    listint_t *temp2 = head2;

    while (temp1 && temp2)
    {
        if (temp1->n == temp2->n)
        {
            temp1 = temp1->next;
            temp2 = temp2->next;
        }
        else
            return 0;
    }

    if (temp1 == NULL && temp2 == NULL)
        return 1;

    return 0;
}
