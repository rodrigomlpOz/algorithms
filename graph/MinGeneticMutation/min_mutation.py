from collections import deque

def minMutation(start: str, end: str, bank: list[str]) -> int:
    if end not in bank:
        return -1  # If the end gene is not in the bank, no valid path

    # Set of valid genes from the bank for quick lookup
    bank_set = set(bank)

    # Valid characters for mutation
    gene_chars = ['A', 'C', 'G', 'T']

    # BFS initialization
    queue = deque([(start, 0)])  # (current gene, mutation steps)
    visited = set([start])  # Track visited genes

    while queue:
        current_gene, mutations = queue.popleft()

        # If we've reached the end gene, return the number of mutations
        if current_gene == end:
            return mutations

        # Try mutating each character in the gene
        for i in range(len(current_gene)):
            for char in gene_chars:
                # Mutate the ith character
                mutated_gene = current_gene[:i] + char + current_gene[i+1:]

                # If the mutated gene is valid and not visited, add it to the queue
                if mutated_gene in bank_set and mutated_gene not in visited:
                    visited.add(mutated_gene)
                    queue.append((mutated_gene, mutations + 1))

    # If no valid mutation path is found
    return -1

# Example usage:
start_gene = "AACCGGTT"
end_gene = "AAACGGTA"
gene_bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]

print(minMutation(start_gene, end_gene, gene_bank))  # Output: 2
