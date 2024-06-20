from PIL import Image
from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer

# Load model and processor
model = VisionEncoderDecoderModel.from_pretrained('microsoft/trocr-large-stage1')
image_processor = ViTImageProcessor.from_pretrained('microsoft/trocr-large-stage1')
tokenizer = AutoTokenizer.from_pretrained('microsoft/trocr-large-stage1')

# Load the image
image_path = "scanned.png"  # Replace this with the path to your PNG image
image = Image.open(image_path)

# Ensure the image is in RGB format
if image.mode != 'RGB':
    image = image.convert('RGB')

# Process the image
pixel_values = image_processor(images=image, return_tensors="pt").pixel_values  # Batch size 1

# Generate predictions
outputs = model.generate(pixel_values)

# Debug: Print the outputs to understand their format
print(f"Outputs: {outputs}")

# Decode the generated tokens to text
predicted_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

# Print the predicted text
print(predicted_text)