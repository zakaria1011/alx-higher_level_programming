#include "lists.h"
/**
 * check_cycle - verifie if we have cycle
 * @list: head of the list
 * Return: zero or one
*/
nt check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
		return (0);

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}

	return (0);
}
