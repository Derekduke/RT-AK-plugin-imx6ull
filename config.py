# coding=utf-8
'''
@ Summary: 
@ Update:  

@ file:    config.py.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    2021/2/25 11:08
'''


# support models
sup_models = {
    "keras": [".h5", ".hdf5", ".json", ".yml", ".yaml"],
    "tflite": [".tflite"],
    "lasagne": [".npz", ".npz"],
    "caffe": [".prototxt", ".caffemodel"],
    "convnetjs": [".json"],
    "onnx": [".onnx"],
}

# support cpus
sup_cpus = ["H7", "MP1", "WL", "M4", "M7", "M33" , "imx6ull"]

# x-cube-ai libraries and c-model dir
imx6ull_dirs = ["Middlewares", "TFLite"]

# sconscripts path
sconscript_path = "platforms/plugin_imx6ull/Sconscripts"

# support modes:{analyze, validate, generate}
sup_modes = {"001", "011", "101", "111"}

