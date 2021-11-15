/*
 * Copyright (c) 2006-2018, RT-Thread Development Team
 *
 * SPDX-License-Identifier: Apache-2.0
 *
 * Change Logs:
 * Date           Author       Notes
 * 2021-09-29     derekduke    the first version
 */

#ifndef __BACKEND_imx6ull_tflite_H__
#define __BACKEND_imx6ull_tflite_H__
#include <rtthread.h>
#include "rt_ai.h"
#ifdef RT_AI_USE_imx6ull

struct imx6ull_tflite
{
    struct rt_ai parent;
    uint8_t                 *model;
};
typedef struct imx6ull_tflite *imx6ull_tflite_t;
#define IMX6ULL_TFLITE(h)   ((imx6ull_tflite_t)(h))

int backend_imx6ull_tflite(void *imx6ull_tflite_s);
#endif //RT_AI_USE_imx6ull
#endif

