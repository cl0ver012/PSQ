from typing import Tuple, Dict, List, Sequence


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

def find_word_combos_with_pronunciation(phonemes: Sequence[str], current_combo: Tuple[str] = ()) -> List[Tuple[str]]:
    if not phonemes:
        return [current_combo]

    combos = []
    for word, word_phonemes in word_to_phonemes.items():
        if phonemes[:len(word_phonemes)] == word_phonemes:
            remaining_phonemes = phonemes[len(word_phonemes):]
            new_combo = current_combo + (word,)
            combos.extend(find_word_combos_with_pronunciation(remaining_phonemes, new_combo))

    return combos

input_phonemes_1 = ["AE", "B", "AH", "K", "AH", "S"]
test_result_1 = find_word_combos_with_pronunciation(input_phonemes_1)
expected_result_1 = [('ABACUS',)]
assert test_result_1 == expected_result_1, f"Expected {expected_result_1}, but got {test_result_1}"

# Test Case 2
input_phonemes_2 = ["DH", "EH", "R", "B", "UH", "K"]
test_result_2 = find_word_combos_with_pronunciation(input_phonemes_2)
expected_result_2 = [('THEIR', 'BOOK'), ('THERE', 'BOOK')]
assert test_result_2 == expected_result_2, f"Expected {expected_result_2}, but got {test_result_2}"

# Test Case 3
input_phonemes_3 = ["T", "AH", "M", "AA", "T", "OW", "B", "UH", "K"]
test_result_3 = find_word_combos_with_pronunciation(input_phonemes_3)
expected_result_3 = [('TOMATO1', 'BOOK')]
assert test_result_3 == expected_result_3, f"Expected {expected_result_3}, but got {test_result_3}"

# Test Case 4
input_phonemes_4 = ["AE", "B", "AH", "K", "AH", "S", "DH", "EH", "R"]
test_result_4 = find_word_combos_with_pronunciation(input_phonemes_4)
expected_result_4 = [('ABACUS', 'THEIR'), ('ABACUS', 'THERE')]
assert test_result_4 == expected_result_4, f"Expected {expected_result_4}, but got {test_result_4}"

# Test Case 5
input_phonemes_5 = ["DH", "EH", "R","AE", "B", "AH", "K", "AH", "S", "DH", "EH", "R","T", "AH", "M", "AA", "T", "OW", "B", "UH", "K",  "DH", "EH", "R"]
test_result_5 = find_word_combos_with_pronunciation(input_phonemes_5)
expected_result_5 = [('THEIR', 'ABACUS', 'THEIR', 'TOMATO1', 'BOOK', 'THEIR'), ('THEIR', 'ABACUS', 'THEIR', 'TOMATO1', 'BOOK', 'THERE'), ('THEIR', 'ABACUS', 'THERE', 'TOMATO1', 'BOOK', 'THEIR'), ('THEIR', 'ABACUS', 'THERE', 'TOMATO1', 'BOOK', 'THERE'), ('THERE', 'ABACUS', 'THEIR', 'TOMATO1', 'BOOK', 'THEIR'), ('THERE', 'ABACUS', 'THEIR', 'TOMATO1', 'BOOK', 'THERE'), ('THERE', 'ABACUS', 'THERE', 'TOMATO1', 'BOOK', 'THEIR'), ('THERE', 'ABACUS', 'THERE', 'TOMATO1', 'BOOK', 'THERE')]
assert test_result_5 == expected_result_5, f"Expected {expected_result_5}, but got {test_result_5}"

input_phonemes_6 = ["DH", "EH", "R","AE", "B", "AH", "K", "AH", "S", "DH", "EH", "R","T", "AH", "M", "AA"]
test_result_6 = find_word_combos_with_pronunciation(input_phonemes_6)
expected_result_6 = []
assert test_result_6 == expected_result_6, f"Expected {expected_result_6}, but got {test_result_6}"
