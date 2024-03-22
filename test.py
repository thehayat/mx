import pdfplumber
from PIL import Image
import os
import io

def extract_images_from_pdf(pdf_path, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages):
            images = page.images
            for j, img in enumerate(images):
                image_bytes = io.BytesIO(page.extract_image(img)["stream"].get("Data"))
                img_pil = Image.open(image_bytes)
                img_pil.save(os.path.join(output_dir, f"page_{i+1}_image_{j+1}.png"))

if __name__ == "__main__":
    pdf_path = "sample1.pdf"
    output_dir = "output_images"
    extract_images_from_pdf(pdf_path, output_dir)
