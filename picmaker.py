import math, random

f = open("foo.ppm", "w")
f.write("P3 500 500 255\n")
i = 0
while(i < 500 * 500):
	f.write(str(math.sin(i + 1) % 255) +" " + str((i + random.randint(-30, 30)) % 255) + " " + str(math.tan(255 - i + 1) % 255) + " ")
	i += 1