// Complete the has_cycle function below.

/*
 * For your reference:
 *
 * SinglyLinkedListNode {
 *     int data;
 *     SinglyLinkedListNode* next;
 * };
 *
 */
bool has_cycle(SinglyLinkedListNode* head) {
     if (!head->next || !head) {
          return false;
     }

     SinglyLinkedListNode* tortoise = head;
     SinglyLinkedListNode* hare = head;

     while (hare && hare->next) {
          tortoise = tortoise->next;
          hare = hare->next->next;
          if (tortoise == hare) {
               return true;
          }
     }

     return false;
}

