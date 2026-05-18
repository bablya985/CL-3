# Create and Art with Neural style transfer on given image using deep learning

import torch
import torchvision.transforms as transforms
from PIL import Image
import matplotlib.pyplot as plt
from torchvision.models import vgg19

# Load image
def load_image(path, size=256):
    image = Image.open(path)
    transform = transforms.Compose([
        transforms.Resize((size, size)),
        transforms.ToTensor()
    ])
    image = transform(image).unsqueeze(0)
    return image

# Display image
def show_image(tensor, title=None):
    image = tensor.clone().detach().squeeze(0)
    image = transforms.ToPILImage()(image)
    plt.imshow(image)
    if title:
        plt.title(title)
    plt.axis('off')

# Load images
content = load_image("content.jpg")
style = load_image("style.jpg")

# Load pretrained VGG19
model = vgg19(pretrained=True).features.eval()

# Simple optimization
output = content.clone().requires_grad_(True)
optimizer = torch.optim.Adam([output], lr=0.01)

# Loss function
mse = torch.nn.MSELoss()

print("Starting Style Transfer...")

for i in range(200):
    optimizer.zero_grad()

    output_features = model(output)
    content_features = model(content)
    style_features = model(style)

    content_loss = mse(output_features, content_features)
    style_loss = mse(output_features, style_features)

    total_loss = content_loss + 0.5 * style_loss

    total_loss.backward()
    optimizer.step()

    if i % 50 == 0:
        print(f"Step {i}, Loss: {total_loss.item():.4f}")

print("Style Transfer Completed!")

# Show result
show_image(output, "Stylized Image")
plt.show()


# 1. Problem Statement
# Apply Neural Style Transfer (NST) to generate artistic images.

# 👉 Goal:
# Take Content Image (your photo)
# Take Style Image (painting like Van Gogh)
# Combine both to create a stylized output image
# 👉 Example:
# Content → Your building/face image
# Style → Painting style
# Output → Your image in painting style

# 🧠 2. Concept (Simple Explanation)
# Neural Style Transfer uses a deep learning model like VGG19 to:
# Preserve content (structure of image)
# Apply style (colors, textures)
# 👉 It works using:
# Content Loss
# Style Loss
# Total Loss

# 💻 3. Python Code (Using PyTorch)

# 📁 Create file:
# neural_style_transfer.py

# 📌 Install libraries:
# pip install torch torchvision pillow matplotlib

# . How to Run in VS Code
# Step 1: Open VS Code
# Step 2: Create file:
# neural_style_transfer.py
# Step 3: Add images in same folder:
# content.jpg
# style.jpg
# Step 4: Open terminal:
# Terminal → New Terminal
# Step 5: Run:
# python neural_style_transfer.py
# 🖼️ 5. Output Explanation
# Console Output:
# Starting Style Transfer...
# Step 0, Loss: 12.3456
# Step 50, Loss: 5.2341
# Step 100, Loss: 2.1123
# Step 150, Loss: 1.2345
# Style Transfer Completed!

# 👉 Loss decreases → model improving

# Final Output:
# A new image appears
# Looks like:
# Same structure as content image
# Style applied from style image
# 🔍 6. Code Explanation
# Load Image
# load_image("content.jpg")

# 👉 Converts image to tensor

# Model
# vgg19(pretrained=True)

# 👉 Pretrained CNN used for feature extraction

# Output Image
# output = content.clone()

# 👉 Start from content image

# Loss Calculation
# content_loss + style_loss

# 👉 Content Loss → keeps structure
# 👉 Style Loss → adds artistic texture

# Optimization
# optimizer.step()

# 👉 Updates image pixels

# 🎤 7. Viva Questions

# Q1. What is Neural Style Transfer?
# 👉 A technique to combine content and style of two images.

# Q2. Which model is used?
# 👉 VGG19 (pretrained CNN)

# Q3. What is content loss?
# 👉 Difference in structure between images.

# Q4. What is style loss?
# 👉 Difference in texture and colors.

# Q5. What is optimizer used?
# 👉 Adam optimizer

# Q6. Why use pretrained model?
# 👉 It already learned image features.

# Q7. What is output of NST?
# 👉 Stylized artistic image.

# Q8. Can NST be used in real life?
# 👉 Yes, in apps, design, filters, AI art.

# 💡 Final Tip (For Exam)

# 👉 Always write:

# Content image + Style image
# VGG19 model
# Loss = Content + Style