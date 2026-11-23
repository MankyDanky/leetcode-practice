class SegmentTree {
    vector<int> tree;
    int n;
    public:
    SegmentTree() {
        n = 4*1e4;
        tree.resize(n*2, 1);
    }

    void Set(int index, int value) {
        index += n;
        tree[index] = value;
        index >>= 1;
        while (index >= 1) {
            tree[index] = tree[index*2] * tree[index * 2 + 1];
            index >>= 1;
        }
    }

    long long Query(int l, int r) {
        long long product = 1;
        l += n;
        r += n;
        while (l < r) {
            if (l % 2) {
                product *= tree[l];
                l += 1;
            }
            if (!(r % 2)) {
                product *= tree[r];
                r -= 1;
            }
            if (r < l) break;
            r>>=1;
            l>>=1;
        }
        if (l == r) {
            product *= tree[l];
        }
        
        return product;
    }
};

class ProductOfNumbers {
public:
    int prod = 1;
    int zeros = 0;
    SegmentTree t;
    int index = 0;

    ProductOfNumbers() {
        
    }
    
    void add(int num) {
        t.Set(index, num);
        index += 1;
    }
    
    int getProduct(int k) {
        long long r = t.Query(index - k, index - 1);
        return r;
    }
};

/**
 * Your ProductOfNumbers object will be instantiated and called as such:
 * ProductOfNumbers* obj = new ProductOfNumbers();
 * obj->add(num);
 * int param_2 = obj->getProduct(k);
 */
