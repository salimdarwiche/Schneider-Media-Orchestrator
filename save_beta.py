#!/usr/bin/env python3
"""
Save the Beta.html content retrieved from GitHub API
"""

# The HTML content from the GitHub API response
html_content = '''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width,initial-scale=1" />
<title>Schneider Electric Media Orchestrator — V6</title>

<!-- pdf.js core -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.min.js"></script>
'''

# This is just the beginning - the full content is ~52KB
# I need a better approach to transfer it

print("Content size would be:", len(html_content), "bytes (partial)")
print("Need to use file transfer from GitHub API response")

