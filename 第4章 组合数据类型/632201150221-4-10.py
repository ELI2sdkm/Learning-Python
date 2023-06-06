# 创建多个字典，对于每个字典，都使用一个宠物的名称来给它命名；在每个字典中，包含宠物的类型及其主人的名字。将这这些字典存储在一个名为pets的列表中，再遍历该列表，并将宠物的所有信息都输出。

pet1 = {'type': 'dog', 'master': 'Alan'}
pet2 = {'type': 'cat', 'master': 'Bob'}
pet3 = {'type': 'dragon', 'master': 'Anonymous'}
pets = {'dog': pet1, 'cat': pet2, 'dragon': pet3}
for key in pets:
    print(key, value)
