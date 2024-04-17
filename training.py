from ultralytics import YOLO
import yaml
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--data', type=str, default='datasets/break.yaml', help='dataset.yaml path')
parser.add_argument('--epochs', type=int, default=1, help='number of epochs')
parser.add_argument('--hyp', type=str, default='weights/hyp1.yaml', help='size of each image batch')
parser.add_argument('--model', type=str, default='weights/yolov8n.pt', help='pretrained weights or model.config path')
parser.add_argument('--batch-size', type=int, default=4, help='size of each image batch')
parser.add_argument('--img-size', type=int, default=320, help='size of each image dimension')
parser.add_argument('--device', type=str, default='0', help='cuda device, i.e. 0 or 0,1,2,3 or cpu')
parser.add_argument('--project', type=str, default='yolo', help='project name')
parser.add_argument('--name', type=str, default='pretrain', help='exp name')
parser.add_argument('--resume', nargs='?', const=True, default=False, help='resume most recent training')

args = parser.parse_args()

assert args.data, 'argument --data path is required'
assert args.model, 'argument --model path is required'

if __name__ == '__main__':
    # Initialize
    model = YOLO(args.model)
    hyperparams = yaml.safe_load(open(args.hyp))
    hyperparams['epochs'] = args.epochs
    hyperparams['batch'] = args.batch_size
    hyperparams['imgsz'] = args.img_size
    hyperparams['device'] = args.device
    hyperparams['project'] = args.project
    hyperparams['name'] = args.name
    hyperparams['resume'] = args.resume

    model.train(data= args.data, **hyperparams)
