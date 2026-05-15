import sys

def solve():
    input = sys.stdin.read().split()
    if not input: return
    
    t = int(input[0])
    curr = 1
    results = []
    
    for _ in range(t):
        n = int(input[curr])
        k = int(input[curr + 1])
        s = input[curr + 2]
        curr += 3
        
        # 1. Check for impossible condition: block of 1s >= k
        max_ones = 0
        current_ones = 0
        for char in s:
            if char == '1':
                current_ones += 1
                max_ones = max(max_ones, current_ones)
            else:
                current_ones = 0
        
        if max_ones >= k:
            results.append("NO")
            continue
            
        # 2. Construction: Assign ranks greedily
        # A safe way is to fill 0-positions with high values 
        # and 1-positions with low values in a specific order.
        p = [0] * n
        ones_indices = [i for i, char in enumerate(s) if char == '1']
        zeros_indices = [i for i, char in enumerate(s) if char == '0']
        
        # We fill indices such that p[i] is small for s[i]==1
        # and p[i] is large for s[i]==0.
        all_vals = list(range(1, n + 1))
        
        # To handle the 'maximum' constraint, simply placing 
        # larger values at '0' spots often suffices.
        val_ptr = 0
        # Fill 1s with smallest values
        for idx in ones_indices:
            p[idx] = all_vals[val_ptr]
            val_ptr += 1
        # Fill 0s with remaining (largest) values
        for idx in zeros_indices:
            p[idx] = all_vals[val_ptr]
            val_ptr += 1
            
        results.append("YES")
        results.append(" ".join(map(str, p)))
        
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()
