import cv2
import numpy as np

# Function to read bounding boxes from text file
def read_bboxes(file_path):
    with open(file_path, 'r') as f:
        boxes = [line.strip().split() for line in f.readlines()]
    # Convert string to float and the class_id to int
    boxes = [[int(box[0])] + [float(coord) for coord in box[1:]] for box in boxes]
    return boxes

# Function to draw bounding boxes on an image
def draw_boxes(image_path, boxes):
    # Read the image
    image = cv2.imread(image_path)
    h, w, _ = image.shape

    for box in boxes:
        class_id, x_center, y_center, width, height = box
        # Convert from relative to absolute coordinates
        x_center, y_center, width, height = x_center * w, y_center * h, width * w, height * h
        x_min, y_min = int(x_center - width / 2), int(y_center - height / 2)
        x_max, y_max = int(x_center + width / 2), int(y_center + height / 2)

        # Draw the bounding box
        cv2.rectangle(image, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)

    return image

def drawImageWithBoxes(image_path, boxes_file):
   
  # Read bounding boxes from text file
  boxes = read_bboxes(boxes_file)

  # Draw bounding boxes on the image
  image_with_boxes = draw_boxes(image_path, boxes)

  # Save the image with bounding boxes to a file
  output_image_path = './output_image.jpg'  # Specify your output image path here
  print('!pwd')
  cv2.imwrite(output_image_path, image_with_boxes)

  print(f"Image with bounding boxes saved to {output_image_path}")

# image_path = 'sheeps1.jpeg'
# boxes_file = 'sheeps1.txt'

# drawImageWithBoxes(image_path, boxes_file)