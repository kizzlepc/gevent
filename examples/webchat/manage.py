#!/usr/bin/python
from django.core.management import execute_manager
try:
    import settings  # Assumed to be in the same directory.
except ImportError:
    import sys
    sys.stderr.write("""Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.
You'll have to run django-admin.py, passing it your settings module.
(If the file settings.py does indeed exist, it's causing an ImportError somehow.)
""" % __file__)
    raise

if __name__ == "__main__":
    execute_manager(settings)
