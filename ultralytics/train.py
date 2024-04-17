from ultralytics import YOLO

# 加载模型
model = YOLO('yolov8n.yaml')  # 从yaml文件加载
model = YOLO('yolov8n.pt')  # 加载预训练模型 (推荐)
model = YOLO('yolov8n.yaml').load('yolov8n.pt')  # 从 YAML加载 然后再加载权重

# 指定训练参数开始训练
model.train(data='D:/python/ultralytics-main/break.yaml', epochs=100, imgsz=640)

