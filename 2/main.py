from typing import Dict, List, Sequence

pronunciation_dict = {
    "ABACUS": ["AE", "B", "AH", "K", "AH", "S"],
    "BOOK": ["B", "UH", "K"],
    "THEIR": ["DH", "EH", "R"],
    "THERE": ["DH", "EH", "R"],
    "TOMATO1": ["T", "AH", "M", "AA", "T", "OW"],
    "TOMATO2": ["T", "AH", "M", "EY", "T", "OW"],
}

word_to_phonemes: Dict[str, List[str]] = {}

for word, phonemes in pronunciation_dict.items():
    word_to_phonemes[word] = phonemes

def compare_phoneme_sequences(seq1: List[str], seq2: List[str]) -> bool:
    return ",".join(seq1) == ",".join(seq2)

def find_word_combos_with_pronunciation(phonemes: Sequence[str]) -> Sequence[Sequence[str]]:
    combos = []
    phoneme_seq = list(phonemes)

    for word1, phonemes1 in word_to_phonemes.items():
        for word2, phonemes2 in word_to_phonemes.items():
            combined_phonemes = phonemes1 + phonemes2
            if compare_phoneme_sequences(phoneme_seq, combined_phonemes):
                combos.append([word1, word2])

    return combos

input_phonemes = ["DH", "EH", "R", "DH", "EH", "R"]
print(find_word_combos_with_pronunciation(input_phonemes))