
from PIL import Image
import numpy as np
from subprocess import check_output



class png2ascii:
    def __init__(self, path):
        self.img = np.asarray(Image.open(path).convert('L'), dtype='int32')
        
        self.increments = ['  ', '..', '::', '!!', '//', 'xx', 'XX', '@@']
        self.incrNum = len(self.increments)


    def __str__(self):
        string = '\n'
        for row in self.img:
            for pix in row:
                string += self.increments[int(self.incrNum/255*pix-1)]
            string += '\n'
        return string



print(png2ascii('orig.png'))