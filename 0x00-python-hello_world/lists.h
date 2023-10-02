#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>
#include <string.h>
#include <stdio.h>
/**
 * struct ListNode - singly linked list
 * @val: string
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 */
typedef struct ListNode
{
int val;
struct ListNode *next;
} listint_t;

int check_cycle(listint_t *list);
#endif
