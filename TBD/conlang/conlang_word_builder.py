__all__ = [
    'fantasy_affix',
    'fantasy_mutation',
    'fantasy_molting',
    'fantasy_pronounce',
    'conlang_unique',
]
import random
import re
from difflib import SequenceMatcher
import os
import json
from difflib import SequenceMatcher
import random

# Path to the lexicon file (local to this world folder)
LEXICON_PATH = os.path.join(os.path.dirname(__file__), '..', 'conlang_lexicon.json')

# Load or initialize lexicon
if os.path.exists(LEXICON_PATH):
    with open(LEXICON_PATH, 'r', encoding='utf-8') as f:
        lexicon = json.load(f)
else:
    lexicon = {}

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def check_lexicon(new_root):
    for word, entry in lexicon.items():
        if similar(new_root, entry['root']) > 0.7:
            return word, entry
    return None, None

def add_to_lexicon(concept, root, final_word):
    lexicon[final_word] = {'concept': concept, 'root': root}
    with open(LEXICON_PATH, 'w', encoding='utf-8') as f:
        json.dump(lexicon, f, ensure_ascii=False, indent=2)

def conlang_process(concept, mongolian_root, kiranti_affix, fula_mutation_func, molting_func):
    # List of alternative Mongolian roots (expand as needed)
    mongolian_alternatives = {
        'Aurora': ['gerelt', 'goyor', 'tsakhilgaan', 'gerelt tsagaan', 'tsagaan tuyaa', 'tserenkhar'],
        'Tundra': ['tsaraitai', 'tsasan tal', 'huiten tal', 'huiten gazar', 'tsasnut', 'talbar'],
    }
    attempts = 0
    max_attempts = 10
    root = mongolian_root
    while attempts < max_attempts:
        word, entry = check_lexicon(root)
        if word:
            # Try alternative root
            alt_list = mongolian_alternatives.get(concept, [])
            if alt_list:
                root = random.choice([r for r in alt_list if r != root])
                attempts += 1
                continue
            print(f"Similar root found: {word} for concept '{entry['concept']}'. Consider using a synonym, metaphor, or symbolic root.")
            return None
        # Step 1: Mongolian root
        # Step 2: Add Kiranti affix
        combined = root + kiranti_affix
        # Step 3: Fula mutation
        mutated = fula_mutation_func(combined)
        # Step 4: Molting/enunciation
        final_word = molting_func(mutated)
        # Root validation: ensure final_word does not start with root or first 2-3 letters
        root_start = root[:3]
        if final_word.startswith(root) or final_word.startswith(root_start):
            # Try alternative root
            alt_list = mongolian_alternatives.get(concept, [])
            if alt_list:
                root = random.choice([r for r in alt_list if r != root])
                attempts += 1
                continue
            print(f"Final word '{final_word}' starts with root '{root}' or '{root_start}'. Please use a new root word.")
            return None
        # Add to lexicon
        add_to_lexicon(concept, root, final_word)
        print(f"Conlang word for '{concept}': {final_word}")
        return final_word
    print(f"Failed to generate unique conlang word for '{concept}' after {max_attempts} attempts.")
    return None

def fula_mutation_func(word):
    # Refined Fula mutation logic
    # Example: swap 'r' with 'd', 's' with 'z', 'f' with 'h', soften consonant clusters, add vowel harmony
    word = word.replace('r', 'd').replace('s', 'z').replace('f', 'h')
    # Soften clusters: replace 'tr' with 'dr', 'kr' with 'gr', etc.
    word = word.replace('tr', 'dr').replace('kr', 'gr').replace('pl', 'bl')
    # Vowel harmony: if word ends with a consonant, add 'a' or 'u'
    if word and word[-1] not in 'aeiou':
        word += random.choice(['a', 'u'])
    return word

def molting_func(word):
    # Indonesian-inspired molting: drop unstressed syllables, merge repeated vowels, favor simple syllables
    import re
    vowels = 'aeiou'
    # Split into syllables (C*V+)
    syllables = re.findall(r'[bcdfghjklmnpqrstvwxyz]*[aeiou]+', word)
    if not syllables:
        return word
    # Always preserve the first syllable (or first two if short)
    preserved = syllables[:2] if len(syllables) > 2 else syllables[:1]
    # Indonesian molting: drop unstressed (short, non-initial) syllables
    reduced = []
    for i, s in enumerate(syllables[len(preserved):]):
        # Merge repeated vowels
        s = re.sub(r'([aeiou])\1+', r'\1', s)
        # Drop syllable if it's short (unstressed) and not initial
        if len(s) <= 2 and i > 0:
            continue
        # Favor simple syllables (CV)
        s = re.sub(r'([bcdfghjklmnpqrstvwxyz]{2,})([aeiou])', r'\1\2', s)
        reduced.append(s)
    # Recombine
    word = ''.join(preserved + reduced)
    # If word is still long (>8 chars), apply extra molting pass
    if len(word) > 8:
        # Split into syllables again
        syllables = re.findall(r'[bcdfghjklmnpqrstvwxyz]*[aeiou]+', word)
        # Always keep first syllable, drop every other unstressed syllable
        shortened = [syllables[0]] if syllables else []
        for i, s in enumerate(syllables[1:], 1):
            # Drop if short and not stressed (length <=2 and not at start/end)
            if len(s) <= 2 and i != len(syllables)-1:
                continue
            # Merge clusters again
            s = re.sub(r'([bcdfghjklmnpqrstvwxyz]{2,})([aeiou])', r'\1\2', s)
            shortened.append(s)
        word = ''.join(shortened)
        # If still long, drop final unstressed syllable
        if len(word) > 8 and word[-1] in vowels:
            word = word[:-1]
        # If still long, truncate to 8 chars (last resort)
        if len(word) > 8:
            word = word[:8]
    return word

def fantasy_affix(word):
    # Structured: extract CVC syllables from each word, blend meaningfully
    import re
    words = re.split(r'\s+', word)
    def extract_cvc(w):
        match = re.match(r'([bcdfghjklmnpqrstvwxyz]?)([aeiou])([bcdfghjklmnpqrstvwxyz]?)', w)
        return ''.join(match.groups()) if match else w[:2]
    syllables = [extract_cvc(w) for w in words]
    # Add fantasy filler syllables if needed
    fillers = ['sha', 'lor', 'ven', 'mir', 'tal', 'zan', 'dra', 'sil', 'kor', 'bel', 'sor', 'val', 'nir', 'mel', 'tor', 'ral', 'zel', 'fin', 'sol', 'dar']
    # Ensure at least 3 syllables
    while len(syllables) < 3:
        syllables.append(random.choice(fillers))
    # Blend and shuffle syllables for organic feel
    random.shuffle(syllables)
    structured = ''.join(syllables)
    # Semantic affix: pick based on concept type
    affix_map = {
        'spring': 'el', 'caverns': 'un', 'font': 'ar', 'primordial': 'shi', 'crystal': 'tar', 'oil': 'os', 'winter': 'ver', 'desert': 'an', 'fields': 'il', 'cascade': 'ad', 'entropy': 'em', 'aetherite': 'eth', 'resonance': 'res', 'magical': 'mag', 'arcane': 'ar'
    }
    for k, v in affix_map.items():
        if k in word.lower():
            structured += v
            break
    else:
        structured += random.choice(['en', 'al', 'or', 'el', 'an', 'ir'])
    # Strictly enforce minimum length and syllables
    while len(structured) < 6 or sum(1 for _ in re.finditer(r'[aeiou]', structured)) < 3:
        structured += random.choice(fillers)
    # If still short, pad more
    while len(structured) < 8:
        structured += random.choice(fillers)
    return structured[:14]

def fantasy_mutation(word):
    # Phonotactic filtering: avoid awkward clusters, apply regular sound changes
    import re
    # Lenition: soften stops
    word = re.sub(r'[ptk]', lambda m: {'p':'b','t':'d','k':'g'}[m.group()], word)
    # Assimilation: double consonants to single
    word = re.sub(r'([bcdfghjklmnpqrstvwxyz])\1+', r'\1', word)
    # Vowel harmony: favor 'a', 'e', 'o'
    word = re.sub(r'[iu]', lambda m: random.choice('aeo'), word)
    # Remove non-CVC syllables
    word = ''.join(re.findall(r'[bcdfghjklmnpqrstvwxyz]?[aeiou][bcdfghjklmnpqrstvwxyz]?', word))
    return word

def fantasy_molting(word):
    # Drop unstressed syllables (short, repeated, or at end)
    import re
    syllables = re.findall(r'[bcdfghjklmnpqrstvwxyz]*[aeiou]+', word)
    if not syllables:
        return word
    # Always keep at least 3 syllables
    result = []
    for s in syllables:
        # Only drop if >3 syllables and short/repeated
        if len(result) >= 3 and (len(s) <= 2 or (result and s == result[-1])):
            continue
        result.append(s)
    # If still too short, pad with fantasy syllables
    fillers = ['sha', 'lor', 'ven', 'mir', 'tal', 'zan', 'dra', 'sil', 'kor', 'bel', 'sor', 'val', 'nir', 'mel', 'tor', 'ral', 'zel', 'fin', 'sol', 'dar']
    while len(result) < 3:
        result.append(random.choice(fillers))
    word = ''.join(result)
    # Merge adjacent vowels
    word = re.sub(r'([aeiou])([aeiou])', r'\1', word)
    # Limit clusters to two consonants
    word = re.sub(r'([bcdfghjklmnpqrstvwxyz]{3,})', lambda m: m.group(0)[:2]+'a', word)
    # Ensure minimum length
    while len(word) < 6:
        word += random.choice(fillers)
    # Limit length
    if len(word) > 14:
        word = word[:14]
    return word

def fantasy_pronounce(word):
    # If more than two consonants in a row, insert 'a'
    import re
    word = re.sub(r'([bcdfghjklmnpqrstvwxyz]{3,})', lambda m: m.group(0)[:2]+'a', word)
    return word

def is_similar(word, existing_words, threshold=0.7):
    for w in existing_words:
        if SequenceMatcher(None, word, w).ratio() > threshold:
            return True
    return False

def conlang_unique(concept, affix_func, mutation_func, molting_func, alt_roots=None, existing_words=None):
    base = concept.lower().replace(' ', '')
    if existing_words is None:
        existing_words = []
    attempts = 0
    max_attempts = 10
    roots = [base] + (alt_roots if alt_roots else [])
    for root in roots:
        affixed = affix_func(root)
        mutated = mutation_func(affixed)
        word = molting_func(mutated)
        if not is_similar(word, existing_words):
            return word
        attempts += 1
        if attempts >= max_attempts:
            break
    return None
