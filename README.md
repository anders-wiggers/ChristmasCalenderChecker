![GitHub](https://img.shields.io/github/license/anders-wiggers/ccc)![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/anders-wiggers/ccc)![GitHub top language](https://img.shields.io/github/languages/top/anders-wiggers/ccc)![GitHub last commit](https://img.shields.io/github/last-commit/anders-wiggers/ccc)
# CCC - Christmas Calendar Checker 

"CCC" is a Deep Learning project that recognizes the different icons on the Danish Quick Christmas Calder game. The model is trained using transfer learning and annotated images gathered during the Christmas season. The Model is accessed through a python flash API which allows a user to query an image; to receive a result in JSON format. 

## Video Demo

A video demo of the project can be viewed [here](https://drive.google.com/file/d/1m6QYcnGxZRZDDEHGETQ4fnJFq98YCcfg/view?usp=sharing)

## Built With

* [Python](https://nextjs.org/) - Programmingh Langauge
* [Pytorch](https://expressjs.com/) - Machine Learning framework
* [Albumentation](https://github.com/albumentations-team/albumentations) - Libary for image augmentation
* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - Backend 


## Model

The models are trained using annotated images of calenders. To reduce the number of training images needed transfer learning and image augmentation was utilized. The base point of the model is the [resnet50](https://arxiv.org/abs/1512.03385) Object detection model provided by Pytorch.  
More information about the can be seen in the Jypyter notebook `qkt.ipynb` which was utilized for the training. 

The complete model is too large to store on GitHub, But a new model can be trained with the `qkt.ipynb` notebook or access can be granted upon request to the author. 

## Server

The server is hosted using a flask API. The API accepts POST request at the route `/predict`. The Post request must include an image with the `file` tag. A helper script can be found in `sender.py` which sends a file to the server. 
Once a request has been received the request is validated. The image is then fed through the model and the predicted results are returns in JSON format. 

# Getting Started

### Prerequisites

To initialize the server *out-of-the-box* the host system **MUST** be [CODA](https://developer.nvidia.com/cuda-zone) enabled.

### Installing

All the dependencies needed to run the server on a Ubnunuto Cuda enabled machine can be found in the `requirments.txt`. To Install all dependencies run
```bash
pip3 install -r requirements.txt
```

### Running
To initialize the server mount the `server` folder and run:
```bash
FLASK_ENV=development FLASK_APP=index.py flask run
```
The server is by default hosted on port 5000 on the system. This can be changed in the `index.py` script

## Authors

* **Anders Wiggers** - *Initial work* - [GitHub](https://github.com/anders-wiggers)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## A note on Docker Instances

A Point for future work of the project is enabling docker instances which would make the process of deployment tremendously easier. The current process of deploying the server on a system is time-consuming and dependency management is not trivial. This is a point that will be addressed in a future release. 