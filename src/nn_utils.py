import random

def transpose(a):
    r = len(a)
    c = len(a[0]) if r else 0
    return [[a[i][j] for i in range(r)] for j in range(c)]

def matmul(a,b):
    """
    args:
        a,b: list[list[float]]
    usage:
        (m,n) * (n,p) -> (m,p)
    """
    m = len(a)
    n = len(a[0]) if m > 0 else 0
    n2 = len(b)
    p = len(b[0]) if n2 > 0 else 0
    
    if n!=n2:
        raise ValueError(f"matmul shape mismatch:{(m,n)}*{(n2,p)}")
    out = []
    # --- row ---
    for i in range(m):
        row = []
        # --- column ---
        for j in range(p):
            s = 0.0
            # --- dot ---
            for k in range(n):
                s += a[i][k] * b[k][j]
            row.append(s)
        out.append(row)
    return out

def add_bias(x,bias):
    """
    args:
        x:(batch,out_dim)
        bias:(out_dim,)
    """
    batch = len(x)
    out_dim = len(x[0]) if batch > 0 else 0
    if len(bias) != out_dim:
        raise ValueError("bias length mismatch")
    y = []
    for i in range(batch):
        row = []
        for j in range(out_dim):
            row.append(x[i][j]+bias[j])
        y.append(row)
    return y

def relu(x):
    y = []
    for row in x:
        y.append([v if v > 0.0 else 0.0 for v in row])
    return y