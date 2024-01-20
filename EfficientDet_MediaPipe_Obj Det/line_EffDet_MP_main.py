import argparse
import sys
import time
import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import utils
from tracker import Tracker
import math

def run(model: str, camera_id: int, width: int, height: int, num_threads: int,
        enable_edgetpu: bool) -> None:

    counter, fps = 0, 0
    count = 0
    start_time = time.time()
    cap = cv2.VideoCapture('people.mp4')
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    # Visualization parameters
    row_size = 20  # pixels
    left_margin = 24  # pixels
    text_color = (0, 0, 255)  # red

    font_size = 1
    font_thickness = 1
    fps_avg_frame_count = 10

    base_options = python.BaseOptions(model_asset_path=model)
    options = vision.ObjectDetectorOptions(base_options=base_options, score_threshold=0.3)
    detector = vision.ObjectDetector.create_from_options(options)

    # while cap.isOpened():
    #     success, image = cap.read()
    #     count += 1
    #     if count % 2 != 0:
    #         continue

    #     if not success:
    #         sys.exit('ERROR: Unable to read from webcam. Please verify your webcam settings.')

    while True:
        success, image = cap.read()
        count += 1
        if count % 2 != 0:
            continue
        if not success:
            break


        counter += 1
        image = cv2.flip(image, 1)
        image = cv2.resize(image, (600, 480))
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_image)
        detection_result = detector.detect(mp_image)
        image = utils.visualize(image, detection_result)

        # print(detection_result)
        # Calculate the FPS
        if counter % fps_avg_frame_count == 0:
            end_time = time.time()
            fps = fps_avg_frame_count / (end_time - start_time)
            start_time = time.time()
        # Show the FPS
        fps_text = 'FPS = {:.1f}'.format(fps)
        text_location = (left_margin, row_size)
        cv2.putText(image, fps_text, text_location, cv2.FONT_HERSHEY_PLAIN, font_size, text_color, font_thickness)
        if cv2.waitKey(1) == 27:
            break
        cv2.imshow('object_detector', image)

    cap.release()
    cv2.destroyAllWindows()

def main():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--model', help='Path of the object detection model.', required=False, default='efficientdet_lite0.tflite')
    parser.add_argument('--cameraId', help='Id of camera.', required=False, type=int, default=0)
    parser.add_argument('--frameWidth', help='Width of frame to capture from camera.', required=False, type=int, default=640)
    parser.add_argument('--frameHeight', help='Height of frame to capture from camera.', required=False, type=int, default=480)
    parser.add_argument('--numThreads', help='Number of CPU threads to run the model.', required=False, type=int, default=4)
    parser.add_argument('--enableEdgeTPU', help='Whether to run the model on EdgeTPU.', action='store_true', required=False, default=False)
    args = parser.parse_args()

    run(args.model, int(args.cameraId), args.frameWidth, args.frameHeight, int(args.numThreads), bool(args.enableEdgeTPU))

if __name__ == '__main__':
    main()
