from typing import Dict, List

import datasets


def process_docs(dataset: datasets.Dataset) -> datasets.Dataset:
    """
    Process the PutnamBench dataset documents to extract problems, solutions, and answers.
    
    Args:
        dataset: The PutnamBench dataset
        
    Returns:
        Processed dataset with problem, solution, and answer fields
    """
    def _process_doc(doc: dict) -> dict:
        out_doc = {
            "problem": doc["informal_statement"],
            "solution": doc["informal_solution"],
            "answer": extract_answer(doc["informal_solution"]),
            "tags": doc["tags"]
        }
        return out_doc

    return dataset.map(_process_doc)


def extract_answer(solution: str) -> str:
    """
    Extract the final answer from the solution.
    For Putnam problems, the answer is typically the last statement or result.
    
    Args:
        solution: The informal solution text
        
    Returns:
        The extracted answer
    """
    return solution


def process_results(doc: dict, results: List[str]) -> Dict[str, float]:
    """
    Process model results and compare with ground truth.
    
    Args:
        doc: The document with the ground truth
        results: The model's generated results
        
    Returns:
        Dictionary with evaluation metrics
    """
    
    model_answer = results[0].strip()
    
    ground_truth = doc["answer"].strip()
    
    exact_match = 0.0
    if model_answer == ground_truth:
        exact_match = 1.0
    
    return {
        "exact_match": exact_match,
    }


def normalize_answer(answer: str) -> str:
    """
    Normalize the answer string for comparison.
    
    Args:
        answer: The answer string
        
    Returns:
        Normalized answer string
    """
    return answer.strip().lower()
