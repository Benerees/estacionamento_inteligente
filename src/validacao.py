import numpy as np
from sklearn.model_selection import LeaveOneOut 
import os
from PIL import Image


image_folder = "imagens da base de dados"  
image_list = []

for filename in os.listdir(image_folder):
    if filename.endswith(".jpg"):
        image_path = os.path.join(image_folder, filename)
        image = Image.open(image_path)
        image_list.append(image)

X = np.array(image_list)

loo = LeaveOneOut()
loo.get_n_splits(X)

print(loo)
LeaveOneOut()
for i, (train_index, test_index) in enumerate(loo.split(X)):
    print(train_index)
    print(test_index)

