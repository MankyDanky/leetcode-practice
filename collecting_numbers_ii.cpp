#include "bits/stdc++.h"
 
using namespace std;
 
int main()
{
    unordered_map<int, int> indices;
    int n, m;
 
    cin >> n;
    cin >> m;
    vector<int> nums(n);
 
    for (int i = 0; i < n; ++i)
    {
        cin >> nums[i];
        nums[i] -= 1;
        indices[nums[i]] = i;
    }
 
    int sortedSequences = 1;
 
    int prev = -1;
 
    for (int i = 0; i < n; ++i)
    {
        if (indices[i] < prev)
        {
            sortedSequences += 1;
        }
        prev = indices[i];
    }
 
    for (int i = 0; i < m; ++i)
    {
        int a, b;
        cin >> a;
        cin >> b;
        a -= 1;
        b -= 1;
 
        int num1 = nums[a];
        int num2 = nums[b];
 
        if (num1 > 0 && indices[num1 - 1] < indices[num1])
        {
            sortedSequences += 1;
        }
        if (num1 < n - 1 && indices[num1 + 1] > indices[num1])
        {
            sortedSequences += 1;
        }
        if (num2 > 0 && indices[num2 - 1] < indices[num2] && num2 - 1 != num1)
        {
            sortedSequences += 1;
        }
        if (num2 < n - 1 && indices[num2 + 1] > indices[num2] && num2 + 1 != num1)
        {
            sortedSequences += 1;
        }
 
        swap(indices[num1], indices[num2]);
        swap(nums[a], nums[b]);
 
        if (num1 > 0 && indices[num1 - 1] < indices[num1])
        {
            sortedSequences -= 1;
        }
        if (num1 < n - 1 && indices[num1 + 1] > indices[num1])
        {
            sortedSequences -= 1;
        }
        if (num2 > 0 && indices[num2 - 1] < indices[num2] && num2 - 1 != num1)
        {
            sortedSequences -= 1;
        }
        if (num2 < n - 1 && indices[num2 + 1] > indices[num2] && num2 + 1 != num1)
        {
            sortedSequences -= 1;
        }
        cout << sortedSequences << endl;
    }
 
    return 0;
}