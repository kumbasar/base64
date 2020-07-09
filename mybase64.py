#!/usr/bin/env python3

import base64

text = 'YmFzZTY0ZW5jb2RlZHN0cmluZw=='

text_bytes = text.encode('ascii')

try:
    print('Decoded: ' + base64.b64decode(text_bytes).decode("utf-8"))
except:
    print('Warning: Input string is not base64 decoded')

print('Encoded: ' + base64.b64encode(text_bytes).decode("utf-8"))
