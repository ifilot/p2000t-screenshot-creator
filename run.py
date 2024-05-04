# -*- coding: utf-8 -*-

import psc

gen = psc.PSC()
gen.write_line(1, [psc.SC_CYAN, psc.SC_DOUBLE, "SDCARD READER              P2000T"])
gen.write_line(2, ["SD Card initialized"])
gen.write_line(3, ["Reading partition 1"])
gen.write_line(4, ["LBA partition 1:", psc.SC_GREEN, "00000040"])
gen.write_line(5, ["Bytes per sector:", psc.SC_GREEN, "512"])
gen.write_line(6, ["Bytes per sector:", psc.SC_GREEN, "512"])
gen.write_line(7, ["Sectors per FAT", psc.SC_GREEN, "7664"])
gen.write_line(8, ["Volume name:", psc.SC_GREEN, "P2000T"])
gen.write_line(9, ["Partition 1 mounted"])
gen.write_line(10, ["System ready"])
gen.write_line(11, [psc.SC_CYAN, ">", psc.SC_WHITE, 127])
gen.write_line(23, "Version: 0.6.0. Memory model: 48kb.")
gen.write_line(24, "Compiled at: May 02 2024 / 14:02:26")

gen.save("img/test.png")