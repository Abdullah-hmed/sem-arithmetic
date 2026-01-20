## 🧪 Setup

### 1. Clone the repository

```bash
git clone https://github.com/Abdullah-hmed/sem-arithmetic.git
cd sem-arithmetic
```

### 2. Create a virtual environment

#### On Linux / macOS

```bash
python -m venv .venv
source .venv/bin/activate
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

## 🧪 Examples

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

## 🛠️ Configuration

You can tweak these constants in the script:

```python
MODEL_PATH = "models/crawl-300d-2M-subword.vec"
CACHE_PATH = "models/fasttext_cc_300d.kv"
TOP_N = 5
```

