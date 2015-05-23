#!/usr/bin/env python
import os
import sys
from SistReco.Sistemanuestro import *

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SecondApp.settings")

    from django.core.management import execute_from_command_line
    cargar()
    execute_from_command_line(sys.argv)
    # Create your views here.
