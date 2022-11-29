import numpy as np
from PIL import Image
import time

#used characters
chars=['.',',',';','*','+','%','#','$','&','@']


def draw(name):
    
    #get rid of red and blue values
    img=np.array(Image.open(name+'.bmp')).reshape(360,480,3)[:,:,1]


    #current frame in ASCII
    frame=''
    
    for i in range(60):
   
        row=''
   
        for j in range(160):
    
            value=np.sum(img[i*6:i*6+6,j*3:j*3+3])

            #convert 3x6 region into a single ASCII character
            row+=chars[int(value/460)]
        
        frame+=(row+'\n')
    
    return frame[:-1]


frames=[""]*6567

st=time.time()
for i in range(1,6568):
        name=str(i)
        
        if len(name)<3:
        
            name='0'*(3-len(name))+name
       
        frames[i-1]=draw(name)
        print("Finished frame "+str(i)+" / 6567. Total time elapsed: " +str(time.time()-st)+"s")

input("Press enter to continue")

a=time.time()
for i in range(0,6567):
        print(frames[i])
        b=time.time()-a
        if b<(i+1)/30:
            time.sleep((i+1)/30-b)
