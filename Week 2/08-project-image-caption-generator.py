import streamlit as st
from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer
from PIL import Image
import torch

# Load model & tokenizer
model = VisionEncoderDecoderModel.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
feature_extractor = ViTImageProcessor.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
tokenizer = AutoTokenizer.from_pretrained("nlpconnect/vit-gpt2-image-captioning")

device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)

# Fungsi captioning
def generate_caption(image):
    if image.mode != "RGB":
        image = image.convert(mode="RGB")

    pixel_values = feature_extractor(images=image, return_tensors="pt").pixel_values
    pixel_values = pixel_values.to(device)

    output_ids = model.generate(pixel_values, max_length=16, num_beams=4)
    preds = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    return preds

# Streamlit UI
st.title("🖼️ Image Caption Generator")
st.write("Upload gambar dan dapatkan caption otomatisnya!")

uploaded_file = st.file_uploader("Upload Gambar", type=["jpg", "png", "jpeg"])

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption="Gambar yang diupload", use_column_width=True)

    with st.spinner("Generating caption..."):
        caption = generate_caption(img)
        st.success("Caption berhasil dibuat!")
        st.write(f"**Caption:** {caption}")