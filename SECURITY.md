# Security

## Safe by design

This package is a **pure model architecture definition** — it contains no code that:

- ✅ Makes network requests
- ✅ Executes arbitrary strings (`exec`, `eval`, `compile`)
- ✅ Deserializes untrusted data (`pickle`)
- ✅ Spawns processes or shells
- ✅ Reads/writes to the filesystem during inference
- ✅ Installs C extensions or post-install scripts

## What the package does

Defines PyTorch `nn.Module` classes that perform standard tensor math:
matrix multiplication, softmax, layer normalization, rotary embeddings.

## What to watch out for

The only attack surface is **model weights loaded from untrusted sources**:

- `.bin` files use `pickle` internally — **never load untrusted `.bin` files**
- `.safetensors` and `.gguf` are safe binary formats (no code execution on load)
- Always prefer `.safetensors` or GGUF for untrusted weights

## Reporting

If you find a security issue, do not open a public issue. Contact Gurt directly.
