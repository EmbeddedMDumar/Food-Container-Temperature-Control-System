import os
import cv2
from ultralytics import YOLO

#image_dir= "C:/Users/RETECH-01/Music/grocery_yolo/images"

#image_path = os.path.join(image_dir, 'input.jpg')

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
H, W, _ = frame.shape

model_path = r"C:\Users\Vijay\OneDrive\Desktop\Project\webcam\webcam\runs\detect\train3\yolov8s.pt"

# Load a model
model = YOLO(model_path)  # load a custom model

threshold = 0.5

while ret:
    results = model(frame)[0]

    for result in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = result
 
        if score > threshold:
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
            output=results.names[int(class_id)].upper()

            if "HOT-DOG" ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(150-200", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "APPLE" ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(150-200)", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "ARTICHOKE"==output:
                    cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(60) ", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)

            elif "ASPARAGUS"==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories: 40 ", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)

            elif "BAGEL" ==output: 
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(250-300)r", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)

            elif "BANANA" ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(105)", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "BEEF" ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories( 150-200)", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "BELL-PEPPER" ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(24)", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "BREAD - CALORIES" ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(70-80)", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "BROCCOLI" ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(55)", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "BURRITO " ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(300-400)", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "CABBAGE" ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(24)", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "CAKE " ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(24)", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "CANDY" ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(24)", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "CANTALOUPE" ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(50)", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "CARROT" ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(25)", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "COMMON" ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(50 )", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "COOKIE" ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(25)", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "DESSERT" ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(25)", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "FRENCH-FRIES" ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(312 )", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)    
            elif "GRAPE" ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(62 )", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "GUACAMOLE" ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(50 )", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "ICE-CREAM" ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(25)", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "MUFFIN" ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(25)", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "ORANGE" ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(62 )", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "PANCAKE" ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(90 )", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA) 
            elif "PEAR" ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(57 )", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA) 
            elif "POPCORN" ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(31 )", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA) 
            elif "PRETZEL" ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(108)", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "STRAWBERRY " ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(33 )", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
          
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
import os
import cv2
from ultralytics import YOLO

#image_dir= "C:/Users/RETECH-01/Music/grocery_yolo/images"

#image_path = os.path.join(image_dir, 'input.jpg')

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
H, W, _ = frame.shape

model_path = r"C:\Users\Vijay\OneDrive\Desktop\Project\webcam\webcam\runs\detect\train3\yolov8s.pt"

# Load a model
model = YOLO(model_path)  # load a custom model

threshold = 0.5

while ret:
    results = model(frame)[0]

    for result in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = result
 
        if score > threshold:
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
            output=results.names[int(class_id)].upper()

            if "HOT-DOG" ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(150-200", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "APPLE" ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(150-200)", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "ARTICHOKE"==output:
                    cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(60) ", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)

            elif "ASPARAGUS"==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories: 40 ", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)

            elif "BAGEL" ==output: 
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(250-300)r", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)

            elif "BANANA" ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(105)", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "BEEF" ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories( 150-200)", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "BELL-PEPPER" ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(24)", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "BREAD - CALORIES" ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(70-80)", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "BROCCOLI" ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(55)", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "BURRITO " ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(300-400)", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "CABBAGE" ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(24)", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "CAKE " ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(24)", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "CANDY" ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(24)", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "CANTALOUPE" ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(50)", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "CARROT" ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(25)", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "COMMON" ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(50 )", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "COOKIE" ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(25)", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "DESSERT" ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(25)", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "FRENCH-FRIES" ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(312 )", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)    
            elif "GRAPE" ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(62 )", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "GUACAMOLE" ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(50 )", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "ICE-CREAM" ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(25)", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "MUFFIN" ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(25)", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "ORANGE" ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(62 )", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "PANCAKE" ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(90 )", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA) 
            elif "PEAR" ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(57 )", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA) 
            elif "POPCORN" ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(31 )", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA) 
            elif "PRETZEL" ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(108)", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "STRAWBERRY " ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(33 )", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "TOMATO  " ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(22 )", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "WAFFLE  " ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(WAFFLE  )", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "CHEESE  " ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(33 )", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "COCKTAIL  " ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(33 )", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "COFFEE  " ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(2  )", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "COOKING-SPRAY " ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(33 )", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "CRAB  " ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(33 )", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "CROISSANT  " ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(231  )", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "CUCUMBER  " ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(16  )", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "DOUGHNUT  " ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(250  )", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "EGG  " ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(78  )", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "FRUIT  " ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(33 )", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "GRAPEFRUIT  " ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(52  )", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "HAMBURGER  " ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(250 )", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "HONEYCOMB  " ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(303)", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "JUICE  " ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(33 )", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "LEMON  " ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(17  )", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "LOBSTER  " ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(33 )", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "MANGO  " ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(60  )", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "MILK  " ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(33 )", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "MILK   " ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(103  )", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "MUSHROOM  " ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(15  )", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "OYSTER  " ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(33 )", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "PASTA  " ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(33 )", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "PASTRY  " ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(33 )", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "PEACH  " ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(59  )", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "PINEAPPLE  " ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(33 )", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "PIZZA  " ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(33 )", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "POMEGRANATE  " ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(83  )", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "POTATO  " ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(77  )", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "PUMPKIN  " ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(26  )", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "RADISH  " ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(16)", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "SALAD   " ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(16)", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "FOOD   " ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(16  )", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "SANDWICH   " ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(16)", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "SHRIMP   " ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(84)", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "c  " ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(18)", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "SQUID   " ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(92)", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "SUBMARINE-SANDWICH   " ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(16)", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "SUSHI   " ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(16  )", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "TACO   " ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(16)", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "TART   " ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(16)", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "TEA   " ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(0)", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "VEGETABLE   " ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(16)", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "WATERMELON   " ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(16)", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "WINE   " ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(16)", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "WINTER-MELON  " ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(13)", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "ZUCCHINI" ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(17 )", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "BANH_MI " ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(16  )", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "BANH_TRANG_TRON  " ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(16  )", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "BANH_XEO  " ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(16  )", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "BUN_BO_HUE  " ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(16  )", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "BUN_DAU" ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(16  )", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "COM_TAM" ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(16  )", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "GOI_CUON" ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(16  )", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "PHO " ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(16  )", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "HU_TIEU " ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(16  )", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "XOI   " ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(16  )", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "HOT-DOG   " ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(150-200  )", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "APPLE   " ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(95)", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "ARTICHOKE   " ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(60)", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "ASPARAGUS   " ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(20)", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "BAGEL   " ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(245)", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "BAKED-GOODS    " ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(16)", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "BANANA " ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(105)", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "BEER    " ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(150-200)", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "BELL-PEPPER   " ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(24)", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "BREAD" ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(70-80)", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "BROCCOLI" ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(55)", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "BURRITO    " ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(300-400)", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "CABBAGE" ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(22)", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "CAKE " ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(16)", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "CANDY  " ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(16)", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "CANTALOUPE  " ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(16)", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            elif "CAKE " ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(16)", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
          
   

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    ret, frame = cap.read()

cap.release()
cv2.destroyAllWindows()
 