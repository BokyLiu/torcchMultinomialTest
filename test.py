import torch
import numpy as np

times = 100

label_to_count = np.array([5, 5, 5 ,5 ,5 ,2, 2, 3, 3, 3])

weights = 1./label_to_count

label0 = 0
label1 = 0
label2 = 0
for time in range(times):
    select = torch.multinomial(torch.from_numpy(weights), 10, replacement=True).tolist()
    for idx in select:
        if idx >=0 and idx<=4:
            label0 += 1
        if idx >=5 and idx<=6:
            label1 += 1
        if idx >=7 and idx<=9:
            label2 += 1
    print('epoch%d: label0 = %d, label1 = %d, label2 = %d' % (time, label0,label1,label2))
watch = 0
