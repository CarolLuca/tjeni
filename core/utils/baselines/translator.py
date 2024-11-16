import torch
from transformers import pipeline


class NLLBTranslator:
    def __init__(self):
        self.pipe = pipeline("translation", model="facebook/nllb-200-distilled-600M")

    def translate(self, sentence, tgt_lang="fra_Latn", src_lang="eng_Latn"):
        return self.pipe(sentence, src_lang=src_lang, tgt_lang=tgt_lang)[0]


if __name__ == "__main__":
    tran = NLLBTranslator()
    print(tran.translate("UN Chief says there is no military solution in Syria", "fra_Latn"))
