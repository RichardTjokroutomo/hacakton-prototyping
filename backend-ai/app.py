from flask import Flask, request, jsonify
import os


from processImage import get_corners, crop_image
from ocr import extract_text

app = Flask(__name__)

# Configure the folder to save uploaded files
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Set the allowed extensions
ALLOWED_EXTENSIONS = {'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET'])
def call_server():
    return jsonify({'msg': 'hello!'}), 200

@app.route('/extract-handwritten-labels', methods=['POST'])
def upload_file():
    # 1) check if the request has the file part
    # ============================================================================
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # 2) check if the file is allowed
    # ============================================================================
    src_filepath = ""
    if file and allowed_file(file.filename):
        src_filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(src_filepath)
        #return jsonify({'message': 'File uploaded successfully', 'file_path': filepath}), 200
    else:
        return jsonify({'error': 'File extension not allowed'}), 400
    

    # 3) process img
    # ============================================================================
    src_filename = "modified-" + file.filename 
    cropped_src_filepath = os.path.join(app.config['UPLOAD_FOLDER'], src_filename)
    coord_arr = get_corners(src_filepath)
    crop_image(coord_arr[0][0], coord_arr[0][1], coord_arr[2][0], coord_arr[2][1], src_filepath, cropped_src_filepath)
    

    # 4) extract text
    # ============================================================================
    res_text = extract_text(cropped_src_filepath)


    # 5) delete image
    # ============================================================================
    os.remove(src_filepath)
    os.remove(cropped_src_filepath)

    # 6) return extracted text
    # ============================================================================
    return jsonify({'extracted_text': res_text}), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0")
