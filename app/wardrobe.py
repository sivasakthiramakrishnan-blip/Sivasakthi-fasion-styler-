import os
import base64
import requests
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash-lite:generateContent?key={GEMINI_API_KEY}"

def call_gemini(prompt, image_bytes):
    image_b64 = base64.b64encode(image_bytes).decode("utf-8")
    payload = {
        "contents": [{
            "parts": [
                {"text": prompt},
                {
                    "inline_data": {
                        "mime_type": "image/jpeg",
                        "data": image_b64
                    }
                }
            ]
        }]
    }
    response = requests.post(GEMINI_URL, json=payload)
    result = response.json()
    if "candidates" in result:
        return result["candidates"][0]["content"]["parts"][0]["text"]
    elif "error" in result:
        return f"Error: {result['error']['message']}"
    else:
        return "Could not analyse image. Please try again."


def analyze_wardrobe_image(image_data: str) -> dict:
    try:
        image_bytes = base64.b64decode(
            image_data.split(",")[1] if "," in image_data else image_data
        )
        prompt = """
You are a professional fashion stylist AI agent. Analyze this clothing item image and provide:

1. ITEM DETECTED: What clothing item is this?
2. COLOR & PATTERN: Describe the color and pattern
3. STYLE CATEGORY: What style does it belong to?
4. OCCASIONS: List 3 best occasions to wear this
5. STYLING TIPS: Give 3 specific styling tips
6. PAIR WITH: Suggest 4 items to pair with this
7. AVOID: What to avoid pairing with this
8. SEASONAL: Which seasons is this best for?

Be specific, practical and fashionable in your suggestions.
        """
        analysis = call_gemini(prompt, image_bytes)
        return {
            "success": True,
            "analysis": analysis,
            "message": "Wardrobe item analyzed successfully!"
        }
    except Exception as e:
        return {
            "success": False,
            "analysis": f"Error analyzing image: {str(e)}",
            "message": "Analysis failed"
        }


def analyze_tryon_image(image_data: str, style: str) -> dict:
    try:
        image_bytes = base64.b64decode(
            image_data.split(",")[1] if "," in image_data else image_data
        )
        prompt = f"""
You are a professional AI fashion stylist. Analyze this person's photo and provide a complete virtual styling consultation for a {style} look.

Please provide:

1. BODY TYPE ANALYSIS: Identify their body type from the photo
2. CURRENT LOOK: Describe what they are currently wearing
3. RECOMMENDED OUTFIT: Describe a complete {style} outfit perfect for them including:
   - Top/dress recommendation with specific details
   - Bottom recommendation (if applicable)
   - Shoes recommendation
   - Accessories recommendation
4. COLOR PALETTE: Best colors that will suit them based on their skin tone
5. STYLING TIPS: 3 specific tips to enhance their look
6. WHAT TO AVOID: What styles/colors to avoid
7. CONFIDENCE TIP: One motivational styling tip

Be specific, encouraging, and fashionable. Make them feel confident!
        """
        analysis = call_gemini(prompt, image_bytes)
        return {
            "success": True,
            "analysis": analysis,
            "style": style,
            "message": "Virtual styling consultation complete!"
        }
    except Exception as e:
        return {
            "success": False,
            "analysis": f"Error: {str(e)}",
            "message": "Try-on analysis failed"
        }
