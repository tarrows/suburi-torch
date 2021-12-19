import torch

# named tensor
img_t = torch.randn(3, 5, 5)  # shape [channels, rows, columns]

# Named tensors and all their associated APIs are an experimental feature
weights = torch.tensor([0.2126, 0.7152, 0.0722], names=['channels'])
# batch_t = torch.randn(2, 3, 5, 5)

# unsqueeze is not yet supported with named tensors
# Please drop names via `tensor = tensor.rename(None)`,
# call the op with an unnamed tensor,
# and set names on the result of the operation.
# img_gray_weigted = torch.einsum('...chw,c->...hw', img_t, weights)

print(weights.shape)
