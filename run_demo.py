from models.common import DetectMultiBackend
from utils.torch_utils import select_device
from torchinfo import summary

device = select_device('cpu') 
model = DetectMultiBackend('yolov5s.pt', device=device)
summary(model.model, input_size=(1, 3, 640, 640), depth=4)
