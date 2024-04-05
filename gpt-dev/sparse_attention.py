import torch
import torch.nn as nn
import torch.nn.functional as F

class SparseAttention(nn.Module):
    def __init__(self, d_model, nhead, window_size):
        super(SparseAttention, self).__init__()
        self.d_model = d_model
        self.nhead = nhead
        self.window_size = window_size

        self.qkv_linear = nn.Linear(d_model, 3 * d_model)
        self.out_linear = nn.Linear(d_model, d_model)

    def forward(self, x):
        batch_size, seq_len, _ = x.size()
        head_dim = self.d_model // self.nhead
        
        # Compute query, key, and value
        qkv = self.qkv_linear(x).view(batch_size, seq_len, 3, self.nhead, head_dim)
        q, k, v = qkv.unbind(2)
        
        # Initialize output tensor
        out = torch.zeros_like(x)
        
        # Perform sparse attention for each position
        for i in range(seq_len):
            # Determine the start and end of the attention window
            start = max(0, i - self.window_size)
            end = min(seq_len, i + self.window_size + 1)

            # Extract the relevant query, key, and value vectors
            q_i = q[:, i, :, :].unsqueeze(1)
            k_i = k[:, start:end, :, :]
            v_i = v[:, start:end, :, :]
            
            # Compute attention scores and weights
            attn_scores = (q_i @ k_i.transpose(-2, -1)) / (head_dim ** 0.5)
            attn_weights = F.softmax(attn_scores, dim=-1)
            
            # Compute weighted sum of values
            out_i = (attn_weights @ v_i).transpose(1, 2).reshape(batch_size, 1, self.d_model)
            out[:, i:i+1, :] = out_i

        # Apply output linear layer
        out = self.out_linear(out)
        return out

# Test the SparseAttention module
sparse_attention = SparseAttention(d_model=128, nhead=8, window_size=5)
x = torch.rand(2, 100, 128)  # Batch of 2 sequences, each with 100 tokens of dimension 128
y = sparse_attention(x)
print(y.size())  # Should be (2, 100, 128)
