from youtube_transcript_api import YouTubeTranscriptApi
import string

ytt_api = YouTubeTranscriptApi()

with open("palavras_que_sei.txt", "r", encoding="UTF-8") as p:
   know = p.read().split()


# sinais do teclado + aspas curvas e reticências (\u2019 \u2018 \u201c \u201d \u2026)
SINAIS = string.punctuation + "\u2019\u2018\u201c\u201d\u2026"


def get_video_id(url):
    começo = url.split("/")[-1]
    fim = começo.split("?")[0]
    return fim


meu_id = get_video_id("https://youtu.be/Z-ucklAfzEk?si=rMWKLXqVAOiQ3nj8")
legenda = ytt_api.fetch(meu_id, languages=["en"])

counts = {}

for pedacinho in legenda:
  v1 = pedacinho.text
  v2 = v1.lower().split()
  for palavra in v2:
    nova_palavra = palavra.strip(SINAIS)
    if nova_palavra != "":
      if nova_palavra not in know:
        if nova_palavra not in counts:
            counts[nova_palavra] = 1
        else:
            counts[nova_palavra] += 1

best_word = ""
best_count = 0


for word, count in counts.items():
    if count > best_count:
        best_word = word
        best_count = count

print(best_word, best_count)