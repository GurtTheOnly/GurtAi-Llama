# GurtAi-Llama

A fully renamed **Llama** architecture fork. Every class, every file — branded **GurtAi**.

| Original | GurtAi |
|----------|--------|
| `LlamaModel` | `GurtAiModel` |
| `LlamaForCausalLM` | `GurtAiForCausalLM` |
| `LlamaAttention` | `GurtAiAttention` |
| `LlamaDecoderLayer` | `GurtAiDecoderLayer` |
| `LlamaConfig` | `GurtAiConfig` |
| `LlamaRMSNorm` | `GurtAiRMSNorm` |
| `LlamaMLP` | `GurtAiMLP` |
| `LlamaRotaryEmbedding` | `GurtAiRotaryEmbedding` |

## Usage

```python
from gurtai_llama import GurtAiConfig, GurtAiForCausalLM

config = GurtAiConfig()
model = GurtAiForCausalLM(config)
```

### Load existing Llama weights

```python
from gurtai_llama import GurtAiForCausalLM

model = GurtAiForCausalLM.from_pretrained(
    "meta-llama/Llama-3.2-1B",        # or: /path/to/your.gguf
    config="meta-llama/Llama-3.2-1B",
    torch_dtype="auto",
)
print(type(model))  # <class 'gurtai_llama.modeling_gurt_llama.GurtAiForCausalLM'>
```

## Install

```bash
pip install -e .
```

## License

Apache 2.0 — derived from Meta's Llama. See `LICENSE`.
