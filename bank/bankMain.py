import os
import pyautogui
import subprocess
import time


import random
import string

import csv
import keyboard
import shutil

from rich import print
from rich.console import Console
from rich.progress import Progress
from rich.table import Table


def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    result_str = ''.join(random.choice(characters) for i in range(length))
    return result_str

def username_exists(username):
    with open("./static/userData.csv", "r") as userData:
        reader = csv.reader(userData)
        next(reader)  # Skip the header
        for row in reader:
            if row[0] == username:
                return True
    return False

def username_not_exists(username):
    with open("./static/userData.csv", "r") as userData:
        reader = csv.reader(userData)
        next(reader)  # Skip the header
        for row in reader:
            if row[0] == username:
                return False
    return True

def signup_animation(console):
    with Progress() as progress:
        task = progress.add_task("[cyan]Signing up...", total=100)

        for i in range(100):
            time.sleep(0.05)  # Simulate some work
            progress.update(task, advance=1)
        
        progress.stop()
    # Display Markdown-formatted text after the progress bar
    print("[bold green]Signup SuccessFul.[/bold green]")

def login_animation(console):
    with Progress() as progress:
        task = progress.add_task("[cyan]Logging in ...", total=100)

        for i in range(100):
            time.sleep(0.05)  # Simulate some work
            progress.update(task, advance=1)
        
        progress.stop()

    # Display Markdown-formatted text after the progress bar
    print("[bold green]Login SuccessFul.[/bold green]")

def transaction_animation(console):
    with Progress() as progress:
        task = progress.add_task("[cyan]Transaction is in Progress ...", total=100)

        for i in range(100):
            time.sleep(0.05)  # Simulate some work
            progress.update(task, advance=1)
        
        progress.stop()

def password_is_correct(username, password):
    with open('./static/userData.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip the header
        for row in reader:
            if username == row[0] and password == row[1]:  # Check if the username and password match
                return True
    return False

def UPI_id_exists(UPI_id):
    with open("./static/userData.csv", "r") as userData:
        reader = csv.reader(userData)
        next(reader)  # Skip the header
        for row in reader:
            if row[5] == UPI_id:
                return True
    return False


def find_and_right_click(folder_path, target_folder_name):
    subprocess.Popen(f'explorer "{folder_path}"')
    time.sleep(3)  # Adjust this value based on your system's responsiveness

    # List items in the folder
    items = os.listdir(folder_path)

    # Check if the target folder is in the list
    if target_folder_name in items:
        # Get the position of the target folder in the window
        target_folder_position = items.index(target_folder_name)
        chooseFolder = 0
        if target_folder_position == 0:
            chooseFolder = 300 + 25
        else:
            chooseFolder = 300 + target_folder_position * 25

        # Print debug information
        # print(f"Moving to coordinates: (500, {chooseFolder})")

        # Move to the coordinates and click
        pyautogui.click(500, 325)


outer_loop_flag = True  # Flag to control the outer loop

while outer_loop_flag :
    try:
        console = Console()


        print("[bold blue]1 = Signup\n 2 = Login\n 3 = Exit[/bold blue]")
        userOperation = int(input("Enter operation : "))

        if userOperation == 1 :
            console.rule("[bold yellow]Signup[/bold yellow]", characters="=")

            # Function to validate non-empty input
            def get_non_empty_input(prompt):
                while True:
                    user_input = input(prompt)
                    if user_input.strip():  # Check if input is not empty after stripping whitespace
                        return user_input
                    else:
                        console.print("[bold red]Input cannot be empty. Please try again.[/bold red]")

            fname = get_non_empty_input("Enter FirstName: ")
            lname = get_non_empty_input("Enter LastName: ")
            username = get_non_empty_input("Enter Username: ")

            if username_exists(username):
                console.print("[bold red]Username already exists.[/bold red]")
                time.sleep(2)
                continue

            password = get_non_empty_input("Enter Password: ")

            upi_id = generate_random_string(20)
            four_digit_pin = random.randint(1000, 9999)
            safe_name = username + "_" + "safe"
            header = ["username", "password", "first_name", "last_name", "balance", "upi_id","pin", "transaction_history_path", "safe_name"]
            data = [username, password, fname, lname, "1000", upi_id, four_digit_pin, "./static/transactionHistory.csv", safe_name]
            safe_path = "./safe_root/" + safe_name
            os.mkdir(safe_path)

            if os.path.isfile("./static/userData.csv") and os.path.getsize("./static/userData.csv") > 0:
                # If file exists and is not empty, append without writing the header
                with open("./static/userData.csv", "a", newline='') as signupFile:
                    writer = csv.writer(signupFile)
                    writer.writerow(data)
            else:
                # If file doesn't exist or is empty, write the header and data
                with open("./static/userData.csv", "w", newline='') as signupFile:
                    writer = csv.writer(signupFile)
                    writer.writerow(header)
                    writer.writerow(data)

            signup_animation(console)
            os.system('cls' if os.name == 'nt' else 'clear')

        elif userOperation == 2 :
            console.rule("[bold yellow]Welcome back![/bold yellow]", characters="=")

            # Function to validate non-empty input
            def get_non_empty_input(prompt):
                while True:
                    user_input = input(prompt)
                    if user_input.strip():  # Check if input is not empty after stripping whitespace
                        return user_input
                    else:
                        console.print("[bold red]Input cannot be empty. Please try again.[/bold red]")

            lgn_username = get_non_empty_input("Enter Username: ")

            if username_not_exists(lgn_username):
                console.print("[bold red]Username not exists.[/bold red]")
                time.sleep(2)
                continue

            lgn_password = get_non_empty_input("Enter Password: ")
            if not password_is_correct(lgn_username, lgn_password):
                console.print("[bold red]Incorrect password.[/bold red]")
                time.sleep(2)
                continue

            # login_animation(console)

            # time.sleep(3)

            os.system('cls' if os.name == 'nt' else 'clear')

            login_loop_flag = True # Flag to control the login loop

            while login_loop_flag :
                try:
                    print("[bold blue]1 = Balance\n 2 = Pay\n 3 = Profile\n 4 = Transaction History\n 5 = Update Profile\n 6 = safe\n7 = Back\n8 = Exit[/bold blue]")
                    login_userOperation = int(input("Enter operation : "))
                    if login_userOperation == 1 :
                        with open("./static/userData.csv", "r") as checkBalanceFile :
                            reader = csv.reader(checkBalanceFile)
                            next(reader)  # Skip the header
                            for row in reader:
                                if row[0] == lgn_username :
                                    print(str(row[4]) + " INR")

                                    while True :
                                        # Check if Enter is pressed
                                        if keyboard.is_pressed('enter'):
                                            print("Enter pressed! Exiting inner loop.")
                                            time.sleep(1)
                                            break
                    
                    elif login_userOperation == 2 :
                        console.rule("[bold yellow]Payment Page![/bold yellow]", characters="=")
                        try:
                            def get_non_empty_input(prompt):
                                while True:
                                    user_input = input(prompt)
                                    if user_input.strip():  # Check if input is not empty after stripping whitespace
                                        return user_input
                                    else:
                                        console.print("[bold red]Input cannot be empty. Please try again.[/bold red]")
                            def get_amount_input_control(prompt):
                                while True:
                                    user_input = input(prompt)
                                    if user_input.strip():  # Check if input is not empty after stripping whitespace
                                        with open("./static/userData.csv", "r") as sendMoneyFile :
                                            reader = csv.reader(sendMoneyFile)
                                            next(reader)  # Skip the header
                                            for row in reader:
                                                if row[0] == lgn_username :
                                                        if int(user_input) <= int(row[4]) / 1.10 :
                                                            return user_input
                                                        else:
                                                            console.print("[bold red]You can only withdraw 90% or less amount of total.[/bold red]")

                                    else:
                                        console.print("[bold red]Input cannot be empty. Please try again.[/bold red]")
                            def get_upi_id_control(prompt):
                                while True:
                                    user_input = input(prompt)
                                    if user_input.strip():  # Check if input is not empty after stripping whitespace
                                        if len(user_input) == 20:
                                            with open("./static/userData.csv", "r") as sendMoneyFile:
                                                reader = csv.reader(sendMoneyFile)
                                                next(reader)  # Skip the header
                                                for row in reader:
                                                    if row[5] == user_input:
                                                        return user_input  # Correct UPI id found, exit the loop and return
                                                console.print("[bold red]UPI id is incorrect.[/bold red]")
                                        else:
                                            console.print("[bold red]UPI id must be 20 digits long.[/bold red]")
                                    else:
                                        console.print("[bold red]Input cannot be empty. Please try again.[/bold red]")

                            receiver_upi_id = get_upi_id_control("Enter Receiver UPI Id : ")
                            amount = int(get_amount_input_control("Enter Amount To Send : "))

                            receiver_account_pin = int(get_non_empty_input("Enter your Secret Pin : "))

                            with open("./static/userData.csv", "r") as sendMoneyFile :
                                reader = csv.reader(sendMoneyFile)
                                next(reader)  # Skip the header
                                for row in reader:
                                    if row[0] == lgn_username :
                                        if int(row[6]) == receiver_account_pin :
                                            final_confirmation = input("Enter 'y' to confirm and 'n' to cancel : ")
                                            if final_confirmation == "y":
                                                new_amount_sender = int(row[4]) - amount

                                                # Read all data from the CSV file
                                                with open("./static/userData.csv", "r") as file:
                                                    reader = csv.reader(file)
                                                    rows = list(reader)

                                                # Update the balance for the sender (lgn_username)
                                                for i, row in enumerate(rows):
                                                    if row[0] == lgn_username:
                                                        rows[i][4] = str(new_amount_sender)

                                                        # Find the receiver's row using UPI ID
                                                        receiver_row = None
                                                        for j, row in enumerate(rows):
                                                            if row[5] == receiver_upi_id:
                                                                receiver_row = row
                                                                break

                                                        if receiver_row:
                                                            new_amount_receiver = int(receiver_row[4]) + amount
                                                            receiver_row[4] = str(new_amount_receiver)

                                                            # Write the updated data back to the CSV file
                                                            with open("./static/userData.csv", "w", newline='') as file:
                                                                writer = csv.writer(file)
                                                                writer.writerows(rows)

                                                            receiver_username = None

                                                            # Find the receiver's username using their UPI ID
                                                            with open("./static/userData.csv", "r") as userDataFile:
                                                                reader = csv.reader(userDataFile)
                                                                next(reader)  # Skip the header
                                                                for row in reader:
                                                                    if row[5] == receiver_upi_id:
                                                                        receiver_username = row[0]
                                                                        break

                                                            if receiver_username is not None:
                                                                # Update the transaction history
                                                                with open("./static/transactionHistory.csv", "a", newline='') as transaction_file:
                                                                    transaction_writer = csv.writer(transaction_file)
                                                                    transaction_index = len(row[7].split("::"))
                                                                    transaction_writer.writerow([lgn_username, lgn_username, receiver_username, amount])

                                                                # Append the transaction index to the sender's transaction history path
                                                                rows[i][7] += f"::{transaction_index}--1"

                                                                # Append the transaction index to the receiver's transaction history path
                                                                receiver_row[7] += f"::{transaction_index}--0"

                                                                # Write the updated data back to the CSV file
                                                                with open("./static/userData.csv", "w", newline='') as file:
                                                                    writer = csv.writer(file)
                                                                    writer.writerows(rows)

                                                                transaction_animation(console)

                                                                success_message = "[bold green]✅ Transaction successful![/bold green]"
                                                                console.print(success_message, justify="center")
                                                                time.sleep(4)

                                            elif final_confirmation == "n" :
                                                print("[bold purple]Transaction canceled[/bold purple]")
                                                time.sleep(2)
                                                break
                                            else :
                                                print("[bold red]Invalid character, Transaction canceled[/bold red]")
                                                time.sleep(2)
                                                break
                                        else :
                                            console.print("[bold red]Incorrect Secret Pin.[/bold red]")

                        except ValueError:
                            console.print("[bold red]Invalid Character. Please enter a number.[/bold red]")
                    
                    elif login_userOperation == 3 :

                        # Create a Table object
                        table = Table(title="My Profile")
                        console.rule("[bold yellow]Profile Page![/bold yellow]", characters="=")

                        # Add columns to the table
                        table.add_column("Username", style="red", justify="center")
                        table.add_column("FirstName", style="magenta")
                        table.add_column("LastName", style="yellow")
                        table.add_column("UPI_Id", style="green")
                        table.add_column("Pin number", style="white")
                        table.add_column("Balance", style="cyan", justify="right")

                        with open("./static/userData.csv", "r") as listProfile:
                            reader = csv.reader(listProfile)
                            next(reader)  # Skip the header
                            for row in reader:
                                # Check if the username matches lgn_username
                                if row[0] == lgn_username:
                                    table.add_row(row[0], row[2], row[3], row[5], row[6], row[4])

                        console.print(table)
                        
                        with open("./static/userData.csv", "r") as listProfile :
                            reader = csv.reader(listProfile)
                            next(reader)  # Skip the header
                            for row in reader:
                                my_profile_loop_flag = True # Flag to control the my profile loop
                                while my_profile_loop_flag :
                                    # Check if Enter is pressed
                                        if keyboard.is_pressed('enter'):
                                            print("Enter pressed! Exiting profile page.")
                                            my_profile_loop_flag = False
                    
                    elif login_userOperation == 4 :
                        table = Table(title="Transaction History")
                        console.rule("[bold yellow]Transaction History![/bold yellow]", characters="=")
                        # Add columns to the table
                        table.add_column("User", style="white", justify="center")
                        table.add_column("Receiver", justify="center")  # Removed the default style for receiver

                        table.add_column("Amount", style="magenta")
                        table.add_column("Type", justify="right")  # Removed the default style

                        with open("./static/transactionHistory.csv", "r") as transaction_file:
                            reader = csv.reader(transaction_file)
                            next(reader)  # Skip the header
                            for row in reader:
                                # Check the length of the row before accessing specific indices
                                if len(row) >= 4:
                                    sender = row[1]
                                    receiver = row[2]
                                    amount = row[3]

                                    # Determine if the user is the sender or receiver
                                    is_sender = lgn_username == sender
                                    is_receiver = lgn_username == receiver

                                    # Only add the transaction to the table if the current user is involved
                                    if is_sender or is_receiver:
                                        # Determine the type of transaction
                                        transaction_type = "Sent" if is_sender else "Received"

                                        # Add the row to the table with the appropriate color for the transaction type
                                        table.add_row(lgn_username, "[cyan]"+receiver+"[/cyan]" if is_sender else "[yellow]"+sender+"[/yellow]", amount, "[red]Sent[/red]" if is_sender else "[green]Received[/green]")

                        transaction_history_loop_flag = True # Flag to control the transaction history loop
                        # Print the transaction history table
                        console.print(table)
                        while transaction_history_loop_flag:
                            # Check if Enter is pressed
                            if keyboard.is_pressed('enter'):
                                print("Enter pressed! Exiting Transaction History.")
                                time.sleep(1)
                                transaction_history_loop_flag = False

                    elif login_userOperation == 5 :
                        console.rule("[bold yellow]Update Profile![/bold yellow]", characters="=")
                        update_data_loop_flag = True # Flag to control the login loop
                        while update_data_loop_flag :
                            print("[bold blue]1 = Username\n 2 = FirstName\n 3 = LastName\n 4 = UPI Id\n 5 = Pin\n 6 = Back\n7 = Exit[/bold blue]")
                            update_userOperation = int(input("Enter operation : "))
                            if update_userOperation == 1 :
                                        new_username = get_non_empty_input("Enter Username: ")

                                        if username_exists(new_username):
                                            console.print("[bold red]Username already exists.[/bold red]")
                                            time.sleep(2)
                                        else:
                                            #--------------------Transaction History.csv--------
                                            # Read the existing data
                                            with open("./static/transactionHistory.csv", "r") as updateUsernameFile:
                                                reader = csv.DictReader(updateUsernameFile)
                                                data = list(reader)

                                            # Update the data
                                            for row in data:

                                                if row['username'] == lgn_username:
                                                    row['username'] = new_username
                                                if row['reciever_id'] == lgn_username:
                                                    row['reciever_id'] = new_username
                                                if row['sender_id'] == lgn_username:
                                                    row['sender_id'] = new_username

                                            # Write the updated data
                                            with open("./static/transactionHistory.csv", "w", newline='') as updateUsernameFile:
                                                fieldnames = data[0].keys()
                                                writer = csv.DictWriter(updateUsernameFile, fieldnames=fieldnames)
                                                writer.writeheader()
                                                writer.writerows(data)


                                                #--------------------userData.csv--------
                                            # Read the existing data
                                            with open("./static/UserData.csv", "r") as updateUsernameFile:
                                                reader = csv.DictReader(updateUsernameFile)
                                                data = list(reader)

                                            # Update the data
                                            for row in data:
                                                if row['username'] == lgn_username:
                                                    row['username'] = new_username

                                            # Write the updated data
                                            with open("./static/UserData.csv", "w", newline='') as updateUsernameFile:
                                                fieldnames = data[0].keys()
                                                writer = csv.DictWriter(updateUsernameFile, fieldnames=fieldnames)
                                                writer.writeheader()
                                                writer.writerows(data)

                                            console.print("[bold green]Username updated successfully.[/bold green]")
                                            time.sleep(2) 
                            
                            elif update_userOperation == 2 :
                                new_firstname = get_non_empty_input("Enter FirstName: ")
                                # Read the existing data
                                with open("./static/UserData.csv", "r") as updateUsernameFile:
                                    reader = csv.DictReader(updateUsernameFile)
                                    data = list(reader)

                                # Update the data
                                for row in data:
                                    if row['username'] == lgn_username:
                                        row['first_name'] = new_firstname

                                # Write the updated data
                                with open("./static/UserData.csv", "w", newline='') as updateUsernameFile:
                                    fieldnames = data[0].keys()
                                    writer = csv.DictWriter(updateUsernameFile, fieldnames=fieldnames)
                                    writer.writeheader()
                                    writer.writerows(data)

                                console.print("[bold green]Firstname updated successfully.[/bold green]")
                                time.sleep(2) 
                            
                            elif update_userOperation == 3 :
                                new_lastname = get_non_empty_input("Enter LastName: ")
                                # Read the existing data
                                with open("./static/UserData.csv", "r") as updateUsernameFile:
                                    reader = csv.DictReader(updateUsernameFile)
                                    data = list(reader)

                                # Update the data
                                for row in data:
                                    if row['username'] == lgn_username:
                                        row['last_name'] = new_lastname

                                # Write the updated data
                                with open("./static/UserData.csv", "w", newline='') as updateUsernameFile:
                                    fieldnames = data[0].keys()
                                    writer = csv.DictWriter(updateUsernameFile, fieldnames=fieldnames)
                                    writer.writeheader()
                                    writer.writerows(data)

                                console.print("[bold green]Lastname updated successfully.[/bold green]")
                                time.sleep(2) 

                            elif update_userOperation == 4 :
                                new_upi_id = generate_random_string(20)
                                if UPI_id_exists(new_upi_id):
                                    new_upi_id = generate_random_string(20)
                                    continue
                                else :
                                    # Read the existing data
                                    with open("./static/UserData.csv", "r") as updateUPI_idFile:
                                        reader = csv.DictReader(updateUPI_idFile)
                                        data = list(reader)

                                    # Update the data
                                    for row in data:
                                        if row['username'] == lgn_username:
                                            row['upi_id'] = new_upi_id

                                    # Write the updated data
                                    with open("./static/UserData.csv", "w", newline='') as updateUsernameFile:
                                        fieldnames = data[0].keys()
                                        writer = csv.DictWriter(updateUsernameFile, fieldnames=fieldnames)
                                        writer.writeheader()
                                        writer.writerows(data)

                                    console.print("[bold green]UPI Id updated successfully.[/bold green]")
                                    time.sleep(2) 
                                # four_digit_pin = random.randint(1000, 9999)

                            elif update_userOperation == 5 :
                                def get_new_secret_pin_input(prompt):
                                    while True:
                                        user_input = input(prompt)
                                        if user_input.strip():  # Check if input is not empty after stripping whitespace
                                            if len(user_input) != 4 :
                                                console.print("[bold red]Pin should be 4 digit.[/bold red]")
                                            else :
                                                return user_input
                                        else:
                                            console.print("[bold red]Input cannot be empty. Please try again.[/bold red]")

                                new_secret_pin = get_new_secret_pin_input("Enter new Secret Pin: ")
                                # Read the existing data
                                with open("./static/UserData.csv", "r") as updateUsernameFile:
                                    reader = csv.DictReader(updateUsernameFile)
                                    data = list(reader)

                                # Update the data
                                for row in data:
                                    if row['username'] == lgn_username:
                                        row['pin'] = new_secret_pin

                                # Write the updated data
                                with open("./static/UserData.csv", "w", newline='') as updateUsernameFile:
                                    fieldnames = data[0].keys()
                                    writer = csv.DictWriter(updateUsernameFile, fieldnames=fieldnames)
                                    writer.writeheader()
                                    writer.writerows(data)

                                console.print("[bold green]Secret Pin updated successfully.[/bold green]")
                                time.sleep(2) 

                            elif update_userOperation == 6 :
                                os.system('cls' if os.name == 'nt' else 'clear')
                                update_data_loop_flag = False  # Set the flag to exit the update data loop
                                break

                            elif update_userOperation == 7 :
                                os.system('cls' if os.name == 'nt' else 'clear')
                                outer_loop_flag = False  # Set the flag to exit both loops
                                login_loop_flag = False  # Set the flag to exit the inner loop
                                update_data_loop_flag = False  # Set the flag to exit the update data loop
                                break

                    elif login_userOperation == 6:
                        # Function to display folder options and get user input
                        def display_and_choose_folder(root_path):
                            fetched_root_dir_items = os.listdir(root_path)

                            for index, second_stage_path in enumerate(fetched_root_dir_items, start=1):
                                path_with_forward_slashes = os.path.join(root_path, second_stage_path).replace('\\', '/')
                                _, extension = os.path.splitext(second_stage_path)
                                if extension.lower() in ['.svg', '.jpg', '.png']:
                                    console.print(f"[bold green]{index}= {path_with_forward_slashes}", style="bold green")
                                else:
                                    console.print(f"[bold cyan]{index}= {path_with_forward_slashes}", style="bold cyan")

                            second_stage_choosed = input("Enter which folder to select (or press Enter to go back): ")
                            if second_stage_choosed == '':
                                return 'BACK'  # Go back if Enter was pressed
                            second_stage_choosed = int(second_stage_choosed) - 1
                            if 0 <= second_stage_choosed < len(fetched_root_dir_items):
                                selected_item_path = os.path.join(root_path, fetched_root_dir_items[second_stage_choosed]).replace('\\', '/')
                                if selected_item_path.lower().endswith(('.jpg', '.png', '.svg')):
                                    image_path_to_safe = selected_item_path
                                    selected_item_path = os.path.dirname(selected_item_path)
                                    console.print(f"[bold red]Selected item path: {image_path_to_safe}[/bold red]", style="bold red")

                                    # Read the existing data
                                    with open("./static/UserData.csv", "r") as AddItemsToSafeFile:
                                        reader = csv.DictReader(AddItemsToSafeFile)
                                        data = list(reader)

                                    # find safe name
                                    for row in data:
                                        if row["username"] == lgn_username:
                                            #'safe_root' is a subdirectory in the current working directory
                                            safe_root_directory = os.path.join(os.getcwd(), 'safe_root')

                                            # Assuming 'safe_name' is obtained from the row in your data
                                            safe_name = row["safe_name"]

                                            # Construct the complete path to the safe directory
                                            complete_path_to_safe = os.path.join(safe_root_directory, safe_name)
                                            shutil.copy(image_path_to_safe, complete_path_to_safe)
                                            time.sleep(2)
                                            folder_path = r"C:\Users\Aliasger B\1001_ai\1001_ai_python\Core_python\bank\safe_root"
                                            target_folder_name = safe_name
                                            find_and_right_click(folder_path, target_folder_name)
                                            
                                    # Open the File Explorer
                                    # subprocess.Popen(f'explorer "{newName}"')
                                # else:
                                #     print("Selected item is not an image.")
                                return selected_item_path
                            else:
                                print("Invalid folder index.")
                                return None


                        user_drive_letter = input("Enter the drive letter (e.g., C): ").upper()

                        # Validate the input to make sure it's a valid drive letter
                        if user_drive_letter.isalpha() and len(user_drive_letter) == 1:
                            root_path = f"{user_drive_letter.upper()}:\\"
                            path_stack = [root_path]
                            while path_stack:
                                root_path = path_stack[-1]
                                new_path = display_and_choose_folder(root_path)
                                if new_path == 'BACK':
                                    path_stack.pop()  # Go back to the previous directory
                                elif new_path is not None:
                                    path_stack.append(new_path)
                                time.sleep(3)
                        else:
                            console.print("[bold red]Invalid drive letter. Please enter a single alphabetical character.[/bold red]")
                            time.sleep(2)

                    
                    elif login_userOperation == 7 :
                        os.system('cls' if os.name == 'nt' else 'clear')
                        login_loop_flag = False  # Set the flag to exit both loops
                        
                    elif login_userOperation == 8 :
                        os.system('cls' if os.name == 'nt' else 'clear')
                        outer_loop_flag = False  # Set the flag to exit both loops
                        login_loop_flag = False  # Set the flag to exit the inner loop

                except ValueError:
                    console.print("[bold red]Invalid operation. Please enter a number.[/bold red]")

        elif userOperation == 3 :
            os.system('cls' if os.name == 'nt' else 'clear')
            outer_loop_flag = False  # Set the flag to exit both loops

        else :
            os.system('cls' if os.name == 'nt' else 'clear')  # This line clears the terminal

            print("[bold red]Invalid operation[/bold red]")

    except ValueError:
        console.print("[bold red]Invalid operation. Please enter a number.[/bold red]")
