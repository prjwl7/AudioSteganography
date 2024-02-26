import numpy as np
from scipy.io import wavfile
import os
import wave

def read_hopping_pattern(filename):
    # Read the hopping pattern from the file
    hopping_pattern = np.loadtxt(filename, dtype=np.int32)
    return hopping_pattern


script_dir = os.path.dirname(os.path.abspath(__file__))
common_parent_dir = os.path.abspath(os.path.join(script_dir, '..'))
true_folder = os.path.abspath(os.path.join(common_parent_dir, '..'))
# Update hopping_pattern_path to be in the same directory as script
hopping_pattern_path = os.path.join(script_dir, 'hopping_pattern.txt')


def read_audio(file_path):
    wave_file = wave.open(file_path, 'rb')
    frames = wave_file.readframes(-1)
    signal = np.frombuffer(frames, dtype=np.int16)
    return signal, wave_file.getframerate()

def write_audio(file_path, signal, framerate):
    with wave.open(file_path, 'wb') as wave_file:
        wave_file.setnchannels(1)
        wave_file.setsampwidth(2)
        wave_file.setframerate(framerate)
        wave_file.writeframes(signal.tobytes())


def fhss_reveal(carrier_filename, hopping_pattern_path):
    
    hopping_pattern = read_hopping_pattern(os.path.join(script_dir, 'hopping_pattern.txt'))
    folder_path = os.path.join(common_parent_dir, 'media', 'uploads')
    carrier_audio_path = os.path.join(folder_path, carrier_filename)
    combined_signal, combined_framerate = read_audio(carrier_audio_path)
    output_folder_path = os.path.join(common_parent_dir, 'media', 'output')

    print(carrier_audio_path)
   # print(secret_audio_path)

    print("Carrier file exists:", os.path.exists(carrier_audio_path))
    output_audio_filename = 'revealed.wav'
    output_audio_path = os.path.join(output_folder_path, output_audio_filename)
    secret_frames = []
    hop_idx = 0

    # Assuming your hopping pattern is read from a file or generated


# Ensure hopping pattern indices are within the range [0, 744)
    hopping_pattern = np.mod(hopping_pattern, 744)

    for i in range(0, len(combined_signal), len(hopping_pattern)):
        frame = combined_signal[i:i + len(hopping_pattern)]

        # Create a mapping based on the hopping pattern
        mapping = sorted(range(len(hopping_pattern)), key=lambda k: hopping_pattern[k])

        # Check hopping pattern and frame lengths
        if len(hopping_pattern) != len(frame):
            print("Mismatched hopping pattern and frame lengths.")
            break

        # Reverse the FHSS process by rearranging the frame based on the mapping
        secret_frame = np.zeros_like(frame)
        for j, hop_index in enumerate(mapping):
        # Ensure that the index stays within bounds
            index = (j + hop_index) % len(hopping_pattern)
            if index < len(frame):
                secret_frame[j] = frame[index]
            else:
                print(f"Index {index} is out of bounds for axis 0 with size {len(frame)}")

        secret_frames.extend(secret_frame)

        hop_idx = (hop_idx + 1) % len(hopping_pattern)



    secret_signal = np.array(secret_frames, dtype=np.int16)

    # Save the revealed secret audio directly
    write_audio(output_audio_path, secret_signal, combined_framerate)
    print("Length of secret_frames:", len(secret_frames))
    print("Length of combined_signal:", len(combined_signal))
    print("Hopping Pattern Length:", len(hopping_pattern))
    print("Frame Length:", len(frame))
    return output_audio_path
    




print(hopping_pattern_path)