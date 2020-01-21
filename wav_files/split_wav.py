from pydub import AudioSegment
from pydub.utils import make_chunks
import sys

myaudio = AudioSegment.from_file(sys.argv[1], "wav")
chunk_length_ms = 1000
chunks = make_chunks(myaudio, chunk_length_ms)

for i, chunk in enumerate(chunks):
  chunk_name = "chunk{0}.wav".format(i)
  print("exporting", chunk_name)
  chunk.export(chunk_name, format="wav")
