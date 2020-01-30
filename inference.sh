

out_path="./pb/dnn_chain_05.pb"
label_file="./trained_models/dnn_labels.txt"
test_path="wav_files/test"

filelist=$(ls ${test_path})
mkdir ${test_path}/out/

for filename in ${filelist}
do
  if [ -f ${test_path}/${filename} ]; 
  then
    #echo "The file ${test_path}/${filename} exist "
    ffmpeg -y -i ${test_path}/${filename} -ar 16000 -acodec pcm_s16le ${test_path}/out/${filename}
    
  fi
done
echo "========================================================================================"
echo "Test files are converted & copied to ${test_path}/out dir. Start labeling."

#python3 label_wav.py --wav $wav_file --graph $out_path --labels $label_file --how_many_labels 1
out_list=$(ls ${test_path}/out)
for filename in ${out_list}
do
  echo "labeling ${filename}..."
  python3 label_wav.py --wav ${test_path}/out/${filename} --graph $out_path --labels $label_file --how_many_labels 1
done
