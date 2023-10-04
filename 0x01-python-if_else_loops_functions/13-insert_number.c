#include "lists.h"
/**
 * insert_node - Inserts a number into a sorted singly linked list.
 * @head: A pointer to the head of the linked list.
 * @number: The number to insert.
 *
 * Return: The address of the new node, or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number) {
    listint_t *new_node = malloc(sizeof(listint_t));
    listint_t *current = *head;
    listint_t *prev = NULL;

    if (new_node == NULL)
        return (NULL);

    new_node->n = number;
    new_node->next = NULL;

    if (*head == NULL || number <= (*head)->n) {
        /* Insert at the beginning of the list */
        new_node->next = *head;
        *head = new_node;
        return (new_node);
    }

    while (current != NULL && number > current->n) {
        prev = current;
        current = current->next;
    }

    /* Insert the new node between prev and current */
    prev->next = new_node;
    new_node->next = current;

    return (new_node);
}
