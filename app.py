from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for treatments
treatments = {
    "Apple": {
        "Apple___Apple_scab": [
            "Use fungicides such as captan or mancozeb during the growing season.",
            "Prune infected leaves and branches to improve air circulation.",
            "Remove fallen leaves and debris to reduce overwintering spores."
        ],
        "Apple___Black_rot": [
            "Remove and destroy infected branches, leaves, and mummified fruits.",
            "Apply fungicides like captan or thiophanate-methyl during the growing season.",
            "Maintain tree health with proper fertilization and watering."
        ],
        "Apple___Cedar_apple_rust": [
            "Apply fungicides like myclobutanil or mancozeb early in the season.",
            "Remove nearby cedar or juniper trees, if possible, as they act as alternate hosts.",
            "Use resistant apple varieties."
        ],
        "Apple___healthy": [
            "No treatment required. Maintain good cultural practices."
        ]
    },
    "Blueberry": {
        "Blueberry___healthy": [
            "No treatment required. Ensure proper soil pH (4.5-5.5) and drainage."
        ]
    },
    "Cherry_(including_sour)": {
        "Cherry_(including_sour)___Powdery_mildew": [
            "Apply fungicides such as sulfur or myclobutanil.",
            "Prune infected leaves and branches.",
            "Avoid overhead watering to reduce humidity."
        ],
        "Cherry_(including_sour)___healthy": [
            "No treatment required. Practice good orchard management."
        ]
    },
    "Corn_(maize)": {
        "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot": [
            "Use resistant hybrids.",
            "Rotate crops to minimize fungal spore carryover.",
            "Apply fungicides like strobilurins or triazoles."
        ],
        "Corn_(maize)___Common_rust_": [
            "Plant rust-resistant hybrids.",
            "Apply fungicides such as azoxystrobin if the infection is severe."
        ],
        "Corn_(maize)___Northern_Leaf_Blight": [
            "Use resistant varieties.",
            "Rotate crops and remove crop debris.",
            "Apply fungicides like propiconazole or mancozeb."
        ],
        "Corn_(maize)___healthy": [
            "No treatment required. Maintain proper cultural practices."
        ]
    },
    "Grape": {
        "Grape___Black_rot": [
            "Apply fungicides like mancozeb or myclobutanil.",
            "Remove and destroy infected plant debris.",
            "Prune vines to improve air circulation."
        ],
        "Grape___Esca(Black_Measles)": [
            "Remove and destroy infected wood.",
            "Apply fungicides such as thiophanate-methyl.",
            "Avoid overwatering."
        ],
        "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": [
            "Apply fungicides like mancozeb or copper-based sprays.",
            "Prune and destroy infected leaves.",
            "Ensure proper vineyard sanitation."
        ],
        "Grape___healthy": [
            "No treatment required. Maintain good vineyard practices."
        ]
    },
    "Orange": {
        "Orange___Haunglongbing_(Citrus_greening)": [
            "Remove infected trees to prevent the spread.",
            "Control the Asian citrus psyllid vector with insecticides.",
            "Use resistant rootstocks where available."
        ]
    },
    "Peach": {
        "Peach___Bacterial_spot": [
            "Apply copper-based bactericides.",
            "Remove and destroy infected leaves and fruit.",
            "Use resistant varieties."
        ],
        "Peach___healthy": [
            "No treatment required. Maintain good orchard care."
        ]
    },
    "Pepper,_bell": {
        "Pepper,_bell___Bacterial_spot": [
            "Apply copper-based bactericides.",
            "Remove and destroy infected plants.",
            "Use disease-free seeds or resistant varieties."
        ],
        "Pepper,_bell___healthy": [
            "No treatment required. Practice proper plant care."
        ]
    },
    "Potato": {
        "Potato___Early_blight": [
            "Apply fungicides like chlorothalonil or mancozeb.",
            "Rotate crops and remove infected debris.",
            "Use certified disease-free seeds."
        ],
        "Potato___Late_blight": [
            "Use fungicides like metalaxyl or chlorothalonil.",
            "Destroy infected plants and debris.",
            "Plant resistant varieties and ensure good drainage."
        ],
        "Potato___healthy": [
            "No treatment required. Maintain good cultural practices."
        ]
    },
    "Raspberry": {
        "Raspberry___healthy": [
            "No treatment required. Provide proper care and pruning."
        ]
    },
    "Soybean": {
        "Soybean___healthy": [
            "No treatment required. Use good crop rotation and resistant varieties."
        ]
    },
    "Squash": {
        "Squash___Powdery_mildew": [
            "Apply fungicides such as sulfur or neem oil.",
            "Remove infected leaves.",
            "Ensure proper plant spacing for good air circulation."
        ]
    },
    "Strawberry": {
        "Strawberry___Leaf_scorch": [
            "Apply fungicides like captan or thiophanate-methyl.",
            "Remove and destroy infected leaves.",
            "Avoid overhead watering."
        ],
        "Strawberry___healthy": [
            "No treatment required. Maintain proper care and sanitation."
        ]
    },
    "Tomato": {
        "Tomato___Bacterial_spot": [
            "Apply copper-based bactericides.",
            "Remove and destroy infected leaves and fruits.",
            "Use disease-free seeds."
        ],
        "Tomato___Early_blight": [
            "Apply fungicides like chlorothalonil or mancozeb.",
            "Rotate crops and remove infected debris."
        ],
        "Tomato___Late_blight": [
            "Use fungicides such as metalaxyl or chlorothalonil.",
            "Destroy infected plants and avoid overcrowding."
        ],
        "Tomato___Leaf_Mold": [
            "Apply fungicides like chlorothalonil or mancozeb.",
            "Prune plants to improve air circulation."
        ],
        "Tomato___Septoria_leaf_spot": [
            "Apply fungicides such as chlorothalonil or copper-based sprays.",
            "Remove infected leaves and debris."
        ],
        "Tomato___Spider_mites Two-spotted_spider_mite": [
            "Use miticides or insecticidal soap.",
            "Increase humidity around plants to reduce mite activity."
        ],
        "Tomato___Target_Spot": [
            "Apply fungicides like chlorothalonil or azoxystrobin.",
            "Remove infected leaves."
        ],
        "Tomato___Tomato_Yellow_Leaf_Curl_Virus": [
            "Control whiteflies with insecticides.",
            "Remove infected plants.",
            "Use resistant varieties."
        ],
        "Tomato___Tomato_mosaic_virus": [
            "Remove infected plants.",
            "Disinfect tools and hands to prevent the spread.",
            "Use resistant seeds."
        ],
        "Tomato___healthy": [
            "No treatment required. Practice proper crop management."
        ]
    }
}
   
   
@app.route('/treatments', methods=['GET'])
def get_all_treatments():
    """Get all treatments."""
    return jsonify(treatments), 200

@app.route('/treatments/<string:category>', methods=['GET'])
def get_category_treatments(category):
    """Get treatments for a specific category."""
    if category not in treatments:
        return jsonify({'error': 'Category not found'}), 404
    return jsonify(treatments[category]), 200

@app.route('/treatments/<string:category>/<string:disease>', methods=['GET'])
def get_disease_treatment(category, disease):
    """Get treatment for a specific disease in a category."""
    category_data = treatments.get(category)
    if not category_data:
        return jsonify({'error': 'Category not found'}), 404

    disease_data = category_data.get(disease)
    if not disease_data:
        return jsonify({'error': 'Disease not found in the specified category'}), 404

    return jsonify({disease: disease_data}), 200

@app.route('/treatments/<string:category>/<string:disease>', methods=['POST'])
def add_disease_treatment(category, disease):
    """Add a treatment for a specific disease in a category."""
    data = request.get_json()
    if not data or not isinstance(data, list):
        return jsonify({'error': 'Invalid data format. Provide a list of treatments.'}), 400

    if category not in treatments:
        treatments[category] = {}

    treatments[category][disease] = data
    return jsonify({disease: data}), 201

@app.route('/treatments/<string:category>/<string:disease>', methods=['PUT'])
def update_disease_treatment(category, disease):
    """Update treatments for a specific disease in a category."""
    data = request.get_json()
    if not data or not isinstance(data, list):
        return jsonify({'error': 'Invalid data format. Provide a list of treatments.'}), 400

    if category not in treatments or disease not in treatments[category]:
        return jsonify({'error': 'Category or disease not found'}), 404

    treatments[category][disease] = data
    return jsonify({disease: data}), 200

@app.route('/treatments/<string:category>/<string:disease>', methods=['DELETE'])
def delete_disease_treatment(category, disease):
    """Delete treatments for a specific disease in a category."""
    if category not in treatments or disease not in treatments[category]:
        return jsonify({'error': 'Category or disease not found'}), 404

    removed_treatment = treatments[category].pop(disease)
    return jsonify({disease: removed_treatment}), 200

@app.route('/treatments/<string:category>', methods=['DELETE'])
def delete_category(category):
    """Delete an entire category."""
    if category not in treatments:
        return jsonify({'error': 'Category not found'}), 404

    removed_category = treatments.pop(category)
    return jsonify({category: removed_category}), 200

if __name__ == '__main__':
    app.run(port=5000)