from PIL import Image, ImageDraw, ImageFont
import os

def create_icon(size, text):
    img = Image.new('RGB', (size, size), color = '#4285F4')
    d = ImageDraw.Draw(img)
    # Simple visual: A white "G" or "GM"
    # Loading default font, might be small but it works for a placeholder
    try:
        # Try to find a sans-serif font, or use default
        font = ImageFont.truetype("arial.ttf", int(size/2))
    except:
        font = ImageFont.load_default()
    
    # Text centering logic (basic)
    text = "G"
    # bbox = d.textbbox((0,0), text, font=font)
    # text_w = bbox[2] - bbox[0]
    # text_h = bbox[3] - bbox[1]
    # d.text(((size-text_w)/2, (size-text_h)/2), text, fill=(255,255,255), font=font)
    
    # Just a simple rectangle if font fails or simplifies things
    d.rectangle([size*0.25, size*0.25, size*0.75, size*0.75], outline="white", width=max(1, int(size/10)))
    
    return img

sizes = [16, 48, 128]
base_dir = r"d:\00000ABOT\GEMINI去浮水印\gemini_extension"

for size in sizes:
    img = create_icon(size, "G")
    img.save(os.path.join(base_dir, f"icon{size}.png"))
    print(f"Created icon{size}.png")