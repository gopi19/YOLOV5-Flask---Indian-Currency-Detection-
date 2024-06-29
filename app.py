

import os
from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory

app = Flask(__name__)

# Upload folder
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def get_latest_subfolder(folder_path):
    # List all subfolders in the specified folder
    subfolders = [f.path for f in os.scandir(folder_path) if f.is_dir()]

    # Get the latest subfolder based on creation time
    latest_subfolder = max(subfolders, key=os.path.getctime, default=None)
    x = latest_subfolder.split("/")
    x = x[-1]

    return x

# Route to render upload form
@app.route('/')
def upload_form():
    return render_template('upload_form.html')

# Route to handle file upload and execute runner.py
@app.route('/upload', methods=['POST'])
def upload_file():
    # Clear the upload directory before saving new files
    clear_upload_folder()

    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    
    file = request.files['file']
    
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    
    if file:
        # Save the uploaded file to the upload folder
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        
        # Assuming runner.py is in the same directory
        runner_script = os.path.join(os.path.dirname(__file__), 'runner.py')
        
        # Execute runner.py script with the uploaded image file path as argument
        os.system(f"python detect.py --weights best_final.pt --source {file_path}")
        
        # Redirect to display image route with file_path as parameter
        return redirect(url_for('display_image', filename=file.filename))
    
    return 'Something went wrong'

# Function to clear the upload folder
def clear_upload_folder():
    folder = "runs/detect"
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            # elif os.path.isdir(file_path): shutil.rmtree(file_path)
        except Exception as e:
            print(f"Failed to delete {file_path}. Reason: {e}")

# Route to display the uploaded image
@app.route('/display/<filename>')
def display_image(filename):
    # Construct the path to the processed image
    #/Users/prasanthimaru/Documents/test1/yolov5/runs/detect
    #processed_image_path = os.path.join("/Users","prasanthimaru","Documents","test1","yolov5","runs","detect",get_latest_subfolder('runs/detect'))
    #C:\Users\dokka\OneDrive\Desktop\final_proj\yolov5\runs
    #yolov5\runs\detect
    processed_image_path = os.path.join("C:",os.sep,"Users","dokka","OneDrive","Desktop","final_proj","yolov5","runs",get_latest_subfolder("runs/detect"))
    print("process = ",processed_image_path)
    # Check if the file exists
    if os.path.exists(processed_image_path):
        #return render_template('img.html', image=processed_image_path)
        return send_from_directory(processed_image_path,filename)
    else:
        return f'Processed image not found at {processed_image_path}'

if __name__ == '__main__':
    app.run(debug=True)
    
    


