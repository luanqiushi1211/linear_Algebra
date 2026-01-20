import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

class imageSvd():
    def __init__(self,image_path,k):
        self.image_path = image_path
        self.k = k
    
    def svd_image(self):
        img = np.array(Image.open(self.image_path).convert("L"))

        U,sigma,VT = np.linalg.svd(img)
        
        P = int(len(sigma)*self.k)

        SP = sigma[:P]

        sigmaP = np.diag(SP)

        UP = U[:,:P]

        VTP = VT[:P,:]

        imagP = UP@sigmaP@VTP

        return imagP
    
    def showImage(self, *image):
        length = len(image)
        fig, aex = plt.subplots(1, length, figsize=(10, 10), squeeze=False)
        
        for index, imageinfo in enumerate(image):
            ax = aex[0, index]
            title, img = imageinfo
            ax.imshow(img, cmap='gray')
            ax.set_title(title)
            ax.axis('off')
        plt.show()

if __name__ == '__main__':
    isd = imageSvd(r'G:\素材\图片\鬼灭之刃\人物\富冈义勇\最终版放大.png',0.3)    
    imagP = isd.svd_image()
    isd.showImage(('origin',np.array(Image.open(isd.image_path).convert("L"))),('svd',imagP))



