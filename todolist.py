task_list = ["sehri", "namaz", "quran", "assigment", "iftar"]
complete_task = []

def todo():
    # agar task list ki len main kuch nahi to input lo warna all tasks are completed ka msg show karao
    if len(task_list) > 0:
        task = input("Enter completed task : ").lower()
        # jab bhi hum element pop karain gay to wo index re arrange kardaiga so last element ki index bhi end main 0 hogi
        # lehaza element ko us index k specific number say pop nahi kara saktay
        # is liyay index() say us particular element ko pop karain gay to prolem nahi ai gi
        if task == "sehri":
            complete_task.append(task_list.pop(task_list.index("sehri")))  
        elif task == "namaz":
            complete_task.append(task_list.pop(task_list.index("namaz")))
        elif task == "quran":
            complete_task.append(task_list.pop(task_list.index("quran")))
        elif task == "assigment":
            complete_task.append(task_list.pop(task_list.index("assigment")))
        elif task == "iftar":
            complete_task.append(task_list.pop(task_list.index("iftar")))
        else:
            print("Given task isn't present in task list.")
            task = input("Enter completed task : ").lower()
        else:
            print("All the tasks are Completed.")

def task_check():
    # agar tasks list empty hai to pehli martaba input lo
        if len(complete_task) == 0:
            todo()
            print("Remaining Tasks : {} \nCompleted Tasks : {} \n".format(task_list, complete_task))
    # agar tasks list empty nahi hai to yes or no input lo
        elif len(complete_task) > 0:
    # agar koi or task complete kia hai to again input completed task k liyay input lo
            another_task = input("Did you completed another task [y/n] : ").lower()
            if len(complete_task) != 0 and another_task == "y":
                todo()
                print("Remaining Tasks : {} \nCompleted Tasks : {}\n".format(task_list, complete_task))
            elif len(complete_task) != 0 and another_task == "n":
                exit()
            else:
                print("Error! Invalid command.")
                another_task = input("Did you completed another task [y/n] : ").lower()

                
             
task_check()
if len(task_list) == 0:
    print("All tasks are Completed.")

