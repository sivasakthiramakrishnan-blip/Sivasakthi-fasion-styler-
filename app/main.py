from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from app.prompts import build_prompt
from app.model import generate_image
from app.feedback import save_feedback
from app.wardrobe import analyze_wardrobe_image, analyze_tryon_image
from app.trends import get_current_trends, get_occasion_trends
import os
import json

app = Flask(__name__)
CORS(app)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GENERATED_DIR = os.path.join(BASE_DIR, "generated")
HISTORY_FILE = os.path.join(BASE_DIR, "history.json")
os.makedirs(GENERATED_DIR, exist_ok=True)

def save_to_history(outfit_data):
    history = []
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            history = json.load(f)
    history.append(outfit_data)
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)

@app.route("/")
def home():
    return jsonify({"message": "StyleMind AI is running!"})

@app.route("/generate-outfit", methods=["POST"])
def generate_outfit():
    data = request.get_json()
    occasion = data.get("occasion", "casual")
    body_type = data.get("body_type", "rectangle")
    style = data.get("style", "minimalist")
    color = data.get("color", "neutral")
    budget = data.get("budget", "medium")
    gender = data.get("gender", "women")
    wardrobe = data.get("wardrobe", [])
    trends = get_current_trends()
    occasion_trends = get_occasion_trends(occasion)
    prompt = build_prompt(occasion, body_type, style, color, budget, gender, wardrobe, trends)
    filename = f"{occasion}_{style}.png"
    image_path = generate_image(prompt, filename, GENERATED_DIR)
    save_to_history({
        "occasion": occasion,
        "style": style,
        "color": color,
        "budget": budget,
        "prompt": prompt,
        "image": f"{occasion}_{style}",
        "wardrobe_items": wardrobe,
        "trends_applied": trends["seasonal_trends"][:2]
    })
    return jsonify({
        "message": "Outfit Generated!",
        "image_path": image_path,
        "prompt_used": prompt,
        "trends": trends,
        "occasion_trends": occasion_trends
    })

@app.route("/image/<outfit_name>")
def get_image(outfit_name):
    filepath = os.path.join(GENERATED_DIR, f"{outfit_name}.png")
    print(f"Looking for image at: {filepath}")
    print(f"File exists: {os.path.exists(filepath)}")
    if os.path.exists(filepath):
        return send_file(filepath, mimetype="image/png")
    return jsonify({"error": "Image not found"}), 404

@app.route("/analyze-wardrobe", methods=["POST"])
def analyze_wardrobe():
    data = request.get_json()
    image_data = data.get("image")
    if not image_data:
        return jsonify({"error": "No image provided"}), 400
    result = analyze_wardrobe_image(image_data)
    return jsonify(result)

@app.route("/tryon", methods=["POST"])
def tryon():
    data = request.get_json()
    image_data = data.get("image")
    style = data.get("style", "casual")
    if not image_data:
        return jsonify({"error": "No image provided"}), 400
    result = analyze_tryon_image(image_data, style)
    return jsonify(result)

@app.route("/trends", methods=["GET"])
def trends_route():
    occasion = request.args.get("occasion", "casual")
    current = get_current_trends()
    occasion_specific = get_occasion_trends(occasion)
    return jsonify({**current, **occasion_specific})

@app.route("/history", methods=["GET"])
def get_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            history = json.load(f)
        return jsonify({"history": history})
    return jsonify({"history": []})

@app.route("/feedback", methods=["POST"])
def feedback():
    data = request.get_json()
    save_feedback(data.get("outfit_name"), data.get("liked"))
    return jsonify({"message": "Feedback saved!"})