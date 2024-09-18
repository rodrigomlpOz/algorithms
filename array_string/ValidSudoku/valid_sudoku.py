def is_valid_sudoku(board: list[list[str]]) -> bool:
    # Initialize sets to track the numbers in rows, columns, and sub-boxes
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    sub_boxes = [set() for _ in range(9)]
    
    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num == '.':
                continue
            
            # Determine sub-box index
            sub_box_index = (i // 3) * 3 + (j // 3)
            
            # Check if the number is already in the row, column, or sub-box
            if num in rows[i] or num in cols[j] or num in sub_boxes[sub_box_index]:
                return False
            
            # Add the number to the corresponding row, column, and sub-box
            rows[i].add(num)
            cols[j].add(num)
            sub_boxes[sub_box_index].add(num)
    
    # If no rule is violated, return True
    return True