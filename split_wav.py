from pydub import AudioSegment
from pydub.utils import make_chunks
import sys
import os
import subprocess
import argparse

chunk_length_ms = 1000

def execute_process(cmd):
  status = subprocess.call(cmd, shell=True)
  if status != 0:
    if status < 0:
      print("Killed by signal", status)
    else:
      print("Command failed with return code - ", status)
  else:
    print('Execution of %s passed!\n' % cmd)

def run(path, wav_files_dir):
  if not os.path.isdir(path):
    os.mkdir(path)
  for subdir, dirs, files in os.walk(wav_files_dir):
    for file in files:
      #print os.path.join(subdir, file)
      filepath = subdir + os.sep + file

      if filepath.endswith(".wav"):
        src = filepath
        dst = path + os.sep + file
        cmd = 'cp {0} {1}'.format(src, dst)
      
        execute_process(cmd)
        
    for subdir, dirs, files in os.walk(path):
      for file in files:
        #print os.path.join(subdir, file)
        filepath = subdir + os.sep + file

        if filepath.endswith(".wav"):
          print(file)
          dir_name = file[0:-5]
          if dir_name[-2:] == 16:
            continue
          if not os.path.isdir(subdir + os.sep + dir_name):
            os.mkdir(subdir + os.sep + dir_name)
          file_index = file[-5]
          
          out_file = "{0}{1}_16k.wav".format(subdir + os.sep + dir_name, file_index)
          
          # convert to 16kHz
          cmd = "ffmpeg -y -i {0} -ar 16000 -acodec pcm_s16le {1}".format(filepath, out_file)
          execute_process(cmd)
          cmd = "rm -f {0}".format(filepath)
          execute_process(cmd)
  try:
    for subdir, dirs, files in os.walk(path):
      for file in files:
        #print os.path.join(subdir, file)
        filepath = subdir + os.sep + file

        if filepath.endswith(".wav"):
          dir_name = file[0:-9]

          myaudio = AudioSegment.from_file(filepath, "wav")
          chunks = make_chunks(myaudio, chunk_length_ms)
          for i, chunk in enumerate(chunks):
            chunk_name = path + os.sep + dir_name + os.sep + dir_name + "-chunk{0}.wav".format(i)
            chunk.export(chunk_name, format="wav")
        
          cmd = "rm -f {0}".format(filepath)
          execute_process(cmd)
  except FileNotFoundError:
    pass
    
if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument(
      '--wav_file_path', 
      type=str,
      default='./wav_files/train',
      help='Location of your wav file, don"t add sep!')
  parser.add_argument('--train_path', 
      type=str,
      default='./ttt',
      help='Location of your train data, don"t add sep!')
  
  args = parser.parse_args()
  run(path=args.train_path, wav_files_dir=args.wav_file_path)
