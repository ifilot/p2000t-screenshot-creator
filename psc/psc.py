# -*- coding: utf-8 -*-

import numpy as np
import os
from PIL import Image
import PIL.ImageFilter
import PIL.ImageDraw

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
CYAN = (0,255,255)
MAGENTA = (255,0,255)

COLS = [
    BLACK,
    RED,
    GREEN,
    YELLOW,
    BLUE,
    MAGENTA,
    CYAN,
    WHITE
]

SC_NONE = 0x00
SC_RED = 0x01
SC_GREEN = 0x02
SC_YELLOW = 0x03
SC_BLUE = 0x04
SC_MAGENTA = 0x05
SC_CYAN = 0x06
SC_WHITE = 0x07
SC_DOUBLE = 0x0D

class PSC:
    
    def __init__(self):
        """
        Build class
        """
        # set class variables
        self.pixheightsrc = 9
        self.pixwidthsrc = 5
        
        self.pixheighttarget = 20
        self.pixwidthtarget = 12
        
        self.imw = 480 # image width
        self.imh = 500 # image height
        
        # initialize charmap and canvas
        self.charmap = self.build_charmap()
        self.canvas = Image.new('RGB', (self.imw, self.imh))
    
    def build_charmap(self):
        """
        Generate character map from txt file
        """
        path = os.path.join(os.path.dirname(__file__), 'fonts', 'English.txt')
        
        with open(path) as f:
            lines = f.readlines()
            
            charlines = []
            for line in lines:
                if line.startswith('-') or line.startswith('+'):
                    charlines.append(line.strip())

            rows = 8
            cols = 16
            
            charmap = np.zeros((rows * self.pixheighttarget, cols * self.pixwidthtarget), dtype=np.uint8)
            
            for i in range(0,rows):
                for j in range(0,cols):
                    for k in range(0,self.pixheightsrc):
                        for l in range(0,self.pixwidthsrc):
                            c = charlines[(i * 16 + j) * self.pixheightsrc + k][l]
                            for n in range(0,2):
                                for o in range(0,2):
                                    charmap[i * self.pixheighttarget + k*2 + 2 + n, 
                                            j * self.pixwidthtarget + l*2 + 2 + o] = (0 if c == '-' else 1)
        
        return charmap
                                    
    def add_character(self, c, pos, color, double = False):
        """
        Add a single character
        """
        pixels = self.canvas.load()
        
        idx = c - 0x20
        cpos = (idx // 16, idx % 16)
        for i in range(self.pixheighttarget):
            for j in range(self.pixwidthtarget):
                c = self.charmap[cpos[0] * self.pixheighttarget + i, 
                                 cpos[1] * self.pixwidthtarget + j]
                
                col = tuple([c * color[i] for i in range(3)])
                
                if double:
                    for k in range(0,2):
                        pixels[pos[1] * self.pixwidthtarget + j, 
                               (pos[0] - 1) * self.pixheighttarget + (i*2) + k] = col
                else:
                    pixels[pos[1] * self.pixwidthtarget + j, 
                           pos[0] * self.pixheighttarget + i] = col

    def write_line(self, line, lst):
        """
        Write a line to the screen
        """
        # construct byte array
        b = bytearray()
        
        # set starting color
        color = WHITE
        double = False
        
        for l in lst:
            if type(l) == str:
                b += bytearray(l.encode('ascii'))
            elif type(l) == int:
                b += bytearray([l])
        
        for i,s in enumerate(b):
            if s > 0x20:
                self.add_character(int(s), (line, i), color, double)
            elif s < 0x08:
                color = COLS[int(s)]
                self.add_character(ord(' '), (line, i), color)
            elif s == SC_DOUBLE:
                double = True
                self.add_character(ord(' '), (line, i), color)
    
    def show(self):
        """
        Show the current canvas
        """
        self.canvas.show()
        
    def upscale_and_blur(self):
        sf = 2
        img = self.canvas.resize((self.imw * sf, self.imh * sf), PIL.Image.NEAREST)
        #img = img.filter(PIL.ImageFilter.GaussianBlur(radius=5))
        #img = img.resize((self.imw, self.imh), PIL.Image.BICUBIC)
        img.show()
        
    def monitor_frame(self):
        """
        Place Canvas in a monitor frame
        """
        cs = (self.imh // 3 * 4 + 40, self.imh + 40)
        frame = Image.new('RGB', cs, color="#403c2c")
        im = PIL.ImageDraw.Draw(frame)
        im.rectangle((20, 20, cs[0] - 20, cs[1] - 20), fill='#000000')
        im.rectangle((0, 0, cs[0] - 1, cs[1] - 1), outline='#706b52')
        frame.paste(self.canvas, ((cs[0] - self.canvas.size[0])//2,
                                  (cs[1] - self.canvas.size[1])//2))
        im.rectangle((20, 20, cs[0] - 20, cs[1] - 20), outline='#706b52')
        return frame
        
    def save(self, filename):
        """
        Store the canvas on disk
        """
        img = self.monitor_frame()
        img.save(filename)
        