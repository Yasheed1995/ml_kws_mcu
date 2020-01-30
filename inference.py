import sys
import os
import subprocess
import argparse

def execute_process(cmd):
  status = subprocess.call(cmd, shell=True)
  if status != 0:
    if status < 0:
      print("Killed by signal", status)
    else:
      print("Command failed with return code - ", status)
  else:
    print('Execution of %s passed!\n' % cmd)

def run(path):
  for subdir, dirs, files in os.walk(path):
    filepath = subdir + os.sep + file

    if filepath.endswith(".wav"):
      cmd = "python3 label_wav.py --wav filepath"


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--16k_path',
      type=str,
      default='./wav_files/test/out',
      help='Location of your test data, don"t add sep!')

  args = parser.parse_args()
  run(path=args.16k_path)

