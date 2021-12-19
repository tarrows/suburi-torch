from pathlib import Path
from torchvision import datasets

data_path = Path.cwd() / 'data'

dataset = datasets.CIFAR10(data_path, train=True, download=True)
dataset_val = datasets.CIFAR10(data_path, train=False, download=True)

# check module resolution order
print(type(dataset).__mro__)
