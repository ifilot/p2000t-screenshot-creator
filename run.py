# -*- coding: utf-8 -*-

import psc

def main():
    boot()
    ls()
    
def ls():
    lines = []
    lines.append((2, ["Volume name:", psc.SC_GREEN, "P2000T"]))
    lines.append((3, ["Partition 1 mounted"]))
    lines.append((4, ["System ready"]))
    lines.append((5, [psc.SC_CYAN, ">", psc.SC_WHITE, "ls"]))
    
    files = [
     ("README.MD", 320, 0x6),
     ("ADMINI~1.DIR", 0, 0x7),
     ("COMMUN~1.DIR", 0, 0x45),
     ("DEMO.DIR", 0, 0x71),
     ("EDUCAT~1.DIR", 0, 0xAC),
     ("GAMES.DIR", 0, 0x135),
     ("NEWS.DIR", 0, 0x310),
     ("PRINTER.DIR", 0, 0x315),
     ("PROGRA~1.DIR", 0, 0x329),
     ("UTILIT~1.DIR", 0, 0x34F),
     ("LAUNCHER.BIN", 11520, 0x3D6),
     ("PROGRAMS.DIR", 0, 0x3D9),
    ]
    
    linenr = 6
    for i,f in enumerate(files):
        pieces = f[0].split(".")
        
        base = pieces[0]
        if len(base) < 8:
            for i in range(8 - len(base)):
                base += ' '
        ext = pieces[1]
        if ext != "DIR":
            base += '.'
        else:
            base += ' '
            
        if len(ext) < 3:
            for i in range(3 - len(ext)):
                ext += ' '
        
        lines.append((linenr, [psc.SC_GREEN, "%3i" % (i+1), psc.SC_WHITE, 
                          "%s%s" % (base, ext), 
                          psc.SC_YELLOW, 
                          ("%6i" % f[1]) if f[1] != 0 else "      ",
                          psc.SC_CYAN, 
                          "%08X" % f[2]]))
        linenr += 1
    
    lines.append((linenr, ["    12 File(s)      11840 Bytes"]))
    linenr += 1
    lines.append((linenr, [psc.SC_CYAN, ">", psc.SC_WHITE, 127]))
    
    build_screenshot(lines, "ls.png")

def boot():
    lines = []
    lines.append((2, ["SD Card initialized"]))
    lines.append((3, ["Reading partition 1"]))
    lines.append((4, ["Bytes per sector:", psc.SC_GREEN, "512"]))
    lines.append((5, ["Partition size:", psc.SC_GREEN, "3832 MiB"]))
    lines.append((6, ["Volume name:", psc.SC_GREEN, "P2000T"]))
    lines.append((7, ["Partition 1 mounted"]))
    lines.append((8, ["System ready"]))
    lines.append((9, [psc.SC_CYAN, ">", psc.SC_WHITE, 127]))
    
    build_screenshot(lines, "boot.png")

def build_screenshot(lines, filename):
    gen = psc.PSC()
    header(gen)
    for l in lines:
        gen.write_line(l[0], l[1])
        
    footer(gen)
    gen.save("img/" + filename)

def header(gen):
    gen.write_line(1, [psc.SC_CYAN, psc.SC_DOUBLE, "SDCARD READER              P2000T"])

def footer(gen):
   gen.write_line(23, "Version: 0.6.0. Memory model: 48kb.")
   gen.write_line(24, "Compiled at: May 02 2024 / 14:02:26")
   
if __name__ == '__main__':
    main()