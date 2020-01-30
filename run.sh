<<<<<<< HEAD
time python3 train.py --data_url= --data_dir=wav_files/train --wanted_words=chain --model_architecture dnn --model_size_info 128 128 128  --train_dir=./trained_models/ --save_step_interval=25 
=======

# Program:
#   This shell script runs wav_split.py, train.py, test.py, freeze.py
  
# History:
# 2020/01/22 Logan   First Release

source_dir="./wav_files/wav_files/train"
data_dir="./wav_files/ttt"
train_dir="./trained_models"
wanted_words="chain"
checkpoint="./trained_models/best/dnn_10000.ckpt-400"
out_path="./pb/dnn_chain_02.pb"

# use venv
source ../venv/bin/activate

python3 ./split_wav.py --wav_file_path $source_dir --train_path $data_dir

time python3 train.py --data_url= --data_dir=$data_dir --wanted_words=$wanted_words --model_architecture dnn --model_size_info 128 128 128  --train_dir=$train_dir --save_step_interval=25 --how_many_training_steps=300,100 --eval_step_interval 100

python3 freeze.py --data_url= --data_dir=$data_dir --wanted_words=chain --checkpoint=$checkpoint --output_file=$out_path 

>>>>>>> b3ae1c5... delete venv
