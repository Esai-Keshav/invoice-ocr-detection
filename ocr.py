from paddleocr import PaddleOCR, draw_ocr

# Paddleocr supports Chinese, English, French, German, Korean and Japanese.
# You can set the parameter `lang` as `ch`, `en`, `french`, `german`, `korean`, `japan`
# to switch the language model in order.
ocr = PaddleOCR(
    use_angle_cls=True, lang="en"
)  # need to run only once to download and load model into memory
img_path = "img.png"
data = []

result = ocr.ocr(img_path, cls=True)
for text in result:
    for i in text:
        data.append(i[1])
# for idx in range(len(result)):
#    res = result[idx]
#    for line in res:
#        print(line)

for info, _ in data:
    print(info)
