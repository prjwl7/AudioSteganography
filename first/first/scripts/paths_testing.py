import os
import numpy as np
from pathlib import Path
script_dir = os.path.dirname(os.path.abspath(__file__))
print(script_dir)
print(os.path.exists(script_dir))
common_parent_dir = os.path.abspath(os.path.join(script_dir, '..'))
true_folder = os.path.abspath(os.path.join(common_parent_dir, '..'))
#print(common_parent_dir)
output_folder_path = os.path.join(true_folder, 'media', 'uploads')

#print(output_folder_path)

host_audio_path = os.path.join(output_folder_path, 'carrier.wav')
secret_audio_path = os.path.join(output_folder_path, 'secret.wav')
print(common_parent_dir)
print(true_folder)
print(host_audio_path)
print(secret_audio_path)
print(output_folder_path)
hopping_pattern_path = os.path.join(script_dir, 'hopping_pattern.txt')
print(os.path.exists(hopping_pattern_path))
print(hopping_pattern_path)

def read_hopping_pattern(filename):
    # Read the hopping pattern from the file
    hopping_pattern = np.loadtxt(filename, dtype=np.int32)

    return hopping_pattern

hopping_pattern = read_hopping_pattern(os.path.join(script_dir, 'hopping_pattern.txt'))

#print(hopping_pattern)
file_name = "carrier.wav"

print(os.path.exists(os.path.join(output_folder_path, file_name)))

BASE_DIR = Path(__file__).resolve().parent.parent

print(BASE_DIR)
true_folder11 = os.path.abspath(os.path.join(BASE_DIR, '..'))
print("true folder", true_folder11)

MEDIA_ROOT = os.path.join(true_folder11,'first','media')
print(MEDIA_ROOT)

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'first' , 'static', 'css'),
]
print(STATICFILES_DIRS)