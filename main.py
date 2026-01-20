import re
import os
from gensim.models import KeyedVectors


MODEL_PATH = "models/crawl-300d-2M-subword.vec"
CACHE_PATH = "models/fasttext_cc_300d.kv"
TOP_N = 5

def tokenize(expr):
    expr = re.sub(r'([+\-()])', r' \1 ', expr)
    return [t for t in expr.split() if t]

def parse_parentheses(tokens):
    positive = []
    negative = []
    current_sign = '+'
    i = 0
    
    while i < len(tokens):
        token = tokens[i]
        
        if token == '+':
            current_sign = '+'
        elif token == '-':
            current_sign = '-'
        elif token == '(':
            depth = 1
            j = i + 1
            while j < len(tokens) and depth > 0:
                if tokens[j] == '(':
                    depth += 1
                elif tokens[j] == ')':
                    depth -= 1
                j += 1
            
            if depth != 0:
                raise ValueError("Mismatched parentheses")
            
            sub_tokens = tokens[i+1:j-1]
            sub_pos, sub_neg = parse_parentheses(sub_tokens)
            
            if current_sign == '+':
                positive.extend(sub_pos)
                negative.extend(sub_neg)
            else:
                positive.extend(sub_neg)
                negative.extend(sub_pos)
            
            i = j
            continue
        elif token == ')':
            raise ValueError("Unexpected closing parenthesis")
        else:
            if current_sign == '+':
                positive.append(token.lower())
            else:
                negative.append(token.lower())
        
        i += 1
    
    return positive, negative

def parse_expression(expr):
    tokens = tokenize(expr)
    if not tokens:
        return [], []
    return parse_parentheses(tokens)

# -----------------------------
# Main
# -----------------------------
def main():
    # Load model (use cached version if available)
    if os.path.exists(CACHE_PATH):
        print(f"Loading cached model from {CACHE_PATH}...")
        model = KeyedVectors.load(CACHE_PATH)
        print("Model loaded!")
    else:
        print(f"Loading FastText model from {MODEL_PATH}...")
        print("(This may take a while...)")
        try:
            model = KeyedVectors.load_word2vec_format(
                MODEL_PATH,
                binary=False,
                unicode_errors="ignore"
            )
            print(f"Saving cache to {CACHE_PATH} for faster loading...")
            model.save(CACHE_PATH)
            print("Model loaded!")
        except FileNotFoundError:
            print(f"Model file not found: {MODEL_PATH}")
            print("Download: https://dl.fbaipublicfiles.com/fasttext/vectors-english/crawl-300d-2M-subword.zip")
            return
        except Exception as e:
            print(f"Error loading model: {e}")
            return

    print("Welcome to Semantic Arithmetic!")
    print("Type 'exit' to quit.")
    while True:
        try:
            expr = input("> ").strip()

            if expr.lower() in {"exit", "quit", "q"}:
                print("Goodbye!")
                break

            if not expr:
                continue

            positive, negative = parse_expression(expr)

            if not positive and not negative:
                print("No valid words detected.")
                continue

            print(f"Computing: ", end="")
            if positive:
                print(f"[+{', +'.join(positive)}]", end=" ")
            if negative:
                print(f"[-{', -'.join(negative)}]", end="")
            print()

            missing = []
            for word in positive + negative:
                if word not in model:
                    missing.append(word)
            
            if missing:
                print(f"Some words not in vocab: {', '.join(missing)}")

            # Vector arithmetic
            results = model.most_similar(
                positive=positive if positive else None,
                negative=negative if negative else None,
                topn=TOP_N
            )

            print("Top results:")
            for i, (word, score) in enumerate(results, start=1):
                print(f"  {i}. {word:<20} {score:.4f}")
            print()

        except ValueError as e:
            print(f"Parse error: {e}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()