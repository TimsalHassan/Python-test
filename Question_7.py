'''
Problem 7:-
    Write a context manager that handles file operations, ensuring that files are properly opened and closed, even in cases of exceptions.
'''
import os

def file_present(path):
    return os.path.isfile(path)

path = 'file1.txt'
operation = input("Read or Write: ").strip().upper()
text = input("Write correction : ")

try:
    if operation == 'READ':
        if file_present(path):
            with open(path, 'r') as file_obj:
                try:
                    data = file_obj.read().splitlines()
                    print(data)
                finally:
                    file_obj.close()
        else:
            print("File not found")
    elif operation == 'WRITE':
        if file_present(path):
            with open(path, 'w') as file_obj:
                try:
                    file_obj.write(text)
                    print("Write operation successful")
                finally:
                    file_obj.close()
        else:
            with open(path, 'a') as file_obj:
                try:
                    file_obj.write(text)
                    print("Write operation successful")
                finally:
                    file_obj.close()
    else:
        print("Invalid operation. Please enter 'READ' or 'WRITE'.")
except Exception as e:
    print(f"An error occurred: {e}")
