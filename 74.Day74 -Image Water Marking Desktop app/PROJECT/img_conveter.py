from PIL import Image, ImageDraw, ImageFont

class IMAGE_CONVERTER():
    
    def __init__(self, file_input_txt, watermark_input_txt, rotation_input_txt, direction_selected):
        self.file_input_txt = file_input_txt.strip('"')
        self.watermark_input_txt = watermark_input_txt
        self.rotation_input_txt = float(rotation_input_txt)
        self.direction_selected = direction_selected
        
        base_image = Image.open(fr"{self.file_input_txt}").convert("RGBA")
        base_w, base_h = base_image.size

        text_layer = Image.new("RGBA", base_image.size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(text_layer)

        if self.direction_selected == 'Bottom-left':
            font = ImageFont.truetype("arial.ttf", 39)
            text = self.watermark_input_txt
            bbox = draw.textbbox((0, 0), text, font=font)
            x = 10
            y = base_h - (bbox[3] - bbox[1]) - 10
            draw.text((x, y), text, fill="gray", font=font)

        elif self.direction_selected == 'Bottom-right':
            font = ImageFont.truetype("arial.ttf", 39)
            text = self.watermark_input_txt
            bbox = draw.textbbox((0, 0), text, font=font)
            x = base_w - (bbox[2] - bbox[0]) - 10
            y = base_h - (bbox[3] - bbox[1]) - 10
            draw.text((x, y), text, fill="gray", font=font)

        elif self.direction_selected == 'Bottom':
            font = ImageFont.truetype("arial.ttf", 45)
            text = self.watermark_input_txt
            bbox = draw.textbbox((0, 0), text, font=font)
            x = (base_w - (bbox[2] - bbox[0])) // 2
            y = base_h - (bbox[3] - bbox[1]) - 10
            draw.text((x, y), text, fill="gray", font=font)

        elif self.direction_selected == 'Full page':
            font = ImageFont.truetype("arial.ttf", 25)
            text = self.watermark_input_txt
            x_gap = 300
            y_gap = 300
            for y in range(0, base_h, y_gap):
                for x in range(0, base_w, x_gap):
                    draw.text((x, y), text, fill="gray", font=font)
            
            # Apply rotation to the entire layer for Full page
            text_layer = text_layer.rotate(self.rotation_input_txt, expand=False)

        # Final composite
        self.final_image = Image.alpha_composite(base_image, text_layer)
        
    def show_img(self):
            self.final_image.convert("RGB").show()
