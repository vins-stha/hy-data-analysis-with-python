import matplotlib.pyplot as plt
import numpy as np

def fadex(image):
    ht,wt,depth = image.shape[:3]
    m = np.linspace(0,1,wt)
    print()
    #print(m[:4], type(m), m.shape)
    #print("dim m = ",m.ndim)
    m = m.reshape(1,wt,1)

    result = image*m
    print("result = ",result.ndim)
    #for i in range(0,5):
    print("{}=={}****{} === {}".format(1,image[:1,:1,:1],m[:1,:1,:1],result[:1,:1,:1]))
    print("{}=={}****{} === {}".format(2,image[:2,:2,:2],m[:2,:2,:2],result[:2,:2,:2]))
    print("{}=={}****{} === {}".format(3,image[:3,:3,:3],m[:3,:3,:3],result[:3,:3,:3]))

    #print(m[:,:10])
   # print(len(m),(m.ndim), m.shape)
  #  print(ht,wt,depth)
    return 0
plt.figure(figsize=(2,2))
painting=plt.imread("src/image.jpg")
""" for i in range(1,5):
    plt.subplot(2,2,i) """

red = painting[:,:,0]
green = painting[:,:,1]
blue = painting[:,:,2]

img = np.array([blue,green,red])
print(" here >>",np.ndim(img),">>",(img[0]))
img = np.swapaxes(img, 0,1)
img = np.swapaxes(img, 1,2)
print(" here >>",np.ndim(img), ">>> ",(img[0]))

print(np.shape(img))
plt.subplot(2,2,2)
painting2 = painting.copy()
painting2[100:200, : , 0] = 255
painting2[300:400, : , 1] = 255
painting2[500:600, : , 2] = 255
#plt.figure(figsize=(10,10))
plt.imshow(painting2)

plt.subplot(2,2,1)
colr0 = painting[:,:,0]


plt.imshow(painting2)

plt.subplot(2,2,3)
colr0 = painting[:,:,1]
plt.imshow(colr0)

plt.subplot(2,2,4)
colr0 = painting[:,:,2]
plt.imshow(colr0)


plt.show()
























plt.imshow(painting[:600,::-1])#,colormap =  "tab20b")
painting2 = painting.copy()
painting2[0:500,:,:] = 0.0
plt.imshow(painting2)
print(type(painting),painting.ndim, painting.shape)
print(painting[1][1][0])
#fadex(painting)
#plt.show()




#plt.show()

