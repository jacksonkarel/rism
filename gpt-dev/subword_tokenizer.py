import sentencepiece as spm


def subword_tokenizer():
    # Train the subword tokenizer
    model_name = "subword_tokenizer"
    vocab_size = 16000
    spm.SentencePieceTrainer.train(input="../data/brittanica_clean.txt", model_prefix=model_name, vocab_size=vocab_size)

    # Load the trained model
    sp = spm.SentencePieceProcessor()
    sp.load(f"{model_name}.model")

    # Update the encoder and decoder
    encode = lambda s: sp.encode_as_ids(s)
    decode = lambda l: sp.decode_ids(l)

    return encode, decode, vocab_size
