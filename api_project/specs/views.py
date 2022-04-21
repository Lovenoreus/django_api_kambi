from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import time
import signal
import sys
# Create your views here.

def sigterm_handler(_signo, _stack_frame):
    # Raises SystemExit(0):
    sys.exit(0)


def execute_file(request, filename):

    if sys.argv[1] == "handle_signal":
        signal.signal(signal.SIGTERM, sigterm_handler)

    path_file = "/Users/lovenoreus/desktop/program/kambi_django_api/executable_files/" + str(filename)
    exec(open(path_file).read())
    message = 'File "' + str(filename) + '" was executed successfully'
    time.sleep(1)
    return JsonResponse({"OK": message})

def list_files(request):
    
    from os import listdir
    from os.path import isfile, join

    if sys.argv[1] == "handle_signal":
        signal.signal(signal.SIGTERM, sigterm_handler)

    path = '/Users/lovenoreus/desktop/program/kambi_django_api/executable_files'
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f) )]
    file_dictionary = {}
    for index in range(len(onlyfiles)):
        file_number = index + 1
        if str(onlyfiles[index]) != '.DS_Store':
            file_dictionary["file_%s" %file_number] = str(onlyfiles[index])
      


    time.sleep(1)
    return JsonResponse(file_dictionary)

def my_custom_bad_request_view(*args, **kwargs):

        error_message = {"Test":"400"}
        return JsonResponse(error_message)

def my_custom_page_not_found_view(*args, **kwargs):

        error_message = {"Test":"404"}
        return JsonResponse(error_message)

def my_custom_internal_server_error_view(*args, **kwargs):

        error_message = {"Test":"500"}
        return JsonResponse(error_message)

def my_custom_not_implemented_view(*args, **kwargs):

        error_message = {"Test":"501"}
        return JsonResponse(error_message)
