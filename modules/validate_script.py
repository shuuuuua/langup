def validate_script(original, target):
    original_words = original.split()
    target_words = target.split()

    diff = []
    for i, org_word in enumerate(original_words):
        if len(target_words) <= i:
            break

        if org_word != target_words[i]:
            diff.append((i, target_words[i]))
        i += 1

    return diff

print('Test1')
original = 'The query execution graph provides an intuitive interface for inspecting query execution details.'
target = 'The query execution graph provides an intuitive interface for inspecting query execution details.'
diff = validate_script(original, target)
if len(diff) == 0:
    print('Pass')
    print(diff)
else:
    print('Fail')
    print(diff)

print('Test2')
original = 'The query execution graph provides an intuitive interface for inspecting query execution details.'
target = 'The query exec graph provides an intuitive interface for inspecting query execution details.'
diff = validate_script(original, target)
if diff == [(2,'exec')]:
    print('Pass')
    print(diff)
else:
    print('Fail')
    print(diff)

print('Test3')
original = 'The query execution graph provides an intuitive interface for inspecting query execution details.'
target = 'The query exec g provides an intuitive interface for inspecting query execution details.'
diff = validate_script(original, target)
if diff == [(2,'exec'), (3, 'g')]:
    print('Pass')
    print(diff)
else:
    print('Fail')
    print(diff)

print('Test4')
original = 'The query execution graph provides an intuitive interface for inspecting query execution details.'
target = 'The query exec graph provide an intuitive interface for inspecting query execution details.'
diff = validate_script(original, target)
if diff == [(2,'exec'), (4, 'provide')]:
    print('Pass')
    print(diff)
else:
    print('Fail')
    print(diff)

print('Test5')
original = 'The query execution graph provides an intuitive interface for inspecting query execution details.'
target = 'The query graph provides an intuitive interface for inspecting query execution details.'
diff = validate_script(original, target)
if diff == [(2,None)]:
    print('Pass')
    print(diff)
else:
    print('Fail')
    print(diff)
