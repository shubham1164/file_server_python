from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
import logging
import json
import sys
import os
from datetime import datetime
from rest_framework import status
from rest_framework.response import Response
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

def simple_upload(request, destination):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        # Delete old file
        if os.path.exists(destination):
            os.remove(destination)
        # Save file
        fs = FileSystemStorage()
        filename = fs.save(destination, myfile)
        print(datetime.now(), ": File saved at ", filename)
        return True
    return False


@api_view(["POST"])
def upload_ppg(request):
    try:
        # Load configs.json
        configs = json.load(open('config.json'))
        ppg_upload_path = configs['ppg_upload_path']

        print(datetime.now(), "Starting uploading....")
        simple_upload(request, configs['ppg_upload_path'])
        print(datetime.now(), "Uploading done")

        # Display the result
        return HttpResponse("Done", status=200)
    except Exception as e:
        logging.error('Error at %s', 'division', exc_info=e)
        return HttpResponse("Error occured"+e, status=500)


@api_view(["POST"])
def upload_eeg(request):
    try:
        # Load configs.json
        configs = json.load(open('config.json'))
        eeg_upload_path = configs['eeg_upload_path']

        print(datetime.now(), "Starting uploading....")
        simple_upload(request, configs['eeg_upload_path'])
        print(datetime.now(), "Uploading done")

        # Display the result
        return HttpResponse("Done", status=200)
    except Exception as e:
        logging.error('Error at %s', 'division', exc_info=e)
        return HttpResponse("Error occured"+e, status=500)

@api_view(["GET"])
def read_output(request):
    try:
        # Load configs.json
        configs = json.load(open('config.json'))
        result_path = configs['result_path']

        # Load the output file
        finalOutput = json.load(open(result_path))

        # Display the result
        return JsonResponse(finalOutput)
    except Exception as e:
        logging.error('Error at %s', 'division', exc_info=e)
        return HttpResponse("Error occured", status=500)
