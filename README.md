
# Semantic Arithmetic

Perform **mathematical operations on words**

This tool lets you write expressions like:

```
king - man + woman
france - paris + italy
(king + queen) - (man + woman)
```

…and returns the **closest semantic concepts** using vector arithmetic over pretrained **FastText word embeddings**.

It’s essentially a small REPL for exploring **concept arithmetic in embedding space**.


## ✨ Features

* **Vector arithmetic on words**
* Supports `+`, `-`, and **nested parentheses**
* Uses **FastText 300-dimensional vectors** (subword-aware)
* **Model caching** for fast startup after first load
* Interactive CLI
* Displays **top-N closest semantic matches**


## 🧪 Setup

### 1. Clone the repository

```bash
git clone https://github.com/Abdullah-hmed/sem-arithmetic.git
cd sem-arithmetic
```

### 2. Create a virtual environment

#### On Linux / macOS

```bash
python -m venv venv
source venv/bin/activate
```

#### On Windows (PowerShell)

```powershell
python -m venv .venv
.venv\Scripts\Activate
```


### 3. Install dependencies

```bash
pip install -r requirements.txt
```


### 4. Running the Tool

Once the virtual environment is active:

```bash
python main.py
```


## 📥 Download the Model

This project uses Facebook’s pretrained FastText English vectors:

**crawl-300d-2M-subword**

Download and extract:

```
https://dl.fbaipublicfiles.com/fasttext/vectors-english/crawl-300d-2M-subword.zip
```

Place the extracted file here:

```
models/crawl-300d-2M-subword.vec
```

On first run, the model will be **cached automatically** for faster future loads.


## 📂 Project Structure

```
.
├── main.py
├── models/
│   ├── crawl-300d-2M-subword.vec
│   └── fasttext_cc_300d.kv   # auto-generated cache
└── README.md
```


## ▶️ Usage

Run the program:

```bash
python main.py
```

You’ll enter an interactive prompt:

```
Welcome to Semantic Arithmetic!
Type 'exit' to quit.
>
```


## 🧪 Examples

### Basic analogy

```
king - man + woman
```

Output:

```
Top results:
  1. queen               0.74
  2. monarch             0.68
  3. princess            0.66
```


### Parentheses support

```
(king + queen) - (man + woman)
```


### Arbitrary spacing allowed

All of these are valid:

```
king+woman
king +woman
king+ woman
```


## 🧠 How It Works

Each word is mapped to a **300-dimensional vector**.

An expression like:

```
king - man + woman
```

is evaluated as:

```
vector("king") - vector("man") + vector("woman")
```

The result vector is then compared (via cosine similarity) to all words in the vocabulary, and the **closest matches** are returned.


## ⚠️ Limitations & Notes

* Results depend heavily on **training data bias**
* Not all semantic relations are linear


## 🛠️ Configuration

You can tweak these constants in the script:

```python
MODEL_PATH = "models/crawl-300d-2M-subword.vec"
CACHE_PATH = "models/fasttext_cc_300d.kv"
TOP_N = 5
```

