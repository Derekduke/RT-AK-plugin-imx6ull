# coding=utf-8
'''
@ Summary: 
@ Update:  

@ file:    plugin_imx6ull_parser.py
@ version: 1.0.0

@ Author:  dkeji627@gmail.com
@ Date:    2021/9/29 21:50
'''
def platform_parameters(parser):
    """ imx6ull platform parameters """
    parser.add_argument("--ext_tools", type=str, default="", help="")
    parser.add_argument("--tflite", type=str, default="./platforms/plugin_imx6ull/TensorflowLiteMicro",
                        help="tensorflow lite micro dir")
    parser.add_argument("--rt_ai_example", type=str, default="./platforms/plugin_imx6ull/templates",
                        help="Model & platform informations registered to RT-AK Lib, eg:imx6ull, stm32, k210.")
    parser.add_argument("--imx6ull_out", type=str, default="",
                        help="TFLite output dir")
    parser.add_argument("--workspace", type=str, default="imx6ullai_ws",
                        help="indicates a working/temporary directory for the intermediate/temporary files")
    parser.add_argument("--val_data", type=str, default="",
                        help="indicates the custom test data set which must be used,"
                             "now is not supported")
    parser.add_argument("--compress", type=int, default=1,
                        help="indicates the expected global factor of compression which will be applied."
                             "1|4|8")
    parser.add_argument("--batches", type=int, default=10,
                        help="indicates how many random data sample is generated (default: 10)")
    parser.add_argument("--mode", type=str, default="001",
                        help="Describe analyze|validate|generate, 0 is False")
    parser.add_argument("--network", type=str, default="network",
                        help="The model name in '<tools>/Documents/<imx6ull> files'")
    parser.add_argument("--enable_rt_lib", type=str, default="RT_AI_USE_imx6ull",
                        help="Enabel RT-AK Lib using tflite")
    parser.add_argument("--clear", action="store_true", help="remove imx6ull middleware")
    return parser
