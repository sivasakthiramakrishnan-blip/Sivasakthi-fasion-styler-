import datetime

def get_current_trends():
    """
    Trend Intelligence Agent
    Simulates real-time fashion trend scraping
    In production: connect to Pinterest API, Instagram API, Google Trends
    """
    month = datetime.datetime.now().month

    # Season detection
    if month in [3, 4, 5]:
        season = "Spring"
        seasonal_trends = ["floral prints", "pastel colors", "linen fabrics", "ballet flats", "sheer layers"]
    elif month in [6, 7, 8]:
        season = "Summer"
        seasonal_trends = ["tropical prints", "color blocking", "crochet", "platform sandals", "co-ord sets"]
    elif month in [9, 10, 11]:
        season = "Fall"
        seasonal_trends = ["plaid blazers", "knee high boots", "rich browns", "layering", "leather pieces"]
    else:
        season = "Winter"
        seasonal_trends = ["faux fur", "metallic textures", "statement coats", "knit sets", "velvet"]

    # Global trending aesthetics 2025-2026
    global_trends = [
        "quiet luxury",
        "clean girl aesthetic",
        "mob wife aesthetic",
        "coastal grandmother",
        "indie sleaze revival",
        "old money aesthetic",
        "Y2K fusion",
        "maximalist ethnic"
    ]

    # Trending in India right now
    india_trends = [
        "Indo-Western fusion",
        "pastel lehengas",
        "mirror work sarees",
        "structured kurta sets",
        "embroidered co-ords",
        "pearl jewelry",
        "block print fabrics",
        "pre-draped sarees"
    ]

    # Trending colors
    trending_colors = {
        "Spring": ["butter yellow", "lavender", "mint green", "peach", "ivory"],
        "Summer": ["coral", "turquoise", "hot pink", "lime green", "white"],
        "Fall": ["burnt orange", "chocolate brown", "olive green", "rust", "camel"],
        "Winter": ["midnight blue", "emerald", "burgundy", "silver", "black"]
    }

    # Trending pieces
    trending_pieces = {
        "Spring": ["flowy midi skirts", "linen blazers", "strappy sandals", "tote bags"],
        "Summer": ["co-ord sets", "maxi dresses", "platform shoes", "mini bags"],
        "Fall": ["oversized blazers", "wide leg trousers", "ankle boots", "scarves"],
        "Winter": ["long coats", "knit dresses", "knee high boots", "statement bags"]
    }

    return {
        "season": season,
        "seasonal_trends": seasonal_trends,
        "global_trends": global_trends[:4],
        "india_trends": india_trends[:4],
        "trending_colors": trending_colors[season],
        "trending_pieces": trending_pieces[season],
        "trend_score": "High demand season for fashion",
        "source": "StyleMind Trend Intelligence Engine"
    }


def get_occasion_trends(occasion: str) -> dict:
    """Get trends specific to an occasion"""
    occasion_trends = {
        "wedding": ["pastel lehengas", "floral sarees", "embroidered sherwanis", "pearl jewelry"],
        "festival": ["mirror work", "block prints", "ethnic jewelry", "kolhapuri footwear"],
        "party": ["sequin dresses", "metallic tops", "statement earrings", "strappy heels"],
        "formal": ["power suits", "structured blazers", "minimal jewelry", "pointed toe heels"],
        "casual": ["co-ord sets", "straight leg jeans", "oversized shirts", "white sneakers"],
        "college": ["baggy jeans", "crop tops", "sneakers", "backpacks"],
        "date": ["midi dresses", "soft colors", "delicate jewelry", "block heels"],
        "beach": ["swimwear coverups", "linen sets", "flatforms", "woven bags"],
        "sports": ["athleisure", "compression wear", "chunky sneakers", "caps"],
        "travel": ["comfortable co-ords", "slip on shoes", "crossbody bags", "layer friendly outfits"]
    }

    return {
        "occasion": occasion,
        "occasion_specific_trends": occasion_trends.get(occasion, ["classic styles", "timeless pieces"])
    }