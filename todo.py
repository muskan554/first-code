#projetc: My To-Do List App -by Muskan
tasks =[]
while True:
    print("\n---Mera To-DO App---")
    print("1.Task Add karo")
    print("2.Saare Task dekho")
    print("3.Task delete karo")
    print("4.Exit")
    choice = input("Apna choice batao (1-4):")
    if choice =='1':
        task = input("Naya Task likho:")
        tasks.append(task)
        print(f"'{task}' add ho gaya!")
    elif choice == '2':
        if not tasks:
            print("Koi task nhi hai,pehle add karo.")
        else:
            print("\nTumhare Task:")
            for i,t in enumerate(tasks,1):
                print(f"{i}.{t}")
    elif choice =='3':
        if not tasks :
              print("Delete karne ko kuch nhi hai.")
        else:
            num = int(input("Kaunsa number delete karna hai?"))
            if 1 <= num <= len(tasks):
                removed =tasks.pop(num-1)
                print(f"'{removed}' delete ho gaya.")
            else:
                print("Galat number!")
    elif choice =='4':
                print("Bye Muskan! kal milte hai.") 
                break
    else:
        print("1 se 4 ke beech me likho yaar!")     