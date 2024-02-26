from django.http import HttpResponse
from django.shortcuts import render
from .scripts.speech_to_speech import process_audio_files
from .scripts.decryption2 import fhss_reveal
from .scripts.speech3 import process_audio_files2
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError 
import numpy as np
import os
from django.conf import settings


def home_view(request, *args, **kwargs):
    return render(request, 'home.html', {});
def speech_view(request, *args, **kwargs):
    return render(request, 'speech.html')

def speech_view2(request, *args, **kwargs):
    return render(request, 'speech2.html')

def decryption_fhss(request, *args, **kwargs):
    return render(request, 'decryption_audio.html')

def output_speech(request):
    if request.method == 'POST':
        # Handle file uploads
        carrier_file = request.FILES['carrier']
        secret_file = request.FILES['secret']


        #script_dir = os.path.dirname(os.path.abspath(__file__))
        #hopping_pattern_path = os.path.join(script_dir, 'hopping_pattern.txt')
        # Save uploaded files
        fs = FileSystemStorage(location='media/uploads/')  # Set the location where original files will be stored
        carrier_filename = fs.save(carrier_file.name, carrier_file)
        secret_filename = fs.save(secret_file.name, secret_file)
        print(carrier_filename)
        print(secret_filename)
        # Process audio files
        #output_audio_path = process_audio_files2(carrier_filename, hopping_pattern_path)
        #output_audio_path2 = fhss_hide(carrier_filename, secret_filename)

        #return render(request, 'output_speech.html', {'output_audio_path': output_audio_path})

    return render(request, 'output_speech.html')

def output_speech2(request):
    if request.method == 'POST':
        # Handle file uploads
        carrier_file = request.FILES['carrier']
        secret_file = request.FILES['secret']



        # Save uploaded files
        fs = FileSystemStorage(location='first/media/upload/')  # Set the location where original files will be stored
        carrier_filename = fs.save(carrier_file.name, carrier_file)
        secret_filename = fs.save(secret_file.name, secret_file)
        print(carrier_filename)
        # Process audio files
        #output_audio_path = process_audio_files1(carrier_filename, secret_filename)
        output_audio_path = process_audio_files2(carrier_filename, secret_filename)
        print(output_audio_path)
        #output_audio_path2 = fhss_hide(carrier_filename, secret_filename)
        output_audio_path1 = os.path.relpath(output_audio_path, settings.MEDIA_ROOT)
        print(output_audio_path1)
       

        return render(request, 'output_speech2.html', {'output_audio_path': output_audio_path})
       #except MultiValueDictKeyError as e:
            # Handle the case where the keys are not found in request.FILES
        #return render(request, 'output_speech2.html', {'error_message': 'Missing key in request.FILES'})
     


    return render(request, 'output_speech2.html')


# Function to read a file in this case the hopping pattern :

def read_hopping_pattern(filename):
    # Read the hopping pattern from the file
    hopping_pattern = np.loadtxt(filename, dtype=np.int32)

    return hopping_pattern

def output_speech3(request):
    if request.method == 'POST':
        # Handle file uploads
        carrier_file = request.FILES['carrier']
        # Save uploaded files
        fs = FileSystemStorage(location='first/media/uploads/')  # Set the location where original files will be stored
        carrier_filename = fs.save(carrier_file.name, carrier_file)
        print(carrier_filename)
        # Process audio files
        scripts_dir = os.path.dirname(__file__)
        hopping_pattern_path = os.path.join(scripts_dir, 'hopping_pattern.txt')
        output_audio_path = fhss_reveal(carrier_filename, hopping_pattern_path)
        #output_audio_path2 = fhss_hide(carrier_filename, secret_filename)

        return render(request, 'output_speech3.html', {'output_audio_path': output_audio_path})

    return render(request, 'output_speech3.html')
