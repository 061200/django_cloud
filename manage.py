#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

# from django.db import connection
#
# @csrf_exempt
# def mannerList(request):
#     if request.method == 'GET':
#         query_set = SmokingArea.objects.all()
#         serializer = SmokingSerializer(query_set, many=True)
#         return JsonResponse(serializer.data, safe=False)

def main():
    """Run administrative tasks."""
    #mannerList()
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
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
