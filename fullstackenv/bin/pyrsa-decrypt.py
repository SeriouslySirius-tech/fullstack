#!/Users/pranavyadlapati/Desktop/new-fullstack/fullstackenv/bin/python
# -*- coding: utf-8 -*-
import re
import sys
from rsa.cli import decrypt
if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    sys.exit(decrypt())