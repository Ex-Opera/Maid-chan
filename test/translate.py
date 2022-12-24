import requests
import config

def translate(input_translate):
  url = f"https://translation.googleapis.com/language/translate/v2?key=config.translate_key"
  input_translate = {
    "q": input_translate,
    "target": "pt",
    "format": "text",
  }
  # output = requests.post(url, json=input_translate).json()
  # print(output['data']['translations'][0]['detectedSourceLanguage'])
  language = input_translate["q"][+2:]
  print(language)

translate("Hello, World!")
