"""
Filename: MWU_Housing_Calculator.py
Author: Anthony Toyco
Date: Monday March 6, 2023
Description: A program that calculates the housing score for the user
at Mary Ward University
"""

import customtkinter as ct
import questions as q
from PIL import Image


# CLASSES


# Class that stores all the fonts used
class Fonts:
    @staticmethod
    def get_font(key):
        FONTS = {
            "MAIN_TEXT_FONT": ct.CTkFont(family="Helvetica", size=15),
            "QUESTION_TEXT_FONT": ct.CTkFont(family="Helvetica", size=20),
            "TITLE_TEXT_FONT_S25": ct.CTkFont(family="Helvetica", size=35),
            "TITLE_TEXT_FONT_S15": ct.CTkFont(family="Helvetica", size=20),
        }
        return FONTS[key]


# Class that stores all the data for the student
class StudentData:
    credits = 0
    points = 0
    question_history = []
    points_history = []


# The main app class
class App(ct.CTk):
    def __init__(self):
        super().__init__()
        # Setup the frame
        ct.set_appearance_mode("dark")
        ct.set_default_color_theme("dark-blue")
        self.geometry(f"{800}x{600}")
        self.title("Mary Ward University - Housing Calculator")

        # Create the logo
        self.logo = ct.CTkImage(
            light_image=Image.open("housing_calc_new/assets/mw_logo.png"),
            dark_image=Image.open("housing_calc_new/assets/mw_logo.png"),
            size=(250, 250),
        )
        self.logo_label = ct.CTkLabel(self, text="", image=self.logo)
        # Display the logo
        self.logo_label.place(relx=0.5, rely=0.5, anchor="center")

        # Initialize the this page as the first page
        self._page = None

        # Go to the next page after 1 second of showing the startup logo
        self.after(
            1000,
            lambda: [
                self.replace_frame(StartPage),
                self.logo_label.destroy(),
            ],
        )

    # Function that replaces the current frame with a new one
    def replace_frame(self, page):
        new_page = page(self)
        if self._page is not None:
            self._page.destroy()
        self._page = new_page
        self._page.pack()


# Class that stores the first page
class StartPage(ct.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        # Setup the frame
        self.configure(fg_color="transparent")
        self.grid_rowconfigure((0, 1, 2, 3), weight=1)
        self.grid_columnconfigure((0, 1, 2), weight=1)

        # Create the widgets
        self.create_widgets(master)
        # Display the widgets
        self.display_widgets()

    # Function that creates the widgets
    def create_widgets(self, master):
        self.logo_label = ct.CTkLabel(self, text="", image=master.logo)
        self.title_text_top = ct.CTkLabel(
            self,
            text="HOUSING SCORE CALCULATOR",
            font=Fonts.get_font("TITLE_TEXT_FONT_S25"),
        )
        self.title_text_under = ct.CTkLabel(
            self,
            text="By Mary Ward University",
            text_color="gray75",
            font=Fonts.get_font("TITLE_TEXT_FONT_S15"),
        )
        self.start_button = ct.CTkButton(
            self,
            width=150,
            height=50,
            text="START",
            hover_color="#001B4B",
            font=Fonts.get_font("TITLE_TEXT_FONT_S15"),
            command=lambda: master.replace_frame(CreditInputPage),
        )

    # Function that displays the widgets
    def display_widgets(self):
        self.logo_label.grid(row=2, column=0, columnspan=3, pady=57)
        self.title_text_top.grid(row=0, column=0, columnspan=3, pady=(50, 0))
        self.title_text_under.grid(row=1, column=0, columnspan=3, pady=(10, 0))
        self.start_button.grid(row=3, column=0, columnspan=3, pady=10)


# Class that allows the user to login
class LoginPage(ct.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        # Setup the frame
        self.configure(fg_color="transparent")


# Class that stores the page where the user inputs their credits
class CreditInputPage(ct.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        # Setup the frame
        self.configure(fg_color="transparent")
        self.grid_rowconfigure((0, 1, 2, 3), weight=1)
        self.grid_columnconfigure((0, 1, 2), weight=1)

        # Create the widgets
        self.create_widgets()
        # Display the widgets
        self.display_widgets()

    # Function that creates the widgets
    def create_widgets(self):
        self.question_title = ct.CTkLabel(
            self,
            text="How many credits do you currently have?",
            font=Fonts.get_font("QUESTION_TEXT_FONT"),
        )
        self.input_box_title = ct.CTkLabel(self, text="Enter an integer below")
        self.input_box = ct.CTkEntry(
            self, font=Fonts.get_font("MAIN_TEXT_FONT")
        )
        self.input_box_error = ct.CTkLabel(
            self,
            text="ERROR: Please enter a valid number!",
            text_color="#FF0000",
            font=Fonts.get_font("MAIN_TEXT_FONT"),
        )
        self.input_button = ct.CTkButton(
            self,
            text="SUBMIT",
            hover_color="#001B4B",
            font=Fonts.get_font("TITLE_TEXT_FONT_S15"),
            command=lambda: [
                self.input_box_error.forget(),
                self.verify_input(self.input_box.get()),
            ],
        )

    # Function that displays the widgets
    def display_widgets(self):
        self.question_title.grid(row=0, column=0, columnspan=3, pady=(50, 0))
        self.input_box_title.grid(
            row=1, column=0, columnspan=3, sticky="S", pady=(50, 10)
        )
        self.input_box.grid(row=2, column=0, columnspan=3, pady=(0, 10))
        self.input_button.grid(row=3, column=0, columnspan=3, pady=10)

    # Function that stores the input as the number of credits for the user
    def store_credits(self, user_entry):
        StudentData.credits = user_entry

    # Function that verifies the input in the input box
    def verify_input(self, user_entry):
        try:
            if (1 <= float(user_entry) <= 40) and (
                float(user_entry) % 0.5 == 0
            ):
                # If valid, delete the error box
                self.input_box_error.grid_forget()
                # Store the number of credits
                self.store_credits(user_entry)
                # Go to the question pages
                self.master.replace_frame(QuestionPage)
            else:
                raise ValueError
        except ValueError:
            self.input_box_error.grid(row=4, column=0, columnspan=3)


# Class that stores the questions
class QuestionPage(ct.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        # Setup the frame
        self.configure(fg_color="transparent")

        # Create the widgets
        self.create_widgets()
        # Change to the first question
        self.next_question("q1p1")

    # Function that creates the widgets
    def create_widgets(self):
        # Title widget
        self.title = ct.CTkLabel(
            self,
            text="text for title",
            font=Fonts.get_font("QUESTION_TEXT_FONT"),
        )
        # Half buttons widgets
        self.b_left_half = ct.CTkButton(
            self,
            hover_color="#001B4B",
            font=Fonts.get_font("TITLE_TEXT_FONT_S15"),
        )
        self.b_right_half = ct.CTkButton(
            self,
            hover_color="#001B4B",
            font=Fonts.get_font("TITLE_TEXT_FONT_S15"),
        )
        # Third buttons widgets
        self.b_left_third = ct.CTkButton(
            self,
            hover_color="#001B4B",
            font=Fonts.get_font("TITLE_TEXT_FONT_S15"),
        )
        self.b_middle_third = ct.CTkButton(
            self,
            hover_color="#001B4B",
            font=Fonts.get_font("TITLE_TEXT_FONT_S15"),
        )
        self.b_right_third = ct.CTkButton(
            self,
            hover_color="#001B4B",
            font=Fonts.get_font("TITLE_TEXT_FONT_S15"),
        )
        # Quarter buttons widgets
        self.b_top_left = ct.CTkButton(
            self,
            hover_color="#001B4B",
            font=Fonts.get_font("TITLE_TEXT_FONT_S15"),
        )
        self.b_top_right = ct.CTkButton(
            self,
            hover_color="#001B4B",
            font=Fonts.get_font("TITLE_TEXT_FONT_S15"),
        )
        self.b_bot_left = ct.CTkButton(
            self,
            hover_color="#001B4B",
            font=Fonts.get_font("TITLE_TEXT_FONT_S15"),
        )
        self.b_bot_right = ct.CTkButton(
            self,
            hover_color="#001B4B",
            font=Fonts.get_font("TITLE_TEXT_FONT_S15"),
        )
        # Back button widget
        self.back_button = ct.CTkButton(
            self,
            text="Back",
            hover_color="#001B4B",
            font=Fonts.get_font("TITLE_TEXT_FONT_S15"),
            command=lambda: [back_button_click()],
        )

        # Function for when the back button is clicked
        @staticmethod
        def back_button_click():
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

    # Function that goes to the next question
    def next_question(self, question_name):
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
    def display_questions(self, question_name):
        if q.questions[question_name]["button_cnt"] == 2:
            # If the question requires 2 buttons
            self.b_left_half.grid(row=1, column=0, pady=10)
            self.b_right_half.grid(row=1, column=2, pady=10)
        elif q.questions[question_name]["button_cnt"] == 3:
            # If the question requires 3 buttons
            self.b_left_third.grid(row=1, column=0, pady=10)
            self.b_middle_third.grid(row=1, column=1, pady=10)
            self.b_right_third.grid(row=1, column=2, pady=10)
        elif q.questions[question_name]["button_cnt"] == 4:
            # If the question requires 4 buttons
            self.b_top_left.grid(row=1, column=0, pady=10)
            self.b_top_right.grid(row=1, column=2, pady=10)
            self.b_bot_left.grid(row=2, column=0, pady=10)
            self.b_bot_right.grid(row=2, column=2, pady=10)

    # Function that displays the back button
    def display_back_button(self, question_name):
        # If the question is the first question or the final question
        # Do not display the back button
        if (question_name == "q1p1") or (question_name == "END"):
            self.back_button.grid_forget()
        else:
            # If the question is not the first question or the final question
            # Display the back button
            self.back_button.grid(row=3, column=0, pady=10)

    # Function that changes the text and commands of the buttons
    def config_questions(self, question_name):
        # Change the title of the question
        self.title.configure(text=q.questions[question_name]["prompt"])
        self.title.grid(row=0, column=0, columnspan=3, pady=(50, 0))
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
    def forget_widgets(self, widget_cnt):
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
    def change_points(self, value):
        StudentData.points_history.append(value)
        StudentData.points += value


# Class that displays the results to the user
class ResultsPage(ct.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        # Setup the frame
        self.configure(fg_color="transparent")

        # Create the widgets
        self.create_widgets()
        # Display the widgets
        self.display_widgets()

    def create_widgets(self):
        # Creates the logo
        self.logo = ct.CTkImage(
            light_image=Image.open("housing_calc_new/assets/mw_logo.png"),
            dark_image=Image.open("housing_calc_new/assets/mw_logo.png"),
            size=(150, 150),
        )
        self.logo_label = ct.CTkLabel(self, text="", image=self.logo)
        # Creates the text
        self.main_text = ct.CTkLabel(
            self,
            text=(
                "Your information has been successfully submitted."
                "\nPlease check your email for a confirmation of your"
                "\nThank you for using the MWU Housing Calculator."
            ),
            font=Fonts.get_font("TITLE_TEXT_FONT_S15"),
        )
        # Creates the points text
        self.points_text = ct.CTkLabel(
            self,
            text=f"Your points: {round(StudentData.points, 1)}",
            font=Fonts.get_font("TITLE_TEXT_FONT_S15"),
        )
        # Creates the restart button
        self.restart_button = ct.CTkButton(
            self,
            text="Restart",
            command=lambda: [
                self.display_widgets("off"),
                self.master.replace_frame(StartPage),
            ],
        )

    # Function that displays the widgets
    def display_widgets(self):
        self.logo_label.grid(row=0, column=1, columnspan=4, pady=(50, 50))
        self.main_text.grid(row=1, column=0, columnspan=6)
        self.points_text.grid(row=2, column=0, columnspan=6, pady=(50, 0))
        self.restart_button.grid(row=4, column=1, columnspan=4)


# MAIN PROGRAM


if __name__ == "__main__":
    app = App()
    app.mainloop()
