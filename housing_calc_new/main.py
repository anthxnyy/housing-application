"""
Filename: main.py
Author: Anthony Toyco
Date: Monday March 6, 2023
Description: A program that calculates the user's housing score.
Note: Read the requirements.txt file for the required modules.
"""

import typing as t

import customtkinter as ct
import questions as q
from PIL import Image

# CLASSES


# Class that stores all the fonts used
class Fonts:
    @staticmethod
    def get_font(key: str) -> ct.CTkFont:
        FONTS = {
            "MAIN_TEXT_FONT": ct.CTkFont(family="Helvetica", size=15),
            "QUESTION_TEXT_FONT": ct.CTkFont(family="Helvetica", size=20),
            "TEXT_FONT_S25": ct.CTkFont(
                family="Helvetica", size=25, weight="bold"
            ),
            "TEXT_FONT_S15": ct.CTkFont(family="Helvetica", size=20),
        }
        return FONTS[key]


# Class that stores all the data for the student
class StudentData:
    credits: int = 0
    points: int = 0
    question_history: list = []
    points_history: list = []


# The main app class
class App(ct.CTk):
    def __init__(self) -> None:
        super().__init__()
        # Setup the frame
        ct.set_appearance_mode("dark")
        ct.set_default_color_theme("dark-blue")
        self.geometry(f"{900}x{600}")
        self.resizable(False, False)
        self.title("Mary Ward University")

        # Initialize the this page as the first page
        self.current_page = None
        # Go to the start page
        self.replace_frame(StartPage),

    # Function that replaces the current frame with a new one
    def replace_frame(self, new_page: t.Type[ct.CTkFrame]) -> None:
        if self.current_page is not None:
            self.current_page.destroy()
        self.current_page = new_page(self)
        self.current_page.pack()


# Class that stores the first page
class StartPage(ct.CTkFrame):
    def __init__(self, master) -> None:
        super().__init__(master)
        # Setup the frame
        self.grid_rowconfigure((0, 1, 2), weight=1)
        self.grid_columnconfigure((0, 1, 2), weight=1)

        # Create the widgets
        self.create_widgets()
        # Display the widgets
        self.display_widgets()

    # Function that creates the widgets
    def create_widgets(self) -> None:
        # Create the background image
        self.start_bg_file = ct.CTkImage(
            light_image=Image.open("housing_calc_new/assets/background.png"),
            dark_image=Image.open("housing_calc_new/assets/background.png"),
            size=(1800, 700),
        )
        self.start_bg = ct.CTkLabel(self, text="", image=self.start_bg_file)
        # Create the frame that holds the widgets
        self.content_frame = ct.CTkFrame(self)
        self.content_frame.grid_rowconfigure((0, 1, 2), weight=1)
        # Create the logo image
        self.logo = ct.CTkImage(
            light_image=Image.open("housing_calc_new/assets/logo.png"),
            dark_image=Image.open("housing_calc_new/assets/logo.png"),
            size=(125, 125),
        )
        self.logo_label = ct.CTkLabel(
            self.content_frame,
            height=125,
            text="",
            image=self.logo,
        )
        # Create the title text
        self.title_text = ct.CTkLabel(
            self.content_frame,
            text="Mary Ward University\nHousing Calculator",
            font=Fonts.get_font("TEXT_FONT_S25"),
        )
        # Create the body text
        self.body_text = ct.CTkLabel(
            self.content_frame,
            text=(
                "\nWelcome to the MWU Housing Calculator"
                "\nPress the start button to login\n"
            ),
            font=Fonts.get_font("MAIN_TEXT_FONT"),
        )
        # Create the start button
        self.start_button = ct.CTkButton(
            self.content_frame,
            height=30,
            width=150,
            text="START",
            font=Fonts.get_font("TEXT_FONT_S15"),
            command=lambda: self.master.replace_frame(LoginPage),
        )

    # Function that displays the widgets
    def display_widgets(self) -> None:
        self.start_bg.grid(row=0, column=0, columnspan=3, rowspan=3)
        self.content_frame.grid(row=0, column=1, rowspan=3, sticky="NS")
        self.logo_label.grid(row=0, column=0)
        self.title_text.grid(row=1, column=0, sticky="N")
        self.body_text.grid(row=2, column=0, ipadx=50, sticky="N")
        self.start_button.grid(row=3, column=0, pady=(0, 50))


# Class that allows the user to login
class LoginPage(ct.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        # Setup the frame
        self.grid_rowconfigure((0, 1, 2), weight=1)
        self.grid_columnconfigure((0, 1, 2), weight=1)

        # Create the widgets
        self.create_widgets()
        # Display the widgets
        self.display_widgets()

    # Function that creates the widgets
    def create_widgets(self):
        # Create the background image
        self.start_bg_file = ct.CTkImage(
            light_image=Image.open("housing_calc_new/assets/background.png"),
            dark_image=Image.open("housing_calc_new/assets/background.png"),
            size=(1800, 700),
        )
        self.start_bg = ct.CTkLabel(self, text="", image=self.start_bg_file)
        # Create the frame that holds the widgets
        self.content_frame = ct.CTkFrame(self)
        self.content_frame.grid_rowconfigure((0, 1, 2), weight=1)
        self.content_frame.grid_columnconfigure((0, 1, 2), weight=1)
        # Create the title text
        self.title_text = ct.CTkLabel(
            self.content_frame,
            text="Login",
            font=Fonts.get_font("TEXT_FONT_S25"),
        )
        # Create the entry box for the username
        self.username_entry = ct.CTkEntry(
            self.content_frame, width=200, placeholder_text="Username"
        )
        # Create the entry box for the password
        self.password_entry = ct.CTkEntry(
            self.content_frame, width=200, show="*", placeholder_text="Password"
        )
        # Create the submit button
        self.submit_button = ct.CTkButton(
            self.content_frame,
            text="SUBMIT",
            command=lambda: self.verify_input(
                self.username_entry.get(), self.password_entry.get()
            ),
            width=200,
            font=Fonts.get_font("TEXT_FONT_S15"),
        )
        # Create the error label
        self.username_error = ct.CTkLabel(
            self.content_frame,
            text="ERROR: Enter valid credentials!",
            text_color="#FF0000",
            font=Fonts.get_font("MAIN_TEXT_FONT"),
        )

    # Function that displays the widgets
    def display_widgets(self):
        self.start_bg.grid(row=0, column=0, columnspan=3, rowspan=3)
        self.content_frame.grid(row=0, column=1, rowspan=3, sticky="NS")
        self.title_text.grid(row=0, column=0, sticky="NSEW", pady=(50, 0))
        self.username_entry.grid(row=1, column=0, padx=30)
        self.password_entry.grid(row=2, column=0, padx=30, sticky="N")
        self.submit_button.grid(row=3, column=0, pady=(0, 50))

    # Function that verifies the inputs of the username and password entry boxes
    def verify_input(self, username: str, password: str) -> None:
        try:
            # If there are strings in the username and password entry boxes
            if username and password:
                # If valid, delete the error box
                self.username_error.grid_forget()
                # Go to the question pages
                self.master.replace_frame(CreditInputPage)
            else:
                raise ValueError
        except ValueError:
            self.username_error.grid(row=2, column=0, columnspan=3)


# Class that stores the page where the user inputs their credits
class CreditInputPage(ct.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        # Setup the frame
        self.grid_rowconfigure((0, 1, 2), weight=1)
        self.grid_columnconfigure((0, 1, 2), weight=1)

        # Create the widgets
        self.create_widgets()
        # Display the widgets
        self.display_widgets()

    # Function that creates the widgets
    def create_widgets(self) -> None:
        # Create the background image
        self.bg_file = ct.CTkImage(
            light_image=Image.open("housing_calc_new/assets/gradient.png"),
            dark_image=Image.open("housing_calc_new/assets/gradient.png"),
            size=(1800, 700),
        )
        self.bg = ct.CTkLabel(self, text="", image=self.bg_file)
        # Create the frame that holds the widgets
        self.content_frame = ct.CTkFrame(self)
        self.content_frame.grid_rowconfigure((0, 1, 2), weight=1)
        self.content_frame.grid_columnconfigure((0, 1, 2), weight=1)
        # Create the question text
        self.question_title = ct.CTkLabel(
            self.content_frame,
            text="How many credits do you currently have?",
            font=Fonts.get_font("TEXT_FONT_S25"),
        )
        # Create the title of the input box
        self.input_box_title = ct.CTkLabel(
            self.content_frame,
            text="Enter an integer below\n",
            font=Fonts.get_font("MAIN_TEXT_FONT"),
        )
        # Create the entry box for the credits
        self.input_box = ct.CTkEntry(
            self.content_frame,
            font=Fonts.get_font("MAIN_TEXT_FONT"),
            width=200,
            placeholder_text="Number",
        )
        # Create the error label
        self.input_box_error = ct.CTkLabel(
            self.content_frame,
            text="ERROR: Please enter a valid number!",
            text_color="#FF0000",
            font=Fonts.get_font("MAIN_TEXT_FONT"),
        )
        # Create the submit button
        self.submit = ct.CTkButton(
            self.content_frame,
            text="SUBMIT",
            hover_color="#001B4B",
            font=Fonts.get_font("TEXT_FONT_S15"),
            command=lambda: [
                self.input_box_error.forget(),
                self.verify_input(self.input_box.get()),
            ],
        )

    # Function that displays the widgets
    def display_widgets(self) -> None:
        self.bg.grid(row=0, column=0, columnspan=3, rowspan=3)
        self.content_frame.grid(row=0, column=1, rowspan=3, sticky="NS")
        self.question_title.grid(
            row=0, column=0, columnspan=3, pady=(50, 0), padx=50, sticky="S"
        )
        self.input_box_title.grid(
            row=1, column=0, columnspan=3, sticky="N", pady=(50, 10)
        )
        self.input_box.grid(row=1, column=0, columnspan=3, pady=(0, 10))
        self.submit.grid(row=2, column=0, columnspan=3, pady=10, sticky="N")

    # Function that verifies the input in the input box
    def verify_input(self, user_entry: int) -> None:
        try:
            if (1 <= float(user_entry) <= 40) and (
                float(user_entry) % 0.5 == 0
            ):
                # If valid, delete the error box
                self.input_box_error.grid_forget()
                # Store the number of credits
                StudentData.credits = user_entry
                # Go to the question pages
                self.master.replace_frame(QuestionPage)
            else:
                raise ValueError
        except ValueError:
            self.input_box_error.grid(
                row=1, column=0, columnspan=3, sticky="S", pady=(0, 30)
            )


# Class that stores the questions
class QuestionPage(ct.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        # Setup the frame
        self.grid_rowconfigure((0, 1, 2), weight=1)
        self.grid_columnconfigure((0, 1, 2), weight=1)

        # Create the widgets
        self.create_widgets()
        # Display the widgets
        self.display_widgets()
        # Change to the first question
        self.next_question("q1p1")

    # Function that creates the widgets
    def create_widgets(self) -> None:
        # Create the background image
        self.bg_file = ct.CTkImage(
            light_image=Image.open("housing_calc_new/assets/gradient.png"),
            dark_image=Image.open("housing_calc_new/assets/gradient.png"),
            size=(1800, 700),
        )
        self.bg = ct.CTkLabel(self, text="", image=self.bg_file)
        # Create the frame that holds the widgets
        self.content_frame = ct.CTkFrame(self)
        self.content_frame.grid_rowconfigure((0, 1, 2, 3), weight=1)
        self.content_frame.grid_columnconfigure((0, 1, 2), weight=1)
        # Title widget
        self.title = ct.CTkLabel(
            self.content_frame,
            text="text for title",
            font=Fonts.get_font("TEXT_FONT_S25"),
        )
        # Half buttons widgets
        self.b_left_half = ct.CTkButton(
            self.content_frame,
            hover_color="#001B4B",
            font=Fonts.get_font("TEXT_FONT_S15"),
            width=250,
            height=100,
        )
        self.b_right_half = ct.CTkButton(
            self.content_frame,
            hover_color="#001B4B",
            font=Fonts.get_font("TEXT_FONT_S15"),
            width=250,
            height=100,
        )
        # Third buttons widgets
        self.b_left_third = ct.CTkButton(
            self.content_frame,
            hover_color="#001B4B",
            font=Fonts.get_font("TEXT_FONT_S15"),
            width=250,
            height=100,
        )
        self.b_middle_third = ct.CTkButton(
            self.content_frame,
            hover_color="#001B4B",
            font=Fonts.get_font("TEXT_FONT_S15"),
            width=250,
            height=100,
        )
        self.b_right_third = ct.CTkButton(
            self.content_frame,
            hover_color="#001B4B",
            font=Fonts.get_font("TEXT_FONT_S15"),
            width=250,
            height=100,
        )
        # Quarter buttons widgets
        self.b_top_left = ct.CTkButton(
            self.content_frame,
            hover_color="#001B4B",
            font=Fonts.get_font("TEXT_FONT_S15"),
            width=250,
            height=100,
        )
        self.b_top_right = ct.CTkButton(
            self.content_frame,
            hover_color="#001B4B",
            font=Fonts.get_font("TEXT_FONT_S15"),
            width=250,
            height=100,
        )
        self.b_bot_left = ct.CTkButton(
            self.content_frame,
            hover_color="#001B4B",
            font=Fonts.get_font("TEXT_FONT_S15"),
            width=250,
            height=100,
        )
        self.b_bot_right = ct.CTkButton(
            self.content_frame,
            hover_color="#001B4B",
            font=Fonts.get_font("TEXT_FONT_S15"),
            width=250,
            height=100,
        )
        # Back button widget
        self.back_button = ct.CTkButton(
            self.content_frame,
            text="BACK",
            hover_color="#001B4B",
            font=Fonts.get_font("TEXT_FONT_S15"),
            command=lambda: [back_button_event()],
        )

        # Function for when the back button is clicked
        @staticmethod
        def back_button_event() -> None:
            # Removes the contents of the current question
            self.forget_widgets("all")
            if len(StudentData.points_history) >= 2:
                # True when the user has answered at least 2 questions
                StudentData.points -= StudentData.points_history[-1]
                StudentData.points_history.pop()
            else:
                # True when the user has answered only 1 question
                StudentData.points -= StudentData.points_history[0]
                StudentData.points_history = []
            # Remove the current question from the history
            StudentData.question_history.pop()
            # Change to the previous question
            self.next_question(StudentData.question_history[-1])
            # Remove the question from the history
            StudentData.question_history.pop()

    # Function that displays the widgets
    def display_widgets(self) -> None:
        self.bg.grid(row=0, column=0, columnspan=3, rowspan=3)
        self.content_frame.grid(
            row=0, column=0, columnspan=3, rowspan=3, sticky="EW", ipady=100
        )

    # Function that changes to the next question
    def next_question(self, question_name: str) -> None:
        # If the question is not the final question
        if question_name != "END":
            # Add the question to the history
            StudentData.question_history.append(question_name)
            # Change widgets to the next question
            self.config_questions(question_name)
            self.display_questions(question_name)
            self.display_back_button(question_name)
        else:
            # If the question is the final question
            # Go to the results page
            self.master.replace_frame(ResultsPage)

    # Function that displays the questions
    def display_questions(self, question_name: str) -> None:
        if q.questions[question_name]["button_cnt"] == 2:
            # If the question requires 2 buttons
            self.b_left_half.grid(row=1, column=0)
            self.b_right_half.grid(row=1, column=2)
        elif q.questions[question_name]["button_cnt"] == 3:
            # If the question requires 3 buttons
            self.b_left_third.grid(row=1, column=0)
            self.b_middle_third.grid(row=1, column=1)
            self.b_right_third.grid(row=1, column=2)
        elif q.questions[question_name]["button_cnt"] == 4:
            # If the question requires 4 buttons
            self.b_top_left.grid(row=1, column=0)
            self.b_top_right.grid(row=1, column=2)
            self.b_bot_left.grid(row=2, column=0)
            self.b_bot_right.grid(row=2, column=2)

    # Function that displays the back button
    def display_back_button(self, question_name: str) -> None:
        # If the question is the first question or the final question
        # Do not display the back button
        if (question_name == "q1p1") or (question_name == "END"):
            self.back_button.grid_forget()
        else:
            # If the question is not the first question or the final question
            # Display the back button
            self.back_button.grid(row=3, column=1, sticky="S", pady=(0, 30))

    # Function that changes the text and commands of the buttons
    def config_questions(self, question_name: str) -> None:
        # Change the title of the question
        self.title.configure(text=q.questions[question_name]["prompt"])
        self.title.grid(row=0, column=0, columnspan=3, pady=(30, 0))
        # Change the text and points awarded for each button
        # Half button setup
        if q.questions[question_name]["button_cnt"] == 2:
            self.b_left_half.configure(
                text=q.questions[question_name]["button_text"][0],
                command=lambda: [
                    self.forget_widgets(2),
                    self.change_points(
                        q.questions[question_name]["button_values"][0]
                    ),
                    self.next_question(
                        q.questions[question_name]["next_question"][0]
                    ),
                ],
            )
            self.b_right_half.configure(
                text=q.questions[question_name]["button_text"][1],
                command=lambda: [
                    self.forget_widgets(2),
                    self.change_points(
                        q.questions[question_name]["button_values"][1]
                    ),
                    self.next_question(
                        q.questions[question_name]["next_question"][1]
                    ),
                ],
            )
        # Third button setup
        elif q.questions[question_name]["button_cnt"] == 3:
            self.b_left_third.configure(
                text=q.questions[question_name]["button_text"][0],
                command=lambda: [
                    self.forget_widgets(3),
                    self.change_points(
                        q.questions[question_name]["button_values"][0]
                    ),
                    self.next_question(
                        q.questions[question_name]["next_question"][0]
                    ),
                ],
            )
            self.b_middle_third.configure(
                text=q.questions[question_name]["button_text"][1],
                command=lambda: [
                    self.forget_widgets(3),
                    self.change_points(
                        q.questions[question_name]["button_values"][1]
                    ),
                    self.next_question(
                        q.questions[question_name]["next_question"][1]
                    ),
                ],
            )
            self.b_right_third.configure(
                text=q.questions[question_name]["button_text"][2],
                command=lambda: [
                    self.forget_widgets(3),
                    self.change_points(
                        q.questions[question_name]["button_values"][2]
                    ),
                    self.next_question(
                        q.questions[question_name]["next_question"][2]
                    ),
                ],
            )
        # Quarter button setup
        elif q.questions[question_name]["button_cnt"] == 4:
            self.b_top_left.configure(
                text=q.questions[question_name]["button_text"][0],
                command=lambda: [
                    self.forget_widgets(4),
                    self.change_points(
                        q.questions[question_name]["button_values"][0]
                    ),
                    self.next_question(
                        q.questions[question_name]["next_question"][0]
                    ),
                ],
            )
            self.b_top_right.configure(
                text=q.questions[question_name]["button_text"][1],
                command=lambda: [
                    self.forget_widgets(4),
                    self.change_points(
                        q.questions[question_name]["button_values"][1]
                    ),
                    self.next_question(
                        q.questions[question_name]["next_question"][1]
                    ),
                ],
            )
            self.b_bot_left.configure(
                text=q.questions[question_name]["button_text"][2],
                command=lambda: [
                    self.forget_widgets(4),
                    self.change_points(
                        q.questions[question_name]["button_values"][2]
                    ),
                    self.next_question(
                        q.questions[question_name]["next_question"][2]
                    ),
                ],
            )
            self.b_bot_right.configure(
                text=q.questions[question_name]["button_text"][3],
                command=lambda: [
                    self.forget_widgets(4),
                    self.change_points(
                        q.questions[question_name]["button_values"][3]
                    ),
                    self.next_question(
                        q.questions[question_name]["next_question"][3]
                    ),
                ],
            )

    # Function that forgets the widgets
    def forget_widgets(self, widget_cnt: int) -> None:
        # Initialize the list of widgets to forget
        widgets = [self.title]
        # Half button setup
        if (widget_cnt == 2) or (widget_cnt == "all"):
            widgets.extend(
                [
                    self.b_left_half,
                    self.b_right_half,
                ]
            )
        # Third button setup
        if (widget_cnt == 3) or (widget_cnt == "all"):
            widgets.extend(
                [
                    self.b_left_third,
                    self.b_middle_third,
                    self.b_right_third,
                ]
            )
        # Quarter button setup
        if (widget_cnt == 4) or (widget_cnt == "all"):
            widgets = [
                self.title,
                self.b_top_left,
                self.b_top_right,
                self.b_bot_left,
                self.b_bot_right,
            ]
        # Forget all widgets
        if widget_cnt == "all":
            widgets.append(self.back_button)
        # Loop through the list of widgets and forget them
        for widget in widgets:
            widget.grid_forget()

    # Function that changes the points of the user based on the button pressed
    def change_points(self, value: int) -> None:
        StudentData.points_history.append(value)
        StudentData.points += value


# Class that displays the results to the user
class ResultsPage(ct.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        # Setup the frame
        self.grid_rowconfigure((0, 1, 2), weight=1)
        self.grid_columnconfigure((0, 1, 2), weight=1)

        # Create the widgets
        self.create_widgets()
        # Display the widgets
        self.display_widgets()

    # Function that creates the widgets
    def create_widgets(self) -> None:
        # Create the background image
        self.start_bg_file = ct.CTkImage(
            light_image=Image.open("housing_calc_new/assets/background.png"),
            dark_image=Image.open("housing_calc_new/assets/background.png"),
            size=(1800, 700),
        )
        self.start_bg = ct.CTkLabel(self, text="", image=self.start_bg_file)
        # Create the frame that holds the widgets
        self.content_frame = ct.CTkFrame(self)
        self.content_frame.grid_rowconfigure((0, 1, 2, 3), weight=1)
        self.content_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)
        # Creates the logo
        self.logo = ct.CTkImage(
            light_image=Image.open("housing_calc_new/assets/logo.png"),
            dark_image=Image.open("housing_calc_new/assets/logo.png"),
            size=(150, 150),
        )
        self.logo_label = ct.CTkLabel(
            self.content_frame, text="", image=self.logo
        )
        # Creates the text
        self.main_text = ct.CTkLabel(
            self.content_frame,
            text=(
                "Your information has been successfully submitted."
                "\nPlease check your email for your results"
                "\nThank you for using the MWU Housing Calculator."
            ),
            font=Fonts.get_font("TEXT_FONT_S15"),
        )
        # Creates the points text
        self.points_text = ct.CTkLabel(
            self.content_frame,
            text=f"Your points: {round(StudentData.points, 1)}",
            font=Fonts.get_font("TEXT_FONT_S15"),
        )
        # Creates the restart button
        self.restart_button = ct.CTkButton(
            self.content_frame,
            text="RESTART",
            command=lambda: [
                self.master.replace_frame(StartPage),
            ],
            font=Fonts.get_font("TEXT_FONT_S15"),
        )

    # Function that displays the widgets
    def display_widgets(self) -> None:
        self.start_bg.grid(row=0, column=0, columnspan=3, rowspan=3)
        self.content_frame.grid(row=0, column=1, rowspan=3, sticky="NS")
        self.logo_label.grid(row=0, column=1, pady=(50, 0))
        self.main_text.grid(
            row=1, column=0, columnspan=3, padx=(50, 50), sticky="NS"
        )
        self.points_text.grid(row=2, column=0, columnspan=3)
        self.restart_button.grid(row=3, column=1)


# MAIN PROGRAM


if __name__ == "__main__":
    app = App()
    app.mainloop()
