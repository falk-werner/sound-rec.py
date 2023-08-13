# sound-rec.py

Example how to record sound via python script

## Prerequisites

```bash
pip3 install -r requirements.txt
```

On Linux systems, `pulseaudio` is required.

```bash
sudo apt install libportaudio2
```

## Usage

```bash
./sound-rec.py
```

### Arguments

| Argument     | Description |
|--------------|-------------|
| -f FILENAME  | filename of the record, default: rec.wav |
| -d DEVICE_ID | id of the input device, default: None |
| -l           | list available devices an exit |
