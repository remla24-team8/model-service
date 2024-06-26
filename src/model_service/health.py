"""
This script allows for testing whether the app has started,
which is only after it has (downloaded and) started the models, which can take up to 15 seconds.
This can then be used by Docker Compose to wait for it to be healthy.
"""

import sys
import requests

try:
    r = requests.get("http://localhost:5000/ready", timeout=0.5)
    if r.status_code != 200:
        sys.exit(1)
except Exception as e:
    sys.exit(1)
