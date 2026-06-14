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
    int pairSum(ListNode* head) {
        ListNode* prev = nullptr;

        ListNode* curr = head;

        int n = 0;
        while (curr != nullptr) {
            n += 1;
            curr = curr->next;
        }

        int i = 0;
        curr = head;
        prev = nullptr;
        while (i < n / 2) {
            i += 1;
            prev = curr;
            curr = curr->next;
        }

        prev->next = nullptr;

        prev = nullptr;
        while (curr != nullptr) {
            ListNode* temp = curr;
            curr = curr->next;
            temp->next = prev;
            prev = temp;
        }

        curr = prev;

        int res = 0;
        while (head != nullptr && curr != nullptr) {
            res = max(res, head->val + curr->val);
            curr = curr->next;
            head = head->next;
        }

        return res;
    }
};
