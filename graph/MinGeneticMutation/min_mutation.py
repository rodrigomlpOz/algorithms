from collections import deque

def minMutation(start: str, end: str, bank: list[str]) -> int:
    # If the end gene is not in the bank, there's no way to reach it
    if end not in bank:
        return -1

    # Convert bank to a set for O(1) lookups
    bank_set = set(bank)
    
    # Define the possible characters for mutation
    gene_chars = ['A', 'C', 'G', 'T']

    # Initialize BFS queue with the start gene and a mutation count of 0
    queue = deque([(start, 0)])
    
    # Track visited genes to avoid revisiting
    visited = set([start])

    # Perform BFS
    while queue:
        current_gene, mutations = queue.popleft()

        # If we reached the end gene, return the number of mutations
        if current_gene == end:
            return mutations

        # Try mutating each character in the gene
        for i in range(len(current_gene)):
            for char in gene_chars:
                # Generate a mutated gene by changing one character
                mutated_gene = current_gene[:i] + char + current_gene[i+1:]
                
                # If the mutated gene is valid and hasn't been visited
                if mutated_gene in bank_set and mutated_gene not in visited:
                    # Mark it as visited and add it to the queue
                    visited.add(mutated_gene)
                    queue.append((mutated_gene, mutations + 1))

    # If no mutation path is found, return -1
    return -1

# Example usage:
start_gene = "AACCGGTT"
end_gene = "AAACGGTA"
gene_bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]

result = minMutation(start_gene, end_gene, gene_bank)
print(result)  # Output: 2
