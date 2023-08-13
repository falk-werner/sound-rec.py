#!/usr/bin/env python3

import sounddevice as sd
import soundfile as sf
import time
import argparse

CHANNELS=1
SAMPLE_RATE=44100


def list_devices():
    has_devices = False
    for device in sd.query_devices():
        if device["max_input_channels"] > 0:
            has_devices = True
            print(f"{device['index']:<2}: {device['name']}")

    # if has_devices:
    #    print(f"default: {sd.default.device[0]}")

    if not has_devices:
        print("no input device available")

def record(device, filename):
    sd.check_input_settings(device=device, channels=CHANNELS, samplerate=SAMPLE_RATE)
    with sf.SoundFile(filename, mode="w", channels=CHANNELS, samplerate=SAMPLE_RATE) as file:

        def write_callback(data, frames, time, status):
            file.write(data)
        
        try:
            with sd.InputStream(device=device, channels=CHANNELS, samplerate=SAMPLE_RATE, callback=write_callback):
                while True:
                    time.sleep(1)

        except KeyboardInterrupt:
            pass

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--filename", type=str, required=False, default="rec.wav")
    parser.add_argument("-d", "--device", type=int, required=False, default=None)
    parser.add_argument("-l", "--list", action='store_true')
    args = parser.parse_args()

    if args.list:
        list_devices()
        return

    record(args.device, args.filename)

if __name__ == "__main__":
    main()
