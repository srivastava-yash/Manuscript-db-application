from author import author
from editor import editor
from reviewer import reviewer
import constants
from db import DB

class main:

    def __init__(self):
        self.db = DB()
        self.author = author(self.db)
        self.editor = editor(self.db)
        self.reviewer = reviewer(self.db)


if __name__ == "__main__":
    main = main()
    while True:
        input_str = input("Enter command(exit or quit to close application): ")

        if input_str == constants.EXIT or input_str == constants.QUIT:
            break
        input_str.replace('"', '')
        input_arr = input_str.split(" ")

        ## register author
        if input_str.startswith(constants.REGISTER_AUTHOR):
            if len(input_arr) < 6:
                print(constants.INVALID_COMMAND)

            else:
                print("Unique ID:", main.author.register_author(input_arr[2],input_arr[3],input_arr[4],input_arr[5]))

        ## register reviewer
        elif input_str.startswith(constants.REGISTER_REVIEWER):
            if len(input_arr) < 7:
                print(constants.INVALID_COMMAND)

            else:
                icodes = input_arr[-3:]
                print("Unique ID:", main.reviewer.register_reviewer(input_arr[2],input_arr[3], icodes))

        ## register editor
        elif input_str.startswith(constants.REGISTER_EDITOR):
            if len(input_arr) < 4:
                print(constants.INVALID_COMMAND)
            else:
                print("Unique ID:", main.editor.register_editor(input_arr[2], input_arr[3]))

        ## login commands
        elif input_str.startswith(constants.LOGIN):
            main.author.logout()
            main.reviewer.logout()
            is_author = main.author.is_author(int(input_arr[1]))
            if is_author:
                print(main.author.login(main.author.get_author_id(int(input_arr[1])),int(input_arr[1])))

            elif main.reviewer.is_reviewer(int(input_arr[1])):
                print(main.reviewer.login(int(main.reviewer.get_reviewer_id(int(input_arr[1])))))

            elif main.editor.is_editor(int(input_arr[1])):
                print(main.editor.login(int(input_arr[1])))

            else:
                print("INVALID USER")

        ## status commands
        elif input_str.startswith(constants.STATUS):
            author_status = main.author.get_status(None)
            if len(author_status) > 0:
                print(author_status)
            else:
                print(main.editor.get_status())

        ## submit manuscript
        elif input_str.startswith(constants.SUBMIT):
            manuscript_id = main.author.submit_manuscript(input_arr)
            if manuscript_id == -1:
                print("Server Error. Please try again")
            else:
                print("Manuscript Submitted with id:", manuscript_id)

        ## accept reject recommendation command for reviewer
        elif input_str.startswith(constants.ACCEPT) or input_str.startswith(constants.REJECT):
            if len(input_arr) > 2:
                scores = input_arr[-4:]
                print(main.reviewer.accept_reject_manuscript(input_arr[1], scores))
            else:
                if input_str.startswith(constants.ACCEPT):
                    print("Manuscript accepted, ID:", main.editor.accept(input_arr[1]))
                else:
                    print("Manuscript rejected, ID:", main.editor.reject(input_arr[1]))

        elif input_str.startswith(constants.ASSIGN):
            main.editor.assign_reviewer(input_arr[1],input_arr[2])
            print("Manuscript Assigned")

        elif input_str.startswith(constants.SCHEDULE):
            print("Manuscript scheduled, ID:", main.editor.schedule(input_arr[1], input_arr[2]))

        elif input_str.startswith(constants.PUBLISH):
            print(f"Issue {main.editor.publish(input_arr[1])} Published")

        elif input_str.startswith(constants.RESET):
            main.editor.reset()
            print("Database Reset")

        else:
            print("Unknown Command. Please enter the right command or type 'quit' or 'exit' to exit program")





    main.db.close_connection()
