# Lunar Gateway

## Description

Interface with the Lunar Gateway via a UART on the device, at 1,600 baud give or take.

The processor does not have an FPU and appears to execute 1 instruction per clock cycle. we have found a suitable emulation of the hardware and have included it in our files. The board has 2MB of RAM, to run the emulator execute the following command:

vmips -o memsize=2097152 <rom file>

One of our reverse engineers in poor hand writing, wrote something, but we can only interpret it as the following...

Find and read the flag at: 0xa2008000

nc 0.cloud.chals.io 19325
	
	Author: Cromulence

## Files

* [emulator](files/emulator)

* [service.rom](files/service.rom)

