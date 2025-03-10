# YOLOV5-Flask---Indian-Currency-Detection-
This Flask application, utilizing fully functional YOLOv5 weights, allows users to upload images of currency. The model processes these images, performing inferences and annotating the detected elements, subsequently displaying the final annotated image.


# File Structure

proj-folder/yolov5

     |...
     |...
     |--templates
           |-upload_form.html          
     |--static
           |--css
                |-styles.css
           |--js
               |-static.js
     |-req.txt
     |-best_final.pt
     |-app.py

# WEIGHTS INSTALLATION - IMP
Download the weights file from [this link](https://drive.google.com/file/d/1jpBarN5lrwQdcYlXvKu1x9_ps--44g7l/view?usp=drive_link). Please name it in the cnvention as stated above - ```best_final.pt```

# Process to run
1) Ensure that the file structure shown above is maintained strictly.
2) Make sure you are in the yolov5 folder. If not ```cd yolov5```
3) Run the command to download all the required installations ```pip install -r req.txt```
4) Ensure that the templates folder and static folder are having the correct files viz. ```upload_form.html``` and ```css/styles.css```; ```js/static.js``` respectively
5) After making sure that the file structure is thoroughly maintained - reconfirm that pwd is in yolov5. run > ```python app.py```
6) You will find the link to webpage. Click and run the app. 

Cheers!


## NOTE:
If the above file structure seems confusing and occasionaly not working, find the full structure to the project [here](https://drive.google.com/drive/folders/1Sp7u4OGHO46zFXu1m57_kTs5a_wjcwcC). Find the main content of this project in ```yolov5``` directory.
