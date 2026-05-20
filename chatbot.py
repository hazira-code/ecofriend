import random

# ---------------------------------
# PLANT DATABASE
# ---------------------------------
plants = [
    {
        "plant_name": "Aloe Vera",
        "category": "Succulent",
        "sunlight": "Full Sun",
        "watering": "Low",
        "climate": "Hot",
        "soil_type": "Sandy Soil",
        "water_quantity": "200 ml/day",
        "uses": ["Medicinal", "Skin Care"]
    },

    {
        "plant_name": "Money Plant",
        "category": "Indoor Plant",
        "sunlight": "Low Light",
        "watering": "Medium",
        "climate": "Moderate",
        "soil_type": "Loamy Soil",
        "water_quantity": "300 ml/day",
        "uses": ["Air Purification", "Decoration"]
    },

    {
        "plant_name": "Rose",
        "category": "Flower Plant",
        "sunlight": "Full Sun",
        "watering": "High",
        "climate": "Moderate",
        "soil_type": "Clay Soil",
        "water_quantity": "500 ml/day",
        "uses": ["Decoration", "Fragrance"]
    },

    {
        "plant_name": "Tulsi",
        "category": "Medicinal Plant",
        "sunlight": "Partial Shade",
        "watering": "Medium",
        "climate": "Hot",
        "soil_type": "Loamy Soil",
        "water_quantity": "250 ml/day",
        "uses": ["Medicinal", "Religious"]
    }
]

# ---------------------------------
# RECOMMENDATION FUNCTION
# ---------------------------------
def recommend_plant(sunlight, watering, climate):

    for plant in plants:

        if (
            plant["sunlight"] == sunlight and
            plant["watering"] == watering and
            plant["climate"] == climate
        ):
            return plant

    return random.choice(plants)

# ---------------------------------
# AI CHATBOT
# ---------------------------------
def ask_ai(question):

    question = question.lower()

    if "water" in question:
        return "Water plants only when the top soil feels dry."

    elif "sunlight" in question:
        return "Plants like Aloe Vera and Rose need full sunlight."

    elif "fertilizer" in question:
        return "Organic compost is best."

    elif "yellow leaves" in question:
        return "Yellow leaves may indicate overwatering."

    else:
        return "I can help with plant care."

# ---------------------------------
# DISEASE DETECTION
# ---------------------------------
def predict_disease(image):

    diseases = [
        "Healthy Leaf",
        "Leaf Spot Disease",
        "Powdery Mildew",
        "Fungal Infection"
    ]

    return random.choice(diseases)

# ---------------------------------
# GROWTH PREDICTION
# ---------------------------------
def growth_prediction(days):

    growth_cm = days * 0.5

    return round(growth_cm, 2)