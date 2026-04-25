def even_gen():
    for i in range(2, 22, 2):
        yield i

# Usage
print(list(even_gen()))
