struct Node {
    int val;
    vector<Node*> connections;
};

class Skiplist {
public:
    int size = 0;
    int tracks = 1;
    int capacity = 1;
    Node* root;


    Skiplist() {
       root = new Node();
       root->connections.push_back(nullptr);
       root->val = -1;
    }
    
    bool search(int target) {
        vector<Node*> conns = vector<Node*>(tracks, root);
        int j = tracks-1;
        while (j >= 0) {
            if (conns[j]->connections[j] == nullptr || conns[j]->connections[j]->val >= target) {
                j -= 1;
                continue;
            }

            for (int k = j - 1; k >= 0; k--) {
                conns[k] = conns[j]->connections[k];
            }
            conns[j] = conns[j]->connections[j];
        }
        print_list();
        if (conns[0]->connections[0] == nullptr) return false;
        return conns[0]->connections[0]->val == target;
    }
    
    void add(int num) {
        if (size == capacity) {
            tracks++;
            capacity *= 2;
            root->connections.push_back(nullptr);
        }
        size += 1;
        vector<Node*> conns = vector<Node*>(tracks, root);
        int j = tracks - 1;
        while (j >= 0) {
            if (conns[j]->connections[j] == nullptr || conns[j]->connections[j]->val >= num) {
                j -= 1;
                continue;
            }
            for (int k = j - 1; k >= 0; k--) {
                conns[k] = conns[j]->connections[k];
            }
            conns[j] = conns[j]->connections[j];
        }
        Node* add = new Node();
        add->val = num;
        add->connections.push_back(conns[0]->connections[0]);
        conns[0]->connections[0] = add;
        int t = 1;
        while (rand()%2 == 1) {
            if (t == tracks) break;
            add->connections.push_back(conns[t]->connections[t]);
            conns[t]->connections[t] = add;
            t++;
            
        }
        print_list();
    }

    void print_list() {
        return;
        Node* node = root;
        while (node != nullptr) {
            cout<<node->val<<' ';
            node = node->connections[0];
        }
        cout<<endl;
    }
    
    bool erase(int num) {
        print_list();
        vector<Node*> conns = vector<Node*>(tracks, root);
        int j = tracks-1;
        while (j >= 0) {
            if (conns[j]->connections[j] == nullptr || conns[j]->connections[j]->val >= num) {
                j -= 1;
                continue;
            }
            for (int k = j - 1; k >= 0; k--) {
                conns[k] = conns[j]->connections[k];
            }
            conns[j] = conns[j]->connections[j];
        }
        if (conns[0]->connections[0] == nullptr) return false;
        if (conns[0]->connections[0]->val != num) return false;
        Node* node = conns[0]->connections[0];
        for (int i = 0; i < node->connections.size(); i++) {
            conns[i]->connections[i] = node->connections[i];
        }
        delete node;
        print_list();
        return true;
    }
};

/**
 * Your Skiplist object will be instantiated and called as such:
 * Skiplist* obj = new Skiplist();
 * bool param_1 = obj->search(target);
 * obj->add(num);
 * bool param_3 = obj->erase(num);
 */
