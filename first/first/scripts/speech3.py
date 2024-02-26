import os
import numpy as np
import wave
import tempfile

script_dir = os.path.dirname(os.path.abspath(__file__))
common_parent_dir = os.path.abspath(os.path.join(script_dir, '..'))
true_folder = os.path.abspath(os.path.join(common_parent_dir, '..'))
# Update hopping_pattern_path to be in the same directory as your script
hopping_pattern_path = os.path.join(script_dir, 'hopping_pattern.txt')

def read_hopping_pattern(filename):
    # Read the hopping pattern from the file
    hopping_pattern = np.loadtxt(filename, dtype=np.int32)

    return hopping_pattern

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


def fhss_hide(secret_audio_path, host_audio_path):
    secret_signal, secret_framerate = read_audio(secret_audio_path)
    host_signal, host_framerate = read_audio(host_audio_path)

    hopping_pattern = read_hopping_pattern(os.path.join(script_dir, 'hopping_pattern.txt'))

    if len(secret_signal) > len(host_signal):
        raise ValueError("Secret audio is too long to be embedded in host audio.")

    combined_frames = []
    hop_idx = 0

    for i in range(0, len(host_signal), len(hopping_pattern)):
        frame = host_signal[i:i + len(hopping_pattern)]

        secret_frame = secret_signal[hop_idx:hop_idx + len(frame)]

        combined_frame = (frame + secret_frame) % 2**16  # Adjust for 16-bit audio
        combined_frames.extend(combined_frame)

        hop_idx = (hop_idx + 1) % len(hopping_pattern)

    return np.array(combined_frames, dtype=np.int16), host_framerate

def process_audio_files2(carrier_file_name, secret_file_name):
    folder_path = os.path.join(common_parent_dir, 'media', 'upload')
    carrier_audio_path = os.path.join(folder_path, carrier_file_name)
    secret_audio_path = os.path.join(folder_path, secret_file_name)
    
    output_folder_path = os.path.join(common_parent_dir, 'media', 'output')

    print(carrier_audio_path)
    print(secret_audio_path)

    print("Carrier file exists:", os.path.exists(carrier_audio_path))
    output_audio_filename = 'output.wav'
    output_audio_path = os.path.join(output_folder_path, output_audio_filename)
    print("Output audio path:", os.path.abspath(output_audio_path))

    combined_frames, host_framerate = fhss_hide(secret_audio_path, carrier_audio_path)
    
    # Write the combined audio directly to the output file
    write_audio(output_audio_path, combined_frames, host_framerate)

    return output_audio_path

