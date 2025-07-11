from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from PIL import Image
import time
import io

# === CONFIGURATION ===
url = "http://127.0.0.1:5500/index.html"
output_file = "website snapshots/screeny.png"
viewport_width = 2000
viewport_height = 2000
background_color = (255, 136, 229)  # optional if padding needed

# === SETUP SELENIUM ===
options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)

try:
    # Load page
    driver.get(url)
    time.sleep(2)

    # Set viewport size to 1000x1000
    driver.set_window_size(viewport_width, viewport_height)
    time.sleep(1)

    # Screenshot viewport (this captures visible area only)
    png_data = driver.get_screenshot_as_png()

finally:
    driver.quit()

# Open image
image = Image.open(io.BytesIO(png_data))

# Optional: If image is smaller or you want to ensure 1000x1000 with padding
if image.size != (viewport_width, viewport_height):
    padded = Image.new("RGB", (viewport_width, viewport_height), background_color)
    x = (viewport_width - image.width) // 2
    y = (viewport_height - image.height) // 2
    padded.paste(image, (x, y))
    image = padded

image.save(output_file)
print(f"Saved viewport screenshot: {output_file} size: {image.size}")