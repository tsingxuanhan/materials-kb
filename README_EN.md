# 📚 Materials Science ML Knowledge Base

> 237 papers · 11 categories · ~9000 lines · For materials science students with zero ML background

## Why This Exists

Chinese-language materials science ML knowledge is scarce. Materials undergraduates face two barriers:
1. **Can't read papers** — dense ML terminology, hard to cross the language+domain gap
2. **Can't run code** — environment setup, data formats, hyperparameters are all pitfalls

This KB bridges the gap with structured, Chinese-language knowledge for materials+ML.

## Coverage

| KB | Files | Lines | Content |
|----|-------|-------|---------|
| KB0 Global Index | 1 | 2855 | ~200 papers, 11 categories |
| KB1 Materials ML Core | 8 | ~2448 | DB→descriptors→property prediction→HTS→GNN |
| KB2 Theory & Basics | 3 | ~887 | ML basics / DL optimization / Bayesian |
| KB3 Models & Tools | 4 | ~1477 | CNN / RNN / RL / frameworks |
| KB4 Generation & NLP | 2 | ~775 | Generative models / LLMs |
| KB5 Entertainment | 1 | ~349 | Games / anime / music |

**Accuracy: ~99%** (7 errors fixed, 3 pending)

## Usage

- **Direct reading**: Clone and read in order KB0 → KB2 → KB3 → KB1
- **RAG knowledge base**: Upload to Open WebUI for model retrieval
- **Fine-tuning**: Extract QA pairs → LLaMA-Factory → custom materials model

See `fine-tune/qa-extraction.md` for details.

## Contributing

Materials science classmates welcome! Fork → add entries → validate with `kb_validate.py` → PR.

## License

MIT — see [LICENSE](LICENSE)
