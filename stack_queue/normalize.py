def simplifyPath(path: str) -> str:
    # Split the path into components based on '/'
    components = path.split('/')
    
    # Stack to store valid directory names
    stack = []
    
    for component in components:
        if component == '' or component == '.':
            # Ignore empty components and current directory '.'
            continue
        elif component == '..':
            # Move one level up (pop from stack) if possible
            if stack:
                stack.pop()
        else:
            # Add the directory name to the stack
            stack.append(component)
    
    # Join the valid components with '/' and ensure the path starts with '/'
    return '/' + '/'.join(stack)

