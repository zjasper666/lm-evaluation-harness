# Putnam Competition Benchmark

This benchmark evaluates language models on problems from the William Lowell Putnam Mathematical Competition, one of the most prestigious mathematics competitions for undergraduate students in the United States and Canada.

## Overview

The Putnam Competition consists of challenging mathematical problems that test deep reasoning skills across various mathematical domains. This benchmark uses problems from the PutnamBench dataset, which contains 522 problems from Putnam competitions spanning from 1965 to 2023.

## Task Structure

The benchmark is divided into subtasks based on mathematical domains:
- Algebra (putnam_algebra)
- Analysis (putnam_analysis)
- Number Theory (putnam_number_theory)
- Linear Algebra (putnam_linear_algebra)
- Abstract Algebra (putnam_abstract_algebra)
- Geometry (putnam_geometry)

## Dataset

The benchmark uses the [PutnamBench dataset](https://huggingface.co/datasets/amitayusht/PutnamBench) from Hugging Face, which provides:
- Formal problem statements in multiple languages (Lean 4, Isabelle, Coq)
- Informal problem statements and solutions
- Problem metadata including tags for mathematical domains

## Evaluation

Models are evaluated on their ability to generate solutions to Putnam problems. The evaluation metrics include:
- Exact match: Whether the model's solution exactly matches the reference solution
- (Future work: Mathematical equivalence checking for more robust evaluation)

## Usage

To evaluate a model on the Putnam benchmark:

```bash
python -m lm_eval --model hf \
    --model_args pretrained=<model_name_or_path> \
    --tasks putnam \
    --device cuda:0
```

To evaluate on a specific subtask:

```bash
python -m lm_eval --model hf \
    --model_args pretrained=<model_name_or_path> \
    --tasks putnam_algebra \
    --device cuda:0
```
