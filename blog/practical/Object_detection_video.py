# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 09:06:26 2019

@author: TANVEER_MUSTAFA
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 18:28:45 2018

@author: TANVEER MUSTAFA
"""

import os
clear = lambda: os.system('cls')
clear()

import cv2
import numpy as np
import tensorflow as tf
import sys


from PIL import Image
import matplotlib.pyplot as plt
from os.path import isfile, join
import time

from utils import label_map_util
from utils import visualization_utils as vis_util


def choose_video(filename):

    start_time = time.time()

    image_array=[] 


    sys.path.append("..")



    MODEL_NAME = 'inference_graph'
    VIDEO_NAME = filename

    CWD_PATH = os.getcwd()


    PATH_TO_CKPT = os.path.join(CWD_PATH,MODEL_NAME,'frozen_inference_graph.pb')

    PATH_TO_LABELS = os.path.join(CWD_PATH,'training','mscoco_label_map.pbtxt')

    # Path to video
    PATH_TO_VIDEO = os.path.join(CWD_PATH,VIDEO_NAME)

    # Number of classes the object detector can identify
    NUM_CLASSES = 6




    try:
        if not os.path.exists('z1video_frames4'):
            os.makedirs('z1video_frames4')
    except OSError:
        print ('Error: Creating directory of data')

    try:
        if not os.path.exists('z1video_frames5'):
            os.makedirs('z1video_frames5')
    except OSError:
        print ('Error: Creating directory of data')


    label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
    categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
    category_index = label_map_util.create_category_index(categories)

    # Load the Tensorflow model into memory.
    detection_graph = tf.Graph()
    with detection_graph.as_default():
        od_graph_def = tf.GraphDef()
        with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
            serialized_graph = fid.read()
            od_graph_def.ParseFromString(serialized_graph)
            tf.import_graph_def(od_graph_def, name='')

        sess = tf.Session(graph=detection_graph)

    image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')

    detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')


    detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
    detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')


    num_detections = detection_graph.get_tensor_by_name('num_detections:0')


    video = cv2.VideoCapture(PATH_TO_VIDEO)


    currentFrame = 0
    i=0
    j=0
    count=1
    while(video.isOpened()):


        ret, frame = video.read()
        if ret:
                
            resize = cv2.resize(frame, (320, 240))
            resize1 = cv2.resize(frame, (620, 440))
            #resize1 = frame.resize( (620, 440))
            frame_expanded = np.expand_dims(frame, axis=0)
        
           
            (boxes, scores, classes, num) = sess.run(
                [detection_boxes, detection_scores, detection_classes, num_detections],
                feed_dict={image_tensor: frame_expanded})
        
          
            vis_util.visualize_boxes_and_labels_on_image_array(
                frame,
                np.squeeze(boxes),
                np.squeeze(classes).astype(np.int32),
                np.squeeze(scores),
                category_index,
                use_normalized_coordinates=True,
                line_thickness=4,
                min_score_thresh=0.40)
        
          
            name = './z1video_frames4/frame' + str(currentFrame) + '.jpg'
            name1 = './z1video_frames5/frame' + str(currentFrame) + '.jpg'
        
            #print('name',name)
            
            cv2.imwrite(name, frame)
            cv2.imwrite(name1, frame)
            cv2.imshow('Object detector', frame)
                # To stop duplicate images
            currentFrame += 1
            
            #****************************************************
            
            # Press 'q' to quit
            if cv2.waitKey(1) == ord('q'):
                break

        else:
            break
        
    #plot_graph()
        



    video.release()
    cv2.destroyAllWindows()

    print("--- %s seconds ---" % (time.time() - start_time))


