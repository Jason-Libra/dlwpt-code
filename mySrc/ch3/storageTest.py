import torch

a = torch.tensor(list(range(9)))
b = a.view(3, 3)

print(f"{id(a.storage())=}")
print(f"{id(b.storage())=}")
print(f"{a.storage().data_ptr()=}")
print(f"{b.storage().data_ptr()=}")
print(f"{id(a.untyped_storage())=}")
print(f"{id(b.untyped_storage())=}")

# 可以发现，虽然 a 和 b 的 storage 是不同的，但是它们的 untyped_storage 是相同的。并且，它们的 data_ptr 也是相同的。
