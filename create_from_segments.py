#!/usr/bin/env python3
"""
Creates beta.html from the content retrieved via GitHub API
Split into segments to handle size constraints
"""

# Segment 1: HTML header through initial CSS
seg1 = '''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width,initial-scale=1" />
<title>Schneider Electric Media Orchestrator — V6 Beta</title>

<!-- pdf.js core -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.min.js"></script>

<style>
  :root{
    --se-life-green: #3DCD58;
    --se-logo-green: #009530;
    --se-dark-gray:  #626469;
    --se-light-gray: #9FA0A4;
    --se-white:      #FFFFFF;
    --se-black:      #000000;
    --border: rgba(159,160,164,0.65);
    --surface: #FFFFFF;
    --surface-alt: #F7F7F7;
    --text: #1f2937;
    --text-muted: #626469;
    --focus: #3DCD58;
    --agenda-accent: var(--se-life-green);
    --agenda-progress-bg: #e5e7eb;
  }
'''

# I'll need many more segments to reach 52KB
# For practical purposes, this approach is taking too long

print("Creating beta.html...")
print("Note: Complete 52KB file requires many segments")
print("Alternative needed for efficiency")

