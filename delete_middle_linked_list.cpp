/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* deleteMiddle(ListNode* head) {
        int n = 0;
        ListNode* curr = head;
        while (curr != nullptr) {
            n += 1;
            curr = curr->next;
        }

        if (n == 1) return nullptr;

        ListNode* prev = nullptr;
        curr = head;
        int i = 0;
        while (i < n/2) {
            i += 1;
            prev = curr;
            curr = curr->next;
        }

        prev->next = curr->next;
        return head;
        
    }
};
