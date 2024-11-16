import spacy
from typing import NamedTuple


class Entity(NamedTuple):
    text: str
    label: str


class LegalNER:
    def __init__(self):
        self.nlp = spacy.load("en_legal_ner_trf")

    def get_entities(self, text: str) -> list[Entity]:
        doc = self.nlp(text)
        return [Entity(text=ent, label=ent.label_) for ent in doc.ents]


if __name__ == "__main__":
    # instantiati o singura data:)
    ner = LegalNER()
    print(
        ner.get_entities(
            "George Simion sued Diana Sosoaca for ilegally trespassing in the Romanian Parliament"
        )
    )
