# -*- coding: utf-8 -*-

import numpy as np
import os
from PIL import Image
import PIL.ImageFilter
import PIL.ImageDraw
import matplotlib.pyplot as plt

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
        self.pixheightsrc1 = 9
        self.pixwidthsrc1 = 5
        
        self.pixheightsrc2 = 10
        self.pixwidthsrc2 = 6
        
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

            # set number of rows and columns in the charmap
            rows = 10
            cols = 16
            
            # build charmap
            charmap = np.zeros((rows * self.pixheighttarget, cols * self.pixwidthtarget), dtype=np.uint8)
            for i in range(0,rows):
                for j in range(0,cols):
                    
                    if i * cols + j < 96:
                        for k in range(0,self.pixheightsrc1):
                            for l in range(0,self.pixwidthsrc1):
                                c = charlines[(i * cols + j) * self.pixheightsrc1 + k][l]
                                for n in range(0,2):
                                    for o in range(0,2):
                                        charmap[i * self.pixheighttarget + k*2 + 2 + n, 
                                                j * self.pixwidthtarget + l*2 + 2 + o] = (0 if c == '-' else 1)
                    else:
                        for k in range(0,self.pixheightsrc2):
                            for l in range(0,self.pixwidthsrc2):
                                idx = (i * cols + j) - 96
                                c = charlines[(96 * self.pixheightsrc1) + idx * self.pixheightsrc2 + k][l]
                                for n in range(0,2):
                                    for o in range(0,2):
                                        charmap[i * self.pixheighttarget + k*2 + n, 
                                                j * self.pixwidthtarget + l*2 + o] = (0 if c == '-' else 1)
        
        # apply filter
        charmap_filtered = np.zeros_like(charmap)
        # for i in range(0,6):
        #     for j in range(0,cols):
        #         p = (i * self.pixheighttarget, j * self.pixwidthtarget)
        #         for k in range(1,19):
        #             for l in range(1,11):
        #                 pc = (p[0] + k, p[1] + l)
        #                 p0 = (pc[0] - 1, pc[1] - 1)
        #                 p1 = (pc[0] - 1, pc[1] + 1)
        #                 p2 = (pc[0] + 1, pc[1] + 1)
        #                 p3 = (pc[0] + 1, pc[1] - 1)
                        
        #                 if charmap[p0[0], p0[1]] > 0.5 and charmap[p2[0], p2[1]] > 0.5:
        #                     charmap_filtered[pc[0], pc[1]] = 1
        #                 if charmap[p1[0], p1[1]] > 0.5 and charmap[p3[0], p3[1]] > 0.5:
        #                     charmap_filtered[pc[0], pc[1]] = 1
        
        return np.logical_or(charmap, charmap_filtered)
                                    
    def add_character(self, c, pos, color, bgcolor, double = False):
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
                
                col = tuple([c * color[i] + (1-c) * bgcolor[i] for i in range(3)])

                if double:
                    for k in range(0,2):
                        pixels[pos[1] * self.pixwidthtarget + j, 
                               (pos[0] - 1) * self.pixheighttarget + (i*2) + k] = col
                else:
                    pixels[pos[1] * self.pixwidthtarget + j, 
                           pos[0] * self.pixheighttarget + i] = col
    
    def write_vmem_file(self, filename):
        """
        Load a VRAM file and build screen from it
        """
        with open(filename, 'rb') as f:
            data = bytearray(f.read())
            self.write_vmem(data)
            
    def write_vmem(self, data):
        """
        Build a screen purely based on VRAM data
        """
        for i in range(0,24):
            
            bgcolor = BLACK
            color = WHITE
            double = False
            graphic = False
            
            for j in range(0,40):
                s = data[i * 40 + j]
                                    
                if s >= 0x20 and s < 0x80:
                    if graphic:
                        if s <= ord('?'):
                            s += 16 * 6
                        if  s >= ord('-') and s <= 127:
                            s += 16 * 4
                    self.add_character(int(s), (i, j), color, bgcolor, double)                        
                elif s < 0x08:
                    color = COLS[int(s)]
                    self.add_character(ord(' '), (i, j), color, bgcolor)
                elif s >= 0x10 and s < 0x18:
                    color = COLS[int(s) - 0x10]
                    graphic = True
                    self.add_character(ord(' '), (i, j), color, bgcolor)
                elif s == SC_DOUBLE:
                    double = True
                    self.add_character(ord(' '), (i, j), color, bgcolor)
                elif s == 0x1C: # black background color
                    bgcolor = BLACK
                    self.add_character(ord(' '), (i, j), color, bgcolor)
                elif s == 0x1D: # change background color
                    bgcolor = COLS[data[i * 40 + j - 1] - 0x10]
                    self.add_character(ord(' '), (i, j), color, bgcolor)
                elif s == 0x1F: # release graphics
                    graphic = False
                    self.add_character(ord(' '), (i, j), color, bgcolor)
                else:
                    print('Uncaptured byte: %i' % s)
                    
    def show(self):
        """
        Show the current canvas
        """
        self.canvas.show()
                
    def monitor_frame(self):
        """
        Place Canvas in a monitor frame
        """
        cs = (self.imh // 3 * 4 + 40, self.imh + 40)
        frame = Image.new('RGB', cs, color="#403c2c")
        im = PIL.ImageDraw.Draw(frame)
        im.rectangle((20, 20, cs[0] - 20, cs[1] - 20), fill='#000000')
        im.rectangle((0, 0, cs[0] - 1, cs[1] - 1), outline='#706b52')
        content = self.canvas.resize((int(self.imw * 1.33), self.imh), PIL.Image.NEAREST)
        frame.paste(content, ((cs[0] - content.size[0])//2,
                              (cs[1] - content.size[1])//2))
        im.rectangle((20, 20, cs[0] - 20, cs[1] - 20), outline='#706b52')
        return frame
    
    def plot_charmap(self):
        plt.figure(dpi=300)
        plt.imshow(self.charmap, cmap='gray_r')
        plt.xticks(np.arange(0, 16*12, 12) - 0.5, [])
        plt.yticks(np.arange(0, 10*20, 20) - 0.5, [])
        plt.grid(linestyle='--', color='black', alpha=0.5)
    
    def save(self, filename):
        """
        Store the canvas on disk
        """
        img = self.monitor_frame()
        img.save(filename)
        