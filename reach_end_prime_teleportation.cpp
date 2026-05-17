class Solution {
    public:
        int minJumps(vector<int>& nums) {
            int m = 0;
            for (int num : nums) {
                m = max(m, num);
            }
            vector<int> sieve(m+1, 0);
            unordered_map<int, vector<int>> primeConnections;
    
            int n = nums.size();
            for (int i = 2; i <= m; i++) {
                if (sieve[i] == 0) {
                    primeConnections[i] = vector<int>();
                    for (int j = i; j <= m; j+= i) {
                        sieve[j] = i;
                    }
                }
            }
    
            for (int i = 0; i < n; i++) {
                int num = nums[i];
    
                while (num > 1) {
                    int p = sieve[num];
                    primeConnections[p].push_back(i);
                    while (num % p == 0) {
                        num /= p;
                    }   
                }
            }
    
            deque<int> q = {0};
            int jumps = 0;
            unordered_set<int> visited;
            visited.insert(0);
    
            while (!q.empty()) {
                int s = q.size();
                for (int i = 0; i < s; i++) {
                    int index = q.front();
                    q.pop_front();
    
                    if (index == n-1) {
                        return jumps;
                    }
    
                    if (index - 1 >= 0 && visited.find(index-1) == visited.end()) {
                        q.push_back(index-1);
                        visited.insert(index-1);
                    }
    
                    if (index + 1 < n && visited.find(index+1) == visited.end()) {
                        q.push_back(index+1);
                        visited.insert(index+1);
                    }
    
                    if (primeConnections.find(nums[index]) != primeConnections.end()) {
                        for (int tp : primeConnections[nums[index]]) {
                            if (visited.find(tp) == visited.end()) {
                                q.push_back(tp);
                                visited.insert(tp);
                            }
                        }
                        primeConnections[nums[index]].clear();
                    } 
                }
    
                jumps += 1;
            }
            return n-1;
        }
    };