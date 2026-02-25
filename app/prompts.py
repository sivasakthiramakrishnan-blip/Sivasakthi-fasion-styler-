def build_prompt(occasion, body_type, style, color, budget, gender="women", wardrobe=None, trends=None):

    if wardrobe is None:
        wardrobe = []
    if trends is None:
        trends = {}

    wardrobe_context = ""
    if wardrobe:
        wardrobe_context = f"incorporating existing wardrobe items: {', '.join(wardrobe)}, "

    trend_context = ""
    if trends and trends.get("seasonal_trends"):
        trend_context = f"following trends: {', '.join(trends['seasonal_trends'][:2])}, "

    if style == "saree":
        prompt = (f"A beautiful Indian saree for {body_type} body type {gender}, "
                  f"occasion: {occasion}, color theme: {color}, budget: {budget}, "
                  f"{wardrobe_context}{trend_context}"
                  f"with matching blouse, jewelry, bangles, bindi, heels, "
                  f"highly detailed, photorealistic, Indian fashion photography")

    elif style == "lehenga":
        prompt = (f"A gorgeous Indian lehenga choli for {body_type} body type {gender}, "
                  f"occasion: {occasion}, color theme: {color}, budget: {budget}, "
                  f"{wardrobe_context}{trend_context}"
                  f"with matching dupatta, jewelry, heels, "
                  f"highly detailed, photorealistic, Indian bridal fashion photography")

    elif style == "kurta":
        prompt = (f"A stylish Indian kurta outfit for {body_type} body type {gender}, "
                  f"occasion: {occasion}, color theme: {color}, budget: {budget}, "
                  f"{wardrobe_context}{trend_context}"
                  f"with matching bottom wear, dupatta, footwear, "
                  f"highly detailed, photorealistic, Indian fashion photography")

    elif style == "indo_western":
        prompt = (f"A trendy Indo-Western fusion outfit for {body_type} body type {gender}, "
                  f"occasion: {occasion}, color theme: {color}, budget: {budget}, "
                  f"{wardrobe_context}{trend_context}"
                  f"with matching accessories, footwear, "
                  f"highly detailed, photorealistic, fusion fashion photography")

    else:
        prompt = (f"A {style} outfit for {body_type} body type {gender}, "
                  f"occasion: {occasion}, color theme: {color}, budget: {budget}, "
                  f"{wardrobe_context}{trend_context}"
                  f"including matching jewelry, shoes, handbag, "
                  f"highly detailed, photorealistic, fashion photography")

    return prompt