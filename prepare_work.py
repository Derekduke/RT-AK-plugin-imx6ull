# coding=utf-8
'''
@ Summary: prepare
            1. create two dirs:
                <cwd>/Middlewares
                <cwd>/TFLite
            2. load 'SConscript' files
@ Update:  

@ file:    prepare_work.py
@ version: 1.0.0

@ Author:  dkeji627@gmail.com
@ Date:    2021/09/29 21:50

'''
import shutil
import logging
from pathlib import Path


def pre_sconscript(stm_out, sconscripts, imx6ull_dirs):
    stm_out, sconscripts = Path(stm_out), Path(sconscripts)

    # delete the dir first
    if stm_out.exists():  shutil.rmtree(stm_out)

    for i, dir in enumerate(imx6ull_dirs):
        # step 1: create two dirs ("Middlewares", "TFLite")
        new_dir = stm_out / dir / ("TF" if i == 0 else "App")
        print(new_dir)
        new_dir.mkdir(parents=True, exist_ok=True)

        # step 2: load sconscript file to <stm_out>
        source_scons = sconscripts / dir
        target_scons = stm_out / dir / "SConscript"
        if not source_scons.exists():
            raise FileNotFoundError(f"Not {source_scons} file found!!!")
        shutil.copy(source_scons, target_scons)

    logging.info(f"Create two dirs: {' '.join(imx6ull_dirs)} successfully...")


if __name__ == "__main__":
    logging.getLogger().setLevel(logging.INFO)

    stm_out = 'tmp_cwd'
    scons_path = "./Sconscripts"
    imx6ull_dirs = ["Middlewares", "TFLite"]

    # 2. prepare tmp output
    _ = pre_sconscript(stm_out, scons_path, imx6ull_dirs)
    print("u a right...")
