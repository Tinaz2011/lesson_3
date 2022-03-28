def int_func(text):
    return text.title()
def my_title(text):
    listed_text = list(text)
    listed_text[0] = listed_text[0].upper()
    return ''.join(listed_text)


output_1 = []
output_2 = []
for word in input('Input str and seperate words by" ": ').split(' '):
    output_1.append(int_func(word))
    output_2.append(my_title(word))

print(f'Var1 str is: {" ".join(output_1)}')
print(f'Var1 str is: {" ".join(output_2)}')