#!/usr/bin/env python

# a python script to generate a MarkDown Table of Contents

import sys
import re

with open(sys.argv[1], "rb") as f:
  lines = f.readlines()

toc = []

for line in lines:
  m = re.match("(#+) (.*)", line.strip())
  if m is not None:
    label = m.group(2)
    spacing = (len(m.group(1))-1) * "  "
    anchor = label.lower().replace(" ", "-")
    for c in "'\":()&[]!'":
      anchor = anchor.replace(c,"")
    toc.append(
      "%s- [%s](#%s)" % (spacing, label, anchor)
      )

print "\n".join(toc)
