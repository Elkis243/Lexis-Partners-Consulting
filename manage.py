#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from lexis_partners_consulting.settings import base


def main():
    
    if base.DEBUG:
        os.environ['DJANGO_SETTINGS_MODULE'] = 'lexis_partners_consulting.settings.local'
    else:
        os.environ['DJANGO_SETTINGS_MODULE'] = 'lexis_partners_consulting.settings.production'
    
    
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
