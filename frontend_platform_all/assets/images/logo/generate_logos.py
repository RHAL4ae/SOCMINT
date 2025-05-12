from PIL import Image, ImageDraw, ImageFont
import os

def create_logo(filename, text_color=(255, 255, 255)):
    # Create a new image with white background
    img = Image.new('RGBA', (128, 128), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Draw green bar
    draw.rectangle([0, 0, 128, 20], fill=(0, 128, 0, 255))

    # Load a font (you might need to adjust the path)
    try:
        font = ImageFont.truetype("assets/fonts/Dubai-Regular.ttf", 24)
    except:
        font = ImageFont.load_default()

    # Draw text
    text = "رحّال"
    if hasattr(draw, 'textsize'):
        text_width, text_height = draw.textsize(text, font=font)
    else:
        text_width, text_height = draw.textbbox((0, 0), text, font=font)[2:4]
    position = ((128 - text_width) // 2, (128 - text_height) // 2)
    draw.text(position, text, fill=text_color, font=font)

    # Save the image
    img.save(os.path.join("assets", "images", "logo", filename))
    print(f"Created: {filename}")

# Create all logo variants
create_logo('logo_primary.png')
create_logo('logo_white.png')
create_logo('logo_black.png', text_color=(0, 0, 0))
create_logo('favicon.png', text_color=(255, 255, 255))
