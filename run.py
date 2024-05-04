# -*- coding: utf-8 -*-

import psc

def main():
    #boot()
    #ls()
    #cd6()
    #lscas()
    runfraxxon_checksum()

def runfraxxon_checksum():
    lines = []
    lines.append((2, ["Reading partition 1"]))
    lines.append((3, ["Bytes per sector:", psc.SC_GREEN, "512"]))
    lines.append((4, ["Partition size:", psc.SC_GREEN, "3832 MiB"]))
    lines.append((5, ["Volume name:", psc.SC_GREEN, "P2000T"]))
    lines.append((6, ["Partition 1 mounted"]))
    lines.append((7, ["System ready"]))
    lines.append((8, [psc.SC_CYAN, ">", psc.SC_WHITE, "cd 6"]))
    lines.append((9, [psc.SC_CYAN, ">", psc.SC_WHITE, "run 45"]))
    lines.append((10, ["Filename: FRAXXON.CAS"]))
    lines.append((11, ["Filesize: 30720 bytes"]))
    lines.append((12, ["Done loading 60 / 60 sectors"]))
    lines.append((13, ["Deploy addr: ", psc.SC_CYAN, "0x6547"]))
    lines.append((14, ["Program length: ", psc.SC_CYAN, "0x5FB9"]))
    lines.append((15, ["Top RAM: ", psc.SC_CYAN, "0xC500"]))
    lines.append((16, ["Press c to calculate checksum or any"]))
    lines.append((17, ["other key to launch program."]))
    lines.append((18, ["CRC16 checksum: ", psc.SC_CYAN, "0x0C3F"]))
    lines.append((19, ["Press any key to start program"]))
    
    build_screenshot(lines, "run-fraxxon-checksum.png")

def runfraxxon():
    lines = []
    lines.append((2, ["SD Card initialized"]))
    lines.append((3, ["Reading partition 1"]))
    lines.append((4, ["Bytes per sector:", psc.SC_GREEN, "512"]))
    lines.append((5, ["Partition size:", psc.SC_GREEN, "3832 MiB"]))
    lines.append((6, ["Volume name:", psc.SC_GREEN, "P2000T"]))
    lines.append((7, ["Partition 1 mounted"]))
    lines.append((8, ["System ready"]))
    lines.append((9, [psc.SC_CYAN, ">", psc.SC_WHITE, "cd 6"]))
    lines.append((10, [psc.SC_CYAN, ">", psc.SC_WHITE, "run 45"]))
    lines.append((11, ["Filename: FRAXXON.CAS"]))
    lines.append((12, ["Filesize: 30720 bytes"]))
    lines.append((13, ["Done loading 60 / 60 sectors"]))
    lines.append((14, ["Deploy addr: ", psc.SC_CYAN, "0x6547"]))
    lines.append((15, ["Program length: ", psc.SC_CYAN, "0x5FB9"]))
    lines.append((16, ["Top RAM: ", psc.SC_CYAN, "0xC500"]))
    lines.append((17, ["Press c to calculate checksum or any"]))
    lines.append((18, ["other key to launch program."]))
    
    build_screenshot(lines, "run-fraxxon.png")

def lscas():
    lines = []
    lines.append((2, [psc.SC_CYAN, ">", psc.SC_WHITE, "lscas"]))
    
    files = [
     (".", 0, 0x135),
     ("..", 0, 0x000),
     ("Vier op een rij", 3, 2955),
     ("alggrot", 2, 1447),
     ("Alice's wonderl.", 18, 17599),
     ("Start-up", 3, 2970),
     ("Androide-nim.BAS", 11, 11164),
     ("azuda", 12, 11961),
     ("BABA.bas", 1, 452),
     ("Info Bat.S...Bas", 5, 4936),
     ("D", 6, 5514),
     ("Beursspel", 6, 5650),
     ("Bingo.BAS", 6, 5974),
     ("Bl", 8, 8145),
     ("Bom", 4, 3503),
     ("boter kaas", 2, 1829),
    ]
    
    linenr = 3
    for i,f in enumerate(files):
        
        base = f[0]
        if i < 2:
            ext = "DIR"          
            if len(base) < 8:
                for j in range(8 - len(base)):
                    base += ' '
        else:
            if len(base) < 16:
                for j in range(16 - len(base)):
                    base += ' '
            base += ' '
            ext = "BAS"
            
        if len(ext) < 3:
            for i in range(3 - len(ext)):
                ext += '  '
        
        if i == 15:
            ext = "AVR"
        if i == 10:
            ext = '   '
        if i == 5:
            ext = 'bas'
        
        if i < 2:
            lines.append((linenr, [psc.SC_YELLOW if ext == "DIR" else psc.SC_GREEN, 
                                   "%3i" % (i+1), psc.SC_WHITE, 
                                   "%s%s" % (base, ext), 
                                   psc.SC_YELLOW, 
                                   ("%6i" % f[1]) if f[1] != 0 else "       ",
                                   psc.SC_CYAN, 
                                   "%08X" % f[2]]))
        else:
            lines.append((linenr, [psc.SC_YELLOW if ext == "DIR" else psc.SC_GREEN,
                                   "%3i" % (i+1), psc.SC_YELLOW, 
                                   "%s%s" % (base, ext), 
                                   psc.SC_CYAN, 
                                   ("%2i" % f[1]) if f[1] != 0 else "      ",
                                   psc.SC_CYAN, 
                                   "%6i" % f[2]]))
            
        linenr += 1
    
    lines.append((linenr, ["-- Press key to continue, q to quit --"]))
    
    build_screenshot(lines, "lscas.png")

def cd6():
    lines = []
    lines.append((2, ["Partition 1 mounted"]))
    lines.append((3, ["System ready"]))
    lines.append((4, [psc.SC_CYAN, ">", psc.SC_WHITE, "ls"]))
    
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
    
    linenr = 5
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
        
        lines.append((linenr, [psc.SC_YELLOW if ext == "DIR" else psc.SC_GREEN, 
                               "%3i" % (i+1), psc.SC_WHITE, 
                               "%s%s" % (base, ext), 
                               psc.SC_YELLOW, 
                               ("%6i" % f[1]) if f[1] != 0 else "      ",
                               psc.SC_CYAN, 
                               "%08X" % f[2]]))
        linenr += 1
    
    lines.append((linenr, ["    12 File(s)      11840 Bytes"]))
    linenr += 1
    lines.append((linenr, [psc.SC_CYAN, ">", psc.SC_WHITE, "cd 6"]))
    linenr += 1
    lines.append((linenr, [psc.SC_CYAN, ">", psc.SC_WHITE, 127]))
    
    build_screenshot(lines, "cd6.png")

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
        
        lines.append((linenr, [psc.SC_YELLOW if ext == "DIR" else psc.SC_GREEN, 
                               "%3i" % (i+1), psc.SC_WHITE, 
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