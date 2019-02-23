
# coding: utf-8

# # Gait Energy Image

# In[1]:


import os
import numpy as np
import matplotlib.pyplot as plt
from imageio import imread
from scipy.misc import imresize
from skimage.transform import resize


# In[2]:


files = os.listdir('/home/DatasetB/silhouettes/001/nm-01/090/')
images = [imread('/home/DatasetB/silhouettes/001/nm-01/090/'+f) for f in files]


# In[3]:


plt.imshow(images[0])


# In[4]:


def mass_center(img,is_round=True):
    Y = img.mean(axis=1)
    X = img.mean(axis=0)
    Y_ = np.sum(np.arange(Y.shape[0]) * Y)/np.sum(Y)
    X_ = np.sum(np.arange(X.shape[0]) * X)/np.sum(X)
    if is_round:
        return int(round(X_)),int(round(Y_))
    return X_,Y_

def image_extract(img,newsize):
    x_s = np.where(img.mean(axis=0)!=0)[0].min()
    x_e = np.where(img.mean(axis=0)!=0)[0].max()
    
    y_s = np.where(img.mean(axis=1)!=0)[0].min()
    y_e = np.where(img.mean(axis=1)!=0)[0].max()
    
    x_c,_ = mass_center(img)
#     x_c = (x_s+x_e)//2
    x_s = x_c-newsize[1]//2
    x_e = x_c+newsize[1]//2
    img = img[y_s:y_e,x_s if x_s>0 else 0:x_e if x_e<img.shape[1] else img.shape[1]]
    return imresize(img,newsize)


# In[5]:


images = [image_extract(i,(128,64)) for i in images]


# In[6]:


plt.figure()
for i in range(10):
    plt.subplot(2,5,i+1)
    plt.imshow(images[i])
plt.show()


# In[7]:


gei = np.mean(images,axis=0)


# In[8]:


plt.imshow(gei)
plt.show()

