#include <board.h>
#include <rt_ai.h>
#include <backend_imx6ull_tflite.h>
#include <rt_ai_network_model.h>

extern unsigned char __Models_person_detect_tflite[];

#define RT_IMX6ULL_AI_NETWORK { \
    .model  = __Models_person_detect_tflite,    \
}

static struct imx6ull_tflite rt_imx6ull_tflite_network_model = RT_IMX6ULL_AI_NETWORK;

static int rt_ai_network_model_init(){
    rt_ai_register(RT_AI_T(&rt_imx6ull_tflite_network_model),RT_AI_NETWORK_MODEL_NAME,0,backend_imx6ull_tflite,&rt_imx6ull_tflite_network_model);
    rt_kprintf("ai register success\n");
    return 0;
}
INIT_APP_EXPORT(rt_ai_network_model_init);