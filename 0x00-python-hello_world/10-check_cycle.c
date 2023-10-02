#include "lists.h"
/**
 * check_cycle - verifie if we have cycle
 * @list: head of the list
 * Return: zero or one
*/
int check_cycle(listint_t *list)
{
if (list == NULL || list->next == NULL)
{
return (0);
}
listint_t *slow = list;
listint_t *fast = list->next;
while (fast != NULL && fast->next != NULL)
{
if (slow == fast)
{
return (1);
}
slow = slow->next;
fast = fast->next->next;
}
return (0);
}
