# Program:
#   This shell script runs wav_split.py, train.py, test.py, freeze.py
  
# History:
# 2020/01/22 Logan   First Release

source_dir="./wav_files/training.wav"
data_dir="./wav_files/tttt"
train_dir="./trained_models"
wanted_words="rtone,birds,chain,rain,wind"
checkpoint="./trained_models/best/dnn_9692.ckpt-200"
out_path="./pb/dnn_chain_05.pb"

# use venv
source ../venv/bin/activate

python3 split_wav.py --wav_file_path $source_dir --train_path $data_dir

time python3 train.py --data_url= --data_dir=$data_dir --wanted_words=$wanted_words --model_architecture dnn --model_size_info 64 64 64  --train_dir=$train_dir --save_step_interval=25 --how_many_training_steps=300,100 --eval_step_interval 100

#python3 freeze.py --data_url= --data_dir=$data_dir --wanted_words=$wanted_words --checkpoint=$checkpoint --output_file=$out_path 

rm -rf $data_dir
