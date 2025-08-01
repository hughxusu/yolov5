# Yolo V5 介绍

## 简介

Yolo V5 只有代码，没有相关论文，Yolo V5包含不同尺寸的模型。

| 版本        | 特点   | 准确率 | 速度 | 适用场景                               |
| ----------- | ------ | ------ | ---- | -------------------------------------- |
| **YOLOv5n** | 超轻量 | 最低   | 最快 | 超低资源设备（如嵌入式设备、移动设备） |
| **YOLOv5s** | 小型   | 较低   | 很快 | 实时检测，计算资源有限的设备           |
| **YOLOv5m** | 中型   | 中等   | 快   | 常见的检测任务，中等计算资源设备       |
| **YOLOv5l** | 大型   | 较高   | 较慢 | 高精度任务，高性能计算设备             |
| **YOLOv5x** | 超大型 | 最高   | 最慢 | 极高精度任务，适合高性能硬件           |

YOLOv5在COCO数据集上训练，因此其默认识别的80个类别与COCO数据集中的类别一致。

* person (人)
* bicycle (自行车)
* car (汽车)
* motorbike (摩托车)
* aeroplane (飞机)
* bus (公共汽车)
* train (火车)
* truck (卡车)
* boat (船)
* traffic light (交通信号灯)
* fire hydrant (消防栓)
* stop sign (停车标志)
* parking meter (停车计费器)
* bench (长椅)
* bird (鸟)
* cat (猫)
* dog (狗)
* horse (马)
* sheep (羊)
* cow (牛)
* elephant (大象)
* bear (熊)
* zebra (斑马)
* giraffe (长颈鹿)
* hat (帽子)
* backpack (背包)
* umbrella (雨伞)
* handbag (手提包)
* tie (领带)
* suitcase (行李箱)
* frisbee (飞盘)
* skis (滑雪板)
* snowboard (滑雪板)
* sports ball (运动球)
* kite (风筝)
* baseball bat (棒球棒)
* baseball glove (棒球手套)
* skateboard (滑板)
* surfboard (冲浪板)
* tennis racket (网球拍)
* bottle (瓶子)
* wine glass (酒杯)
* cup (杯子)
* fork (叉子)
* knife (刀子)
* spoon (勺子)
* bowl (碗)
* banana (香蕉)
* apple (苹果)
* sandwich (三明治)
* orange (橙子)
* broccoli (西兰花)
* carrot (胡萝卜)
* hot dog (热狗)
* pizza (披萨)
* donut (甜甜圈)
* cake (蛋糕)
* chair (椅子)
* couch (沙发)
* potted plant (盆栽)
* bed (床)
* dining table (餐桌)
* toilet (马桶)
* tv (电视)
* laptop (笔记本电脑)
* mouse (鼠标)
* remote (遥控器)
* keyboard (键盘)
* cell phone (手机)
* microwave (微波炉)
* oven (烤箱)
* toaster (烤面包机)
* sink (水槽)
* refrigerator (冰箱)
* book (书)
* clock (时钟)
* vase (花瓶)
* scissors (剪刀)
* teddy bear (泰迪熊)
* hair drier (吹风机)

### 项目目录结构

```shell
.
├── data # 数据相关配置文件
├── detect.py # 模型推理检测脚本
├── models # 模型相关配置文件和模型结构代码
├── requirements.txt # 依赖库版本文件
├── runs  # 输出结果文件夹
├── train.py # 训练脚本文件
├── tutorial.ipynb # 官方指南
├── utils # 相关工具代码，如绘图和loss值
├── val.py # 模型测试脚本
└── yolov5s.pt   # 下载模型文件

```

### 运行测试程序并下载模型

```shell
python detect.py --weights yolov5s.pt --conf 0.25 --source data/images
```

## 子目录文件夹

data子文件夹

```shell
.
├── hyps   # 超参数文件夹
│   ├── hyp.no-augmentation.yaml
│   ├── hyp.Objects365.yaml
│   ├── hyp.scratch-high.yaml
│   ├── hyp.scratch-low.yaml
│   ├── hyp.scratch-med.yaml
│   └── hyp.VOC.yaml
├── images  # 测试数据文件夹
│   ├── bus.jpg
│   └── zidane.jpg
├── Objects365.yaml
├── scripts  # 数据下载脚本
│   ├── download_weights.sh
│   ├── get_coco.sh
│   ├── get_coco128.sh
│   ├── get_imagenet.sh
│   ├── get_imagenet10.sh
│   ├── get_imagenet100.sh
│   └── get_imagenet1000.sh
├── Argoverse.yaml   # 数据配置文件 yaml文件
├── coco.yaml
├── coco128-seg.yaml
├── coco128.yaml
├── ImageNet.yaml
├── ImageNet10.yaml
├── ImageNet100.yaml
├── ImageNet1000.yaml
├── GlobalWheat2020.yaml
├── SKU-110K.yaml
├── VisDrone.yaml
├── VOC.yaml
└── xView.yaml
```

models子文件夹

```shell
.
├── hub  # 其他网络配置的yaml文件
├── common.py # 网络层文件
├── yolo.py  # 网络架构代码
├── yolov5l.yaml
├── yolov5m.yaml
├── yolov5n.yaml
├── yolov5s.yaml
└── yolov5x.yaml
```

utils文件夹

```shell
.
├── activations.py    
├── augmentations.py
├── autoanchor.py
├── autobatch.py
├── callbacks.py
├── dataloaders.py
├── downloads.py
├── general.py
├── google_app_engine
├── loggers
├── loss.py  # 损失函数计算
├── metrics.py
├── plots.py
├── torch_utils.py
└── triton.py
```

打印网络接口

需要安装包`pip install torchinfo`

```python
from models.common import DetectMultiBackend
from utils.torch_utils import select_device
from torchinfo import summary

device = select_device('cpu') 
model = DetectMultiBackend('yolov5s.pt', device=device)
summary(model.model, input_size=(1, 3, 640, 640), depth=4, verbose=2)

```

