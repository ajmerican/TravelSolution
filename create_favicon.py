from PIL import Image

# Open the source favicon image
img = Image.open('assets/images/favicon-source.jpg')

# Resize to 32x32 for favicon
favicon = img.resize((32, 32), Image.Resampling.LANCZOS)

# Save as ICO
favicon.save('favicon.ico', format='ICO')

print("Favicon created successfully!")

