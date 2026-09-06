from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


MODEL_NAME = "Helsinki-NLP/opus-mt-fr-en"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)


def translate_text(text):
    inputs = tokenizer(
        text,
        return_tensors="pt",
        padding=True,
        truncation=True
    )

    outputs = model.generate(
        **inputs,
        max_length=512
    )

    translated_text = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    )

    return translated_text