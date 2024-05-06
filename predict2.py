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
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(150-200) ingratiates: Bread,Sausage,Mustard,Ketchup,Relish", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "APPLE" ==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(150-200 kcal) ingratiates:Apple", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "ARTICHOKE"==output:
                    cv2.putText(frame, results.names[int(class_id)].upper()+"Calories(60) ingratiates:Artichoke,Olive oil,Lemon,Garlic,Salt", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "ASPARAGUS"==output:
                cv2.putText(frame, results.names[int(class_id)].upper()+"Calories: 40 ingratiates: Asparagus,Olive oil,Salt,Pepper,Lemon", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)

            elif "BAGEL" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(240) ingredients: Bagel, Cream cheese, Smoked salmon, Red onion, Capers", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "BAKED-GOODS" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(Varies) ingredients: Flour, Sugar, Butter, Eggs, Baking powder", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "BANANA" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(105) ingredients: Banana, Peanut butter, Honey, Yogurt, Granola", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "BEER" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(150-200) ingredients: Barley, Hops, Yeast, Water, Malt", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "BELL-PEPPER" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(31) ingredients: Bell pepper, Onion, Garlic, Olive oil, Salt", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "BREAD" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(70-80) ingredients: Flour, Water, Yeast, Salt, Sugar", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "BROCCOLI" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(34) ingredients: Broccoli, Olive oil, Garlic, Salt, Pepper", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "BURRITO" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(326) ingredients: Tortilla, Rice, Beans, Cheese, Meat", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "CABBAGE" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(25) ingredients: Cabbage, Olive oil, Vinegar, Salt, Pepper", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "CAKE" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(250-300) ingredients: Flour, Sugar, Butter, Eggs, Milk", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "CANDY" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(Varies) ingredients: Sugar, Corn syrup, Flavorings, Food coloring, Gelatin", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "CANTALOUPE" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(53) ingredients: Cantaloupe", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "CARROT" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(25) ingredients: Carrot", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "COMMON-FIG" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(74) ingredients: Common fig", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "COOKIE" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(50-100) ingredients: Flour, Sugar, Butter, Eggs, Vanilla extract", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "DESSERT" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(Varies) ingredients: Sugar, Flour, Butter, Eggs, Chocolate", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "FRENCH-FRIES" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(300) ingredients: Potatoes, Oil, Salt", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "GRAPE" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(62) ingredients: Grape", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "GUACAMOLE" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(50) ingredients: Avocado, Onion, Tomato, Lime, Salt", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "ICE-CREAM" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(200-300) ingredients: Milk, Cream, Sugar, Eggs, Flavorings", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "MUFFIN" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(300) ingredients: Flour, Sugar, Butter, Eggs, Baking powder", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "ORANGE" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(62) ingredients: Orange", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "PANCAKE" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(220) ingredients: Flour, Milk, Eggs, Butter, Baking powder", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "PEAR" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(57) ingredients: Pear", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "POPCORN" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(31) ingredients: Popcorn, Butter, Salt", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "PRETZEL" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(300) ingredients: Flour, Water, Salt, Yeast, Sugar", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "STRAWBERRY" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(33) ingredients: Strawberry", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "TOMATO" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(18) ingredients: Tomato", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "WAFFLE" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(218) ingredients: Flour, Milk, Eggs, Butter, Baking powder", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "FOOD-DRINKS" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(Varies) ingredients: Various food and drink items", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "CHEESE" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(300-400) ingredients: Milk, Rennet, Salt, Bacteria culture", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "COCKTAIL" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(Varies) ingredients: Alcohol, Mixers, Ice", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "COFFEE" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(2) ingredients: Coffee beans, Water", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "COOKING-SPRAY" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(0) ingredients: Cooking spray", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "CRAB" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(85) ingredients: Crab", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "CROISSANT" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(230) ingredients: Flour, Butter, Sugar, Yeast, Milk", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "CUCUMBER" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(16) ingredients: Cucumber", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "DOUGHNUT" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(190) ingredients: Flour, Sugar, Eggs, Butter, Yeast", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "EGG" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(78) ingredients: Egg", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "FRUIT" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(Varies) ingredients: Various fruits", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "GRAPEFRUIT" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(52) ingredients: Grapefruit", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "HAMBURGER" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(250-300) ingredients: Beef patty, Bun, Lettuce, Tomato, Onion", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "HONEYCOMB" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(300) ingredients: Honeycomb", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "JUICE" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(Varies) ingredients: Fruit juice", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "LEMON" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(17) ingredients: Lemon", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "LOBSTER" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(89) ingredients: Lobster", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "MANGO" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(60) ingredients: Mango", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "MILK" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(42) ingredients: Milk", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "MUSHROOM" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(22) ingredients: Mushroom", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "OYSTER" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(68) ingredients: Oyster", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "PASTA" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(131) ingredients: Pasta, Water, Salt", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "PASTRY" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(300-400) ingredients: Flour, Butter, Sugar, Eggs, Water", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "PEACH" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(39) ingredients: Peach", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "PINEAPPLE" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(50) ingredients: Pineapple", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "PIZZA" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(298) ingredients: Dough, Tomato sauce, Cheese, Toppings", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "POMEGRANATE" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(83) ingredients: Pomegranate", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "POTATO" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(77) ingredients: Potato", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "PUMPKIN" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(26) ingredients: Pumpkin", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "RADISH" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(16) ingredients: Radish", (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "SALAD" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(Varies) ingredients: Lettuce, Tomato, Cucumber, Dressing", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "FOOD" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(Varies) ingredients: Various food items", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "SANDWICH" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(Varies) ingredients: Bread, Meat, Cheese, Lettuce, Tomato", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "SHRIMP" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(85) ingredients: Shrimp", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "SQUASH" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(28) ingredients: Squash", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "SQUID" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(79) ingredients: Squid", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "SUBMARINE-SANDWICH" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(Varies) ingredients: Bread, Meat, Cheese, Lettuce, Tomato", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "SUSHI" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(Varies) ingredients: Rice, Fish, Vegetables, Seaweed", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "TACO" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(Varies) ingredients: Tortilla, Meat, Cheese, Lettuce, Tomato", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "TART" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(Varies) ingredients: Pastry crust, Filling (fruit, custard, etc.)", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "TEA" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(2) ingredients: Tea leaves, Water", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "VEGETABLE" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(Varies) ingredients: Various vegetables", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "WATERMELON" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(30) ingredients: Watermelon", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "WINE" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(120-130) ingredients: Grapes, Yeast, Sugar", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "WINTER-MELON" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(14) ingredients: Winter melon", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "ZUCCHINI" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(17) ingredients: Zucchini", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "BANH_MI" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(330) ingredients: Baguette, Meat, Pickled vegetables, Cilantro, Chili", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "BANH_TRANG_TRON" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(Varies) ingredients: Rice paper, Tamarind sauce, Green mango, Papaya, Chili", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "BANH_XEO" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(190) ingredients: Rice flour, Coconut milk, Pork, Shrimp, Bean sprouts", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "BUN_BO_HUE" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(500) ingredients: Rice vermicelli, Beef, Pork blood, Lemongrass, Shrimp paste", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "BUN_DAU" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(380) ingredients: Rice vermicelli, Tofu, Fried pork, Herbs, Dipping sauce", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "COM_TAM" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(550) ingredients: Broken rice, Grilled pork, Egg, Pickled vegetables, Fish sauce", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "GOI_CUON" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(90) ingredients: Rice paper, Shrimp, Pork, Lettuce, Mint", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "PHO" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(350-500) ingredients: Rice noodles, Beef, Onions, Cilantro, Basil", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "HU_TIEU" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(400) ingredients: Egg noodles, Pork, Shrimp, Squid, Green onions", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)
            elif "XOI" == output:
                cv2.putText(frame, results.names[int(class_id)].upper() + "Calories(Varies) ingredients: Glutinous rice, Mung bean, Fried shallots, Coconut milk, Sugar", (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3, cv2.LINE_AA)

            
   
    cv2.imshow("food,",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    ret, frame = cap.read()

cap.release()
cv2.destroyAllWindows()
