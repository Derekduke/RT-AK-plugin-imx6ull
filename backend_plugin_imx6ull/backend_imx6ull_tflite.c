/*
 * Copyright (c) 2006-2018, RT-Thread Development Team
 *
 * SPDX-License-Identifier: Apache-2.0
 *
 * Change Logs:
 * Date           Author       Notes
 * 2021-09-29     derekduke    the first version
 */

#include <backend_imx6ull_tflite.h>
#include <rt_ai_log.h>
#ifdef RT_AI_USE_imx6ull

#define imx6ull_load_model  person_detect_init
#define imx6ull_run_model   person_detect
#define imx6ull_get_model

extern uint32_t g_ai_done_flag;
static void kpu_done_callback(void *data)
{
    g_ai_done_flag = 1;
}

static int _imx6ull_tflite_init(rt_ai_t ai, rt_ai_buffer_t *buf)
{
    imx6ull_load_model(IMX6ULL_TFLITE(ai)->model);
    return 0;
}

static int _imx6ull_tflite_run(rt_ai_t ai, void (*callback)(void *arg), void *arg)
{
    imx6ull_run_model();
    return 0;
}

static int _imx6ull_get_ouput(rt_ai_t ai, rt_ai_uint32_t index)
{
    return 0;
}

static int _imx6ull_get_info(rt_ai_t ai, rt_ai_buffer_t *buf)
{
    return 0;
}

static int _imx6ull_tflite_config(rt_ai_t ai, int cmd, rt_ai_buffer_t *args)
{
    return 0;
}

int backend_imx6ull_tflite(void *imx6ull_tflite_s)
{
    RT_AI_T(imx6ull_tflite_s)->init = _imx6ull_tflite_init;
    RT_AI_T(imx6ull_tflite_s)->run = _imx6ull_tflite_run;
    RT_AI_T(imx6ull_tflite_s)->get_output = _imx6ull_get_ouput;
    RT_AI_T(imx6ull_tflite_s)->get_info = _imx6ull_get_info;
    RT_AI_T(imx6ull_tflite_s)->config = _imx6ull_tflite_config;
    RT_AI_T(imx6ull_tflite_s)->mem_flag = ALLOC_INPUT_BUFFER_FLAG;

    return 0;
}

#endif //RT_AI_USE_imx6ull
