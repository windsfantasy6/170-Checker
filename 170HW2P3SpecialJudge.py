import sys
import math

if __name__ == "__main__":
  line = raw_input("Please input the C & N for subproblem 1:");
  #print line
  vals = line.strip().split(" ")
  c = float(vals[0])
  n0 = float(vals[1])
  #print 2 * n0 * n0 * n0 + 3
  #print c * n0 * n0 * n0 * n0 + 1e-8
  if 2 * n0 * n0 * n0 + 3 * n0 <= c * n0 * n0 * n0 * n0 + 1e-8:
    print "Right!"
  else:
    print "Wrong!"
  line = raw_input("Please input the C & N for subproblem 2:");
  vals = line.strip().split(" ")
  c = float(vals[0])
  n0 = float(vals[1])
  #print 8 + math.log(n0, 2)
  if 8 + math.log(n0, 2) <= c * n0 + 1e-8:
    print "Right!"
  else:
    print "Wrong!"

  line = raw_input("Please input the C & N for subproblem 3:");
  vals = line.strip().split(" ")
  c = float(vals[0])
  n0 = float(vals[1])
  if math.pow(2, n0) <= c * math.pow(math.log(n0, 2), n0) + 1e-8:
    print "Right!"
  else:
    print "Wrong!"


