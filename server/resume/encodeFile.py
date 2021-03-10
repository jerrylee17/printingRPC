import base64
class encodeFile():
    def __init__(self):
        print("constructor")
        
    def encode(self, text):
        encoded_string = ""
        with open(text, "rb") as decoded_file:
            data = decoded_file.read()
            encoded_string = base64.b64encode(data)
        if encoded_string:
            with open("encodedResume.txt", "wb") as txt:
                txt.write(encoded_string)

def main():
    encoder = encodeFile()
    encoder.encode('./Resume.pdf')

main()



# import base64
# class encodeFile():
#     def encodeFile(self, text):
#         encoded_string = ""
#         with open(text, "rb") as decoded_file:
#             data = decoded_file.read()
#             encoded_string = base64.b64encode(data)
#         if encoded_string:
#             with open("encodedResume.txt", "wb") as txt:
#                 json.write(encoded_string)

# def main():
#     encodeFile('./Resume.pdf')

# main()