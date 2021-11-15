# coding=utf-8
'''
@ Summary: 
@ Update:  

@ file:    generate_rt_ai_model_h.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    2021/2/4 16:32
'''
import os
import sys
import logging
from pathlib import Path

path = os.path.dirname(__file__)
sys.path.append(os.path.join(path, '../../'))

from platforms.plugin_imx6ull import plugin_imx6ull_parser

def check_file(file):
    assert Path(file).exists(), logging.error(f"No such file {file} exists!")

def read_file(file):
    check_file(file)
    with open(file, "r") as f:
        lines = f.readlines()
    return lines

def get_model_info(template, model_name, default_name="network"):
    template_lines = read_file(template)
    return template_lines

def rt_ai_model_gen(stm_out, project, model_name, rt_ai_example):
    # modol informations

    template_file = Path(rt_ai_example)/"rt_ai_template_model.h"
    model_info = get_model_info(template_file, model_name)

    # project/applications/<model>.h
    pro_app_model_h = Path(project) / "applications" / f"rt_ai_{model_name}_model.h"
    #pro_app_model_h = Path(project) / "applications" / f"rt_ai_network_model.h"
    if pro_app_model_h.exists():  pro_app_model_h.unlink()

    with pro_app_model_h.open("w+") as fw:
        fw.write("".join(model_info))

    logging.info(f"Generate rt_ai_{model_name}_model.h successfully...")


if __name__ == "__main__":
    logging.getLogger().setLevel(logging.INFO)
    convert_info = ""
    tmp_project = Path("tmp_cwd")
    app_path = tmp_project / "applications"

    if not app_path.exists():
        app_path.mkdir(parents=True)

    report = "./convert_report.txt"
    _ = rt_ai_model_gen(report, tmp_project, "facelandmark")