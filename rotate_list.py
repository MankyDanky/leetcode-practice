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
    ListNode* rotateRight(ListNode* head, int k) {
        if (head == nullptr) return nullptr;
        int n = 0;
        ListNode* tail = nullptr;
        ListNode* node = head;
        while (node != nullptr) {
            n += 1;
            tail = node;
            node = node->next;
        }

        cout<<n<<endl;

        k %= n;
        k = n-k;
        k %= n;
        
        if (k == 0) return head;

        cout<<k<<endl;

        ListNode* prev = nullptr;
        node = head;

        for (int i = 0; i < k; i++) {
            prev = node;
            node= node->next;
        }

        cout<<head->val<<endl;
        cout<<node->val;

        tail->next = head;
        prev->next = nullptr;

        return node;


    }
};