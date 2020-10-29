from keras.models import load_model
import cv2
import numpy as np
from keras.applications import VGG16

def classify_the_fashion(img):
    tags_to_names = {0 :"T-shirt/top", 1 :"Trouser", 2 :"Pullover" ,3:"Dress" ,4 :"Coat",5 :"Sandal",6 :"Shirt",7: "Sneaker",8 :"Bag",9 :"Ankle boot"}
    vgg16 = VGG16(weights='imagenet', include_top=False, input_shape = (48, 48, 3), classes = 10)
    model = load_model('fmnist_model.h5')
    img = cv2.resize(img,(48,48))
    im_features = vgg16.predict(np.expand_dims(img, axis=0))
    im_features = np.reshape(im_features,(1,512))
    x = model.predict(im_features)
    return tags_to_names[np.argmax(x)]

img = cv2.imread('testimg.jpg')
print(classify_the_fashion(img))