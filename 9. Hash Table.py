hash_table = [[] for _ in range(10)]

def insert(hash_table, key, value):
    hash_key = hash(key) % len(hash_table)
    key_exists = False
    bucket = hash_table[hash_key]
    for count, key_value in enumerate(bucket):
        keyy, val = key_value
        if key == keyy:
            key_exists = True
            break
    if key_exists:
        bucket[count] = ((key, value))
    else:
        bucket.append((key, value))

insert(hash_table, 10, 'Nepal')
insert(hash_table, 25, 'USA')
insert(hash_table, 20, 'India')
print(hash_table)

'''output:  [[(10, 'Nepal'), (20, 'India')], [], [], [], [], [(25, 'USA')], [], [], [], []]'''
