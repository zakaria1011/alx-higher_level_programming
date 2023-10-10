#include "lists.h"
int num_of_nods(listint_t *head)
{
int count = 0;
listint_t *current = head;
while (current != NULL)
{
    current = current->next;
    count++;
}
return (count);
}
int is_palindrome(listint_t **head)
{
    listint_t *current;
    int count = 0;
    int mid, half1 = 0 ,half2 = 0;
    int i;
    current = *head;
    
    count = num_of_nods(current);
    if (count % 2 == 0)
    {
        mid = count / 2;
        for (i = 1; i <= mid ; i++)
        {
            half1 += current->n;
            current = current->next;
        }
        for (i = (mid + 1); i <= (2*mid) ; i++)
        {
            half2 = half2 + ((-1)*current->n);
            current = current->next;
        }
        if (half1 + half2 == 0)
        {
            return (1);
        }
        else
        {
            return (0);
        }
    }
    else
    {
        mid  = count / 2;
        for (i = 1; i <= mid ; i++)
        {
            half1 += current->n;
            current = current->next;
        }
        for (i = (mid + 1) ; i <= (2*mid) ; i++)
        {
            half2 = half2 + ((-1)*current->n);
            current = current->next;
        }
        if (half1 + half2 == 0)
        {
            return (1);
        }
        else
        {
            return (0);
        }
    }
    
}
