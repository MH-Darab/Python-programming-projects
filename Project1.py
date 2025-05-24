import os
import pickle

file_path="data.dat"

if os.path.exists(file_path):
    with open(file_path, "rb") as file:
        dictionary = pickle.load(file)
else:
    dictionary = dict()
    with open(file_path, "wb") as file:
        pickle.dump(dictionary, file)

def save(dictionary):
    with open(file_path, "wb") as file:
        pickle.dump(dictionary, file)
        
def delete():
    dictionary.pop(awnser)
    
def z():
    print("-----------------------")

while True:
    os.system("cls")
    print(dictionary)
    awnser=input("Do you want del or ask? (d/a): ").strip().lower()
    if awnser=="a":
        word = input("Give your word to say what's the meaning: ").strip().lower()
        if word in dictionary:
            print(f"Meaning: {dictionary[word]}")
            z()
        else:
            answer1 = input("I don't know this word. Do you know it? (y/n): ").strip().lower()
            if answer1 == "y":
                meaning = input("What's the meaning?: ").strip()
                dictionary[word] = meaning
                save(dictionary)
                print("Saved successfully!")
                z()
            else:
                answer2 = input("Do you want to try another word? (y/n): ").strip().lower()
                if answer2 == "y":
                    z()
                    continue
                else:
                    print("Goodbye!")
                    break
    else:
        awnser=input("Whats word do you want to delete: ")
        if awnser in dictionary:
            delete()
            save(dictionary)
            input("Delete suceessfully")
            z()
        else:
            input(f"{awnser} isnt there")