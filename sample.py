from math import sin, pi, ceil
import sys


note = float(sys.argv[1])
print("Given Frequency is", note, "Hz.") #first argument only

if len(sys.argv) == 3:
	LRCK = int(sys.argv[2])
else:
	LRCK = 44100
print("Current Sampling Frequency (LRCK) is", LRCK/1000, "kHz")

f = open('{0} Hz at Sample Rate of {1} kHz.txt'.format(note, LRCK/1000), 'w')

sampleCount = 0
previousSample = 0
sample = 0

for i in range(0, LRCK): #first quarter of full cycle
	sample = sin(note * 2 * 3.14 * i/LRCK)
	if sample < previousSample:
		break
	else:
		if i != 0:
			f.write("\n")
		f.write(str(sample))
		sampleCount += 1
		previousSample = sample
	
f.close()

print(sampleCount, "samples output into \'{0} Hz at Sample Rate of {1} kHz.txt\'".format(note, LRCK/1000))