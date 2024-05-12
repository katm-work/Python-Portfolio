
nums = [4, 56, 3, 7, 87 ,9, 546, 8, 1239, 403 ,31, 57, 756, 3, 5, 7, 5, 4, 3, 4, 6, 46, 87, 66]
sum = 0
count = 0
for num in (nums):
    if not (num % 2):
       sum += num
       count += 1
average = sum/count
print(average)

names = ['Beth', 'Margaret', 'Bob', 'Faye', 'Kristen', 'Luqman', 'Mom', 'Dad', 'Min', 'Johnny']
count = 0
for name in (names):
     for letter in (name):
        if letter == 'M':
         count += 1
print(count)