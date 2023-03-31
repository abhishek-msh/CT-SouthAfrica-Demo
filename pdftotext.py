import fitz
# OCR the PDF using the default 'text' parameter
with fitz.open(r"C:\Users\abhis\Desktop\Celebal\Jay\EducationBot_SouthAfrica\Books\English\English1.pdf") as doc:
    #save the text to file
    with open(r'C:\Users\abhis\Desktop\Celebal\Jay\EducationBot_SouthAfrica\Books\English\English1.txt', 'w') as f:
        for page in doc:
            text = page.get_text()
            # text = text.replace('1', 'a')
            # text = text.replace('2', 'b')
            # text = text.replace('3', 'c')
            # text = text.replace('4', 'd')
            # text = text.replace('5', 'e')
            # text = text.replace('6', 'f')
            # text = text.replace('7', 'g')
            # text = text.replace('8', 'h')
            # text = text.replace('9', 'i')
            # text = text.replace('0', 'j')
            # text = text.replace('e-B', '5-B')
            f.write(text)
            # print(text)