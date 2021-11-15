# coding=utf-8
'''
@ Summary: generate rt_ai_<model_name>_model.c + rt_ai_template.c/h
@ Update:  将会在稳定版本被移除，需要后续做修改

@ file:    gen_rt_ai_model_c.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    2021/2/26 11:13
'''
import re
import logging
from pathlib import Path


def update_network_name(info_file, new_example_file, default_name, model_name):
    """ replace old_name by new_name """
    # load file
    with info_file.open() as fr:
        lines = fr.read()

    if default_name != model_name:
        old_name_list = [default_name, default_name.upper()]
        new_name_list = [model_name, model_name.upper()]

        # replace file
        for i in range(len(old_name_list)):
            lines = re.sub(old_name_list[i], new_name_list[i], lines)

    # save new example file
    with new_example_file.open("w") as fw:
        fw.write(lines)

    return new_example_file


def load_rt_ai_example(project, rt_ai_example, platform, old_name, new_name):
    """ replace old_name by new_name; RTAK inference example and rt_ai_model file"""
    rt_ai_example = Path(rt_ai_example)

    # model.c
    file = rt_ai_example / "rt_ai_template_model.c"
    new_file_name = f"rt_ai_network_model.c"
    example_file = Path(project) / "applications" / new_file_name
    if example_file.exists():  example_file.unlink()

    update_network_name(file, example_file, old_name, new_name)
    
    logging.info("Load rt_ai examples successfully...")
    return True


if __name__ == "__main__":
    logging.getLogger().setLevel(logging.INFO)

    project = "tmp_cwd"
    tmp_project = Path("tmp_cwd") / "applications"
    if not tmp_project.exists():
        tmp_project.mkdir()

    rt_ai_example = "../../Documents"
    platform = "stm32"
    old_name = "mnist"
    new_name = "network"
    load_rt_ai_example(project, rt_ai_example, platform, old_name, new_name)
    print("u a right...")