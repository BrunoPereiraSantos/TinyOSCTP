#! /usr/bin/python
from TOSSIM import *
import sys

t = Tossim([])
r = t.radio()
f = open("topo.txt", "r")
outFile = open("log.txt", "w")

for line in f:
  s = line.split()
  if s:
    print " ", s[0], " ", s[1], " ", s[2];
    r.add(int(s[0]), int(s[1]), float(s[2]))

t.addChannel("TreeRoutingCtl", sys.stdout)
t.addChannel("TreeRouting", sys.stdout)
t.addChannel("RoutingTimer", sys.stdout)
t.addChannel("RoutingTimer", sys.stdout)
t.addChannel("LITest", sys.stdout)
t.addChannel("BRUNO_RE", sys.stdout)
t.addChannel("EasyCollection", sys.stdout)

t.addChannel("TreeRoutingCtl", outFile)
t.addChannel("TreeRouting", outFile)
t.addChannel("RoutingTimer", outFile)
t.addChannel("RoutingTimer", outFile)
t.addChannel("LITest", outFile)
t.addChannel("BRUNO_RE", outFile)
t.addChannel("EasyCollection", outFile)


noise = open("../../tos/lib/tossim/noise/meyer-heavy.txt", "r")
for line in noise:
  str1 = line.strip()
  if str1:
    val = int(str1)
    for i in range(1, 10):
      t.getNode(i).addNoiseTraceReading(val)

for i in range(1, 10):
  print "Creating noise model for ",i;
  t.getNode(i).createNoiseModel()

t.getNode(1).bootAtTime(1001);
t.getNode(2).bootAtTime(6008);
t.getNode(3).bootAtTime(4009);
t.getNode(4).bootAtTime(1050);
t.getNode(5).bootAtTime(3050);
t.getNode(6).bootAtTime(5050);
t.getNode(7).bootAtTime(7050);
t.getNode(8).bootAtTime(3550);
t.getNode(9).bootAtTime(4450);



t.runNextEvent();
time = t.time()
while time + 100000000000 > t.time():
  t.runNextEvent()

