#!/usr/bin/env python
# coding: utf-8

# In[1]:


import hsluv


# In[2]:


for i in range(16):
    for j in range(16):
        for k in range(16):
            print("Hex #"f"{hex(i)[2:]}"f"{hex(i)[2:]}"f"{hex(j)[2:]}"f"{hex(j)[2:]}"f"{hex(k)[2:]}"f"{hex(k)[2:]}"f":")
            print("H: "f"{hsluv.rgb_to_hsluv((i/15,j/15,k/15))[0]:>6.2f}")
            print("S: "f"{hsluv.rgb_to_hsluv((i/15,j/15,k/15))[1]:>6.2f}")
            print("L: "f"{hsluv.rgb_to_hsluv((i/15,j/15,k/15))[2]:>6.2f}")


# In[3]:


for i in range(16):
    for j in range(16):
        for k in range(16):
            print("Hex #"f"{hex(i)[2:]}"f"{hex(i)[2:]}"f"{hex(j)[2:]}"f"{hex(j)[2:]}"f"{hex(k)[2:]}"f"{hex(k)[2:]}"f":")
            print("H: "f"{hsluv.rgb_to_hpluv((i/15,j/15,k/15))[0]:>6.2f}")
            print("P: "f"{hsluv.rgb_to_hpluv((i/15,j/15,k/15))[1]:>6.2f}")
            print("L: "f"{hsluv.rgb_to_hpluv((i/15,j/15,k/15))[2]:>6.2f}")


# In[4]:


for i in range(1,10):
    for j in range(11):
        for k in range(36):
            if j == 0 and k != 0:
                break
            print("HSLuv ("f"{k*10}"", "f"{j*10}"", "f"{i*10}"f"):")
            print("R: "f"{hsluv.hsluv_to_rgb((k*10,j*10,i*10))[0]:>6.3f}")
            print("G: "f"{hsluv.hsluv_to_rgb((k*10,j*10,i*10))[1]:>6.3f}")
            print("B: "f"{hsluv.hsluv_to_rgb((k*10,j*10,i*10))[2]:>6.3f}")


# In[5]:


for i in range(1,10):
    for j in range(11):
        for k in range(36):
            if j == 0 and k != 0:
                break
            print("HPLuv ("f"{k*10}"", "f"{j*10}"", "f"{i*10}"f"):")
            print("R: "f"{hsluv.hpluv_to_rgb((k*10,j*10,i*10))[0]:>6.3f}")
            print("G: "f"{hsluv.hpluv_to_rgb((k*10,j*10,i*10))[1]:>6.3f}")
            print("B: "f"{hsluv.hpluv_to_rgb((k*10,j*10,i*10))[2]:>6.3f}")


# In[ ]:




