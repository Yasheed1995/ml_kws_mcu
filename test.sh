python3 test.py --data_url= --data_dir=wav_files/train --wanted_words=chain --checkpoint ./trained_models/best/dnn_10000.ckpt-400 

python3 freeze.py --data_url= --data_dir=wav_files/train --wanted_words=chain --checkpoint ./trained_models/best/dnn_10000.ckpt-400 --output_file pb/dnn_chain.pb

