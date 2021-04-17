import torchvision
from torchvision.models.detection.faster_rcnn import FastRCNNPredictor
import os
import numpy as np
import torch
import torch.utils.data
from PIL import Image
import xml.etree.ElementTree as ET
import transforms as T
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import utils
import time;

from flask import Flask, jsonify, request, render_template
import io

app = Flask(__name__)
### Model

if __name__ == '__main__':
    app.run(host='0.0.0.0')

device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
m = torch.load('model/aug')
m.to(device)

m.eval()
def countPeople(img):
    #imgPath = 'testimg.jpg'
    custom_img = Image.open(io.BytesIO(img)).convert("RGB")
    custom_img = custom_img.resize((custom_img,))
    custom_img = T.ToTensor()(custom_img,None)
    custom_img = custom_img[0]
    with torch.no_grad():
        pred = m([custom_img.to(device)])


    person = 0
    boxes = pred[0]['boxes'].cpu().numpy()
    scores = pred[0]['scores'].cpu().numpy()
    for i in range(boxes.shape[0]):
        if scores[i] > 0.9:
            person = person + 1 
    return(person)


def countSave(img):
    custom_img = Image.open(io.BytesIO(img)).convert("RGB")
    
    height, weight = custom_img.size
    custom_img = custom_img.resize((height*3,weight*3))

    custom_img = T.ToTensor()(custom_img,None)
    custom_img = custom_img[0]
    with torch.no_grad():
        pred = m([custom_img.to(device)])

    img2 = Image.fromarray(custom_img.mul(255).permute(1, 2, 0).byte().numpy())
    plt.figure()
    fig, ax = plt.subplots(1, figsize=(12,9))
    ax.imshow(img2)
    boxes = pred[0]['boxes'].cpu().numpy()
    labels = pred[0]['labels'].cpu().numpy()
    scores = pred[0]['scores'].cpu().numpy()
    cmap = plt.get_cmap('tab20b')
    colors = [cmap(i) for i in np.linspace(0, 1, 20)]


    person = 0
    for i in range(boxes.shape[0]):
        if scores[i] > 0.9:
            person = person + 1 
            #print(i,boxes[i,:],labels[i],scores[i])
            x1 = boxes[i,0]
            y1 = boxes[i,1]
            box_w = boxes[i,2] - x1
            box_h = boxes[i,3] - y1
            color = colors[0]
            bbox = patches.Rectangle((x1, y1), box_w, box_h,
                        linewidth=2, edgecolor=color, facecolor='none')
            ax.add_patch(bbox)
            plt.text(x1, y1, s='Person', 
                         color='white', verticalalignment='top',
                         bbox={'color': color, 'pad': 0})
    plt.axis('off')
    dirPath = os.getcwd() + '/processed_img/' + str(time.time()) + '.png'
    plt.savefig(dirPath)
    plt.close()
    return(person)


@app.route('/')
def hello():
    return render_template("submit.html")

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
    # we will get the file from the request
        file = request.files['file']
        # convert that to bytes
        img_bytes = file.read()
        calResults = countSave(img_bytes)
        return jsonify({'cal': calResult})

      
