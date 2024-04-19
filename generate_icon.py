from PIL import Image, ImageDraw

def generate_colors(count):
    """
    Generates a list of distinct colors in HLS and converts to RGB.

    Args:
    - count (int): The number of colors to generate.

    Returns:
    - A list of color tuples.
    """
    colors = []
    for i in range(count):
        hue = i / count
        lightness = 0.5  # Adjust lightness if needed
        saturation = 1.0  # Full saturation for vivid colors
        rgb = colorsys.hls_to_rgb(hue, lightness, saturation)
        colors.append(tuple(int(x * 255) for x in rgb))
    return colors

def create_icon(color, file_path, size=(100, 100)):
    """
    Creates an icon with a specified color and transparent background.

    Args:
    - color (tuple): RGB color of the icon.
    - file_path (str): Path where the icon will be saved.
    - size (tuple): Size of the icon (width, height).
    """
    # Create a new image with transparency (RGBA)
    image = Image.new('RGBA', size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)

    # Define the user icon properties
    circle_center = (size[0] // 2, size[1] // 3)
    circle_radius = min(size) // 4
    body_top = (size[0] // 2, size[1] // 3 + circle_radius)
    body_bottom = (size[0] // 2, 2 * size[1] // 3)
    body_width = size[0] // 4

    # Draw the head (circle)
    draw.ellipse([(circle_center[0] - circle_radius, circle_center[1] - circle_radius),
                  (circle_center[0] + circle_radius, circle_center[1] + circle_radius)],
                 fill=color + (255,))  # Add full alpha for opacity

    # Draw the body (rectangle)
    draw.rectangle([(body_top[0] - body_width, body_top[1]),
                    (body_top[0] + body_width, body_bottom[1])],
                   fill=color + (255,))  # Add full alpha for opacity

    # Save the image
    image.save(file_path)

# Example usage
import colorsys

count = 20  # Specify the number of icons to generate
colors = generate_colors(count)

for i, color in enumerate(colors):
    create_icon(color, f'icons/user_icon_{i}.png')
