from ultralytics import YOLO
import sys

model = YOLO("yolov8n.pt")  # versi nano
model(sys.argv[1], save=True)
