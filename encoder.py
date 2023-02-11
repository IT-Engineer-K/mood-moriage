import numpy as np
from transformers import BertTokenizer, BertModel
import torch

MODEL_NAME = 'model'

#トークナイザとモデルのロード
tokenizer = BertTokenizer.from_pretrained(MODEL_NAME)
bertModel = BertModel.from_pretrained(MODEL_NAME)


def toVec(text):
    input_batch = [text]

    encoded_data = tokenizer.batch_encode_plus(
    input_batch, pad_to_max_length=True, add_special_tokens=True)

    input_ids = torch.tensor(encoded_data["input_ids"])
    tokenizer.convert_ids_to_tokens(input_ids[0].tolist())

    outputs = bertModel(input_ids)
    last_hidden_states = outputs[0]
    sentencevec = last_hidden_states[:,0,:]
    return sentencevec.detach().numpy()

musics = [
'おとぼけダンス', '大混乱', 'Funny_Funny', '全力で逃げる時のBGM', 'トッカータとフーガ〜ギャグVer〜', 'シラけムードは少し気まずい',
'修羅場_怒り心頭', 'おばけとかぼちゃのスープ', 'いちごホイップ', 'eye-catch', '夏の霧', '昼下がり気分',
'Happy_birthday', 'はっぴいばあすでいつーゆー', 'yonhonnorecorder', 'happytime', '夏休みの探検', 'Recollections', 'パステルハウス'
]

from tensorflow.keras.models import load_model

model = load_model('model.h5')
def getMusic(sentence):
    print(sentence)
    predicted = model(np.array(toVec(sentence)))
    index = np.argmax(predicted[0])
    return musics[index]