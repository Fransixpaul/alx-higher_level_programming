#include "lists.h"
/**
 * check_cycle - Function that check if a list is has a circle
 * @list: Liked list
 * Return: 1 if there is a circle or 0 if not a circle
 */
int check_cycle(listint_t *list)
{
	listint_t *rapid, *slow;

	if (!list || !list->next)
		return (0);
	rapid = list;
	slow = list;

	while (slow != NULL && rapid != NULL && rapid->next != NULL)
	{
		slow = slow->next;
		rapid = rapid->next->next;

		if (slow == rapid)
		{
			return (1);
		}
	}
	return (0);
}
