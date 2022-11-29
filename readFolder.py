import os
import glob

# print(os.getcwd())

# print(os.listdir())

# print(os.path.exists('Folder1.zip'))

# print(os.path.isdir('Folder1'))
# print(os.path.isdir('Folder1/file1.txt'))

# print(os.path.isfile('Folder1')) 
# print(os.path.isfile('Folder1/file1.txt'))

# print(os.path.join('Folder1', 'file1.txt'))

# for path in os.listdir(os.getcwd()):
#     if os.path.isfile(os.path.join(os.getcwd(), path)):
#         print('File => %s'%path)
#     elif os.path.isdir(os.path.join(os.getcwd(), path)):
#         print('Directory => %s'%path)


# for name in glob.glob(os.getcwd()+'**/**',recursive=True):
#     print(name)

# for root,d_names,f_names in os.walk(os.getcwd()):
# 	print (root, d_names, f_names)


# def test(rootPath):
#     for path in os.listdir(rootPath):
#         newPath = rootPath + '\\' + path
#         if os.path.isdir(os.path.join(os.getcwd(), newPath)):
#             print('Folder => %s'%newPath)
#             test(newPath)
#         if os.path.isfile(os.path.join(os.getcwd(), newPath)):
#             print('File => %s'%newPath)
# test(os.path.join(os.getcwd(), 'Folder1'))