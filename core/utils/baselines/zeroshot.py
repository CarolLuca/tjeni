from transformers import AutoTokenizer, AutoModel
from torch.nn import functional as F

tokenizer = AutoTokenizer.from_pretrained("deepset/sentence_bert")
model = AutoModel.from_pretrained("deepset/sentence_bert")

sentence = "Who are you voting for in 2020?"
labels = ["business", "art & culture", "politics"]

# run inputs through model and mean-pool over the sequence
# dimension to get sequence-level representations
inputs = tokenizer.batch_encode_plus(
    [sentence] + labels, return_tensors="pt", pad_to_max_length=True
)
input_ids = inputs["input_ids"]
attention_mask = inputs["attention_mask"]
output = model(input_ids, attention_mask=attention_mask)[0]
sentence_rep = output[:1].mean(dim=1)
label_reps = output[1:].mean(dim=1)

# now find the labels with the highest cosine similarities to
# the sentence
similarities = F.cosine_similarity(sentence_rep, label_reps)
closest = similarities.argsort(descending=True)
for ind in closest:
    print(f"label: {labels[ind]} \t similarity: {similarities[ind]}")
