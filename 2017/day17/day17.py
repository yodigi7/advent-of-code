# step
input = 345

print("----------PART 1----------")
lock = [0]
index = 0
for i in range(1, 2018):
    insertIdx = ((input + index) % len(lock)) + 1
    lock.insert(insertIdx, i)
    index = insertIdx
print(lock[insertIdx + 1])

print("----------PART 2----------")
lock_len = 1
val_after_0 = None
for i in range(1, 50_000_000):
    insertIdx = ((input + index) % lock_len) + 1
    if insertIdx == 1:
        val_after_0 = i
    lock_len += 1
    index = insertIdx
print(val_after_0)
