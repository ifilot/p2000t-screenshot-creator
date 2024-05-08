# -*- coding: utf-8 -*-

import psc

def main():
    # boot()
    # ls()
    # cd6()
    # lscas()
    # runfraxxon()
    # runfraxxon_checksum()
    # hexdump_fraxxon()
    # invalid_command()
    # flasher_boot()
    # flasher_done()
    # galgje_intro()
    # fraxxon_intro()
    gen = psc.PSC()
    gen.plot_charmap()
    pass

def galgje_intro():
    gen = psc.PSC()
    gen.write_vmem_file('vmemdumps/galgje.vram')
    gen.save("img/" + "galgje.png")
    
def fraxxon_intro():
    gen = psc.PSC()
    gen.write_vmem_file('vmemdumps/fraxxon.vram')
    gen.save("img/" + "fraxxon.png")

def invalid_command():
    lines = []
    
    lines = []
    lines.append(["SD Card initialized"])
    lines.append(["Reading partition 1"])
    lines.append(["Bytes per sector:", psc.SC_GREEN, "512"])
    lines.append(["Partition size:", psc.SC_GREEN, "3832 MiB"])
    lines.append(["Volume name:", psc.SC_GREEN, "P2000T"])
    lines.append(["Partition 1 mounted"])
    lines.append(["System ready"])
    lines.append([psc.SC_CYAN, ">", psc.SC_WHITE, "blaat"])
    lines.append([psc.SC_RED, "ERROR", psc.SC_WHITE, "Invalid command"])
    lines.append([psc.SC_CYAN, ">", psc.SC_WHITE, 127])
    
    lines = reformat_lines(lines, 3)
    
    build_screenshot_launcher(lines, "invalid_command.png")

def flasher_boot():
    lines = []
    lines.append(["System booted."])
    lines.append(["Press any key to search SD card for"])
    lines.append(["flashable file."])
    
    lines = reformat_lines(lines, 3)
    
    build_screenshot_flasher(lines, "flasher_boot.png")
    
def flasher_done():
    lines = []
    lines.append(["SD Card initialized"])
    lines.append(["Reading partition 1"])
    lines.append(["Bytes per sector:", psc.SC_GREEN, "512"])
    lines.append(["Partition size:", psc.SC_GREEN, "3832 MiB"])
    lines.append(["Volume name:", psc.SC_GREEN, "P2000T"])
    lines.append(["Partition 1 mounted"])
    lines.append([])
    lines.append(["LAUNCHER.BIN found: ", psc.SC_GREEN, "11520 Bytes"])
    lines.append(["Connection to ROM chip established."])
    lines.append(["Device signature", psc.SC_CYAN, "B5BF", psc.SC_WHITE, ": SST39SF010"])
    lines.append(["Wiping 0x0000-0x3FFF"])
    lines.append(["Copying LAUNCHER.BIN, please wait..."])
    lines.append(["Done parsing 23 / 23 sectors"])
    lines.append([])
    lines.append(["Calculating CRC16, please wait..."])
    lines.append(["Checksum succesfully validated."])
    lines.append([])
    lines.append([psc.SC_GREEN, "FLASHING COMPLETED!"])
    
    lines = reformat_lines(lines, 3)
    
    build_screenshot_flasher(lines, "flasher_done.png")

def hexdump_fraxxon():
    lines = []
    ln = 3
    lines.append((ln, ["Filename: FRAXXON. CAS"]))
    ln += 1
    for i in range(6):
        lines.append((ln, [psc.SC_YELLOW,
                               "%04X" % (i * 8),
                               psc.SC_WHITE,
                               "00 00 00 00 00 00 00 00",
                               psc.SC_CYAN,
                               "........"]))
        ln += 1
    
    lines.append((ln, [psc.SC_YELLOW,
                           "0030",
                           psc.SC_WHITE,
                           "47 65 B9 5F B9 5F 46 72",
                           psc.SC_CYAN,
                           "Ge.",0x5F,".",0x5F,"Fr"]))
    ln += 1
    
    lines.append((ln, [psc.SC_YELLOW,
                           "0038",
                           psc.SC_WHITE,
                           "61 78 78 6F 6E 00 42 41",
                           psc.SC_CYAN,
                           "axxon.BA"]))
    
    ln += 1
    
    lines.append((ln, [psc.SC_YELLOW,
                           "0040",
                           psc.SC_WHITE,
                           "53 42 4E B9 5F 00 00 00",
                           psc.SC_CYAN,
                           "SBN.", 0x5F, "..."]))
    
    ln += 1
    
    lines.append((ln, [psc.SC_YELLOW,
                           "0048",
                           psc.SC_WHITE,
                           "00 00 00 00 00 00 00 18",
                           psc.SC_CYAN,
                           "........"]))
    
    ln += 1
    
    for i in range(6):
        lines.append((ln, [psc.SC_YELLOW,
                               "%04X" % ((i+10) * 8),
                               psc.SC_WHITE,
                               "00 00 00 00 00 00 00 00",
                               psc.SC_CYAN,
                               "........"]))
        ln += 1
    
    lines.append((ln, [psc.SC_CYAN, ">", psc.SC_WHITE, 127]))
    build_screenshot_launcher(lines, "hexdump-fraxxon.png")

def runfraxxon_checksum():
    lines = []
    
    lines.append(["Reading partition 1"])
    lines.append(["Bytes per sector:", psc.SC_GREEN, "512"])
    lines.append(["Partition size:", psc.SC_GREEN, "3832 MiB"])
    lines.append(["Volume name:", psc.SC_GREEN, "P2000T"])
    lines.append(["Partition 1 mounted"])
    lines.append(["System ready"])
    lines.append([psc.SC_CYAN, ">", psc.SC_WHITE, "cd 6"])
    lines.append([psc.SC_CYAN, ">", psc.SC_WHITE, "run 45"])
    lines.append(["Filename: FRAXXON.CAS"])
    lines.append(["Filesize: 30720 bytes"])
    lines.append(["Done loading 60 / 60 sectors"])
    lines.append(["Deploy addr: ", psc.SC_CYAN, "0x6547"])
    lines.append(["Program length: ", psc.SC_CYAN, "0x5FB9"])
    lines.append(["Top RAM: ", psc.SC_CYAN, "0xC500"])
    lines.append(["Press c to calculate checksum or any"])
    lines.append(["other key to launch program."])
    lines.append(["CRC16 checksum: ", psc.SC_CYAN, "0x0C3F"])
    lines.append(["Press any key to start program"])
    
    lines = reformat_lines(lines, 3)
    
    build_screenshot_launcher(lines, "run-fraxxon-checksum.png")

def runfraxxon():
    lines = []
    
    lines.append(["SD Card initialized"])
    lines.append(["Reading partition 1"])
    lines.append(["Bytes per sector:", psc.SC_GREEN, "512"])
    lines.append(["Partition size:", psc.SC_GREEN, "3832 MiB"])
    lines.append(["Volume name:", psc.SC_GREEN, "P2000T"])
    lines.append(["Partition 1 mounted"])
    lines.append(["System ready"])
    lines.append([psc.SC_CYAN, ">", psc.SC_WHITE, "cd 6"])
    lines.append([psc.SC_CYAN, ">", psc.SC_WHITE, "run 45"])
    lines.append(["Filename: FRAXXON.CAS"])
    lines.append(["Filesize: 30720 bytes"])
    lines.append(["Done loading 60 / 60 sectors"])
    lines.append(["Deploy addr: ", psc.SC_CYAN, "0x6547"])
    lines.append(["Program length: ", psc.SC_CYAN, "0x5FB9"])
    lines.append(["Top RAM: ", psc.SC_CYAN, "0xC500"])
    lines.append(["Press c to calculate checksum or any"])
    lines.append(["other key to launch program."])
    
    lines = reformat_lines(lines, 3)
    
    build_screenshot_launcher(lines, "run-fraxxon.png")

def lscas():
    lines = []
    lines.append((3, [psc.SC_CYAN, ">", psc.SC_WHITE, "lscas"]))
    
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
    
    linenr = 4
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
    
    build_screenshot_launcher(lines, "lscas.png")

def cd6():
    lines = []
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
    lines.append((linenr, [psc.SC_CYAN, ">", psc.SC_WHITE, "cd 6"]))
    linenr += 1
    lines.append((linenr, [psc.SC_CYAN, ">", psc.SC_WHITE, 127]))
    
    build_screenshot_launcher(lines, "cd6.png")

def ls():
    lines = []
    lines.append((3, ["Volume name:", psc.SC_GREEN, "P2000T"]))
    lines.append((4, ["Partition 1 mounted"]))
    lines.append((5, ["System ready"]))
    lines.append((6, [psc.SC_CYAN, ">", psc.SC_WHITE, "ls"]))
    
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
    
    linenr = 7
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
    
    build_screenshot_launcher(lines, "ls.png")

def boot():
    """
    Create screenshot for SD card boot
    """
    lines = []
    lines.append((3, ["SD Card initialized"]))
    lines.append((4, ["Reading partition 1"]))
    lines.append((5, ["Bytes per sector:", psc.SC_GREEN, "512"]))
    lines.append((6, ["Partition size:", psc.SC_GREEN, "3832 MiB"]))
    lines.append((7, ["Volume name:", psc.SC_GREEN, "P2000T"]))
    lines.append((8, ["Partition 1 mounted"]))
    lines.append((9, ["System ready"]))
    lines.append((10, [psc.SC_CYAN, ">", psc.SC_WHITE, 127]))
    
    build_screenshot_launcher(lines, "boot.png")

def lines_to_vram(lines):
    """
    Convert lines to VRAM
    """
    data = bytearray([0x00] * 24 * 40)
    
    for line in lines:
        ctr = 0
        for i in line[1]:
            if type(i) == str:
                for c in i:
                    data[40 * line[0] + ctr] = ord(c)
                    ctr += 1
            else:
                data[40 * line[0] + ctr] = i
                ctr += 1
    return data

def build_screenshot_launcher(lines, filename):
    """
    Build a screenshot for a launcher screen
    """
    gen = psc.PSC()
    lines = header(lines)
    lines = footer(lines)
    data = lines_to_vram(lines)
    gen.write_vmem(data)
    gen.save("img/" + filename)
    
def build_screenshot_flasher(lines, filename):
    """
    Build a screenshot for a flasher screen
    """
    gen = psc.PSC()
    lines = header_flasher(lines)
    lines = footer_flasher(lines)
    data = lines_to_vram(lines)
    gen.write_vmem(data)
    gen.save("img/" + filename)

def header(lines):
    """
    Add the header for the SD card screens
    """
    lines.append((2, [psc.SC_CYAN, psc.SC_DOUBLE, "SDCARD READER              P2000T"]))
    return lines

def footer(lines):
    """
    Add the footer for the SD card screens
    """
    lines.append((22, "Version: 0.6.0. Memory model: 48kb."))
    lines.append((23, "Compiled at: May 02 2024 / 14:02:26"))
   
    return lines
   
def header_flasher(lines):
    """
    Add the header for the flash screens
    """
    lines.append((2, [psc.SC_CYAN, psc.SC_DOUBLE, "SDCARD FLASHER"]))
    
    return lines

def footer_flasher(lines):
    """
    Add the footer for the flash screens
    """
    lines.append((22, "Version: 0.6.0"))
    lines.append((23, "Compiled at: May 02 2024 / 14:02:26"))
   
    return lines

def reformat_lines(lines, start):
    """
    Reformat the lines such that all the lines are given a line number
    """
    newlines = []
    
    for i,line in enumerate(lines):
        newlines.append((start + i, line))
        
    return newlines

if __name__ == '__main__':
    main()