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
    vector<int> nodesBetweenCriticalPoints(ListNode* head) {
        int prev = -1;
        int first = -1;
        int curr = 0;
        ListNode* currNode = head;
        ListNode* prevNode = nullptr;
        int maxDist = 0;
        int minDist = INT_MAX;
        while (currNode != nullptr) {
            if (prevNode != nullptr && currNode->next != nullptr) {
                if ((prevNode->val < currNode->val && currNode->next->val < currNode->val) 
                || 
                (prevNode->val > currNode->val && currNode->next->val > currNode->val)) {
                    if (prev != -1) {
                        maxDist = curr - first;
                        minDist = min(minDist, curr - prev);
                    }
                    if (first == -1) {
                        first = curr;
                    }
                    prev = curr;
                }
            }

            curr++;
            prevNode = currNode;
            currNode = currNode->next;
        }
        if (minDist == INT_MAX) {
            return {-1, -1};
        }
        return {minDist, maxDist};
    }
};
