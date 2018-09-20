from googletrans import Translator
from gtts import gTTS



with open('/Users/alex/coding/anki_deck_generator/vocab.txt', 'r') as fh:
    vocab = fh.readlines()
    fh.close()


translator = Translator()
fw = open('./vocabtranslations.txt','w')


for w in vocab:
    word = w.strip()
    # get the translation
    translation = translator.translate(word, dest='es', src='en').text
    fw.write(word+","+translation+"\n")
    tts_es = gTTS(translation, lang='es')
    tts_es.save(word+'.mp3')

fw.close()
