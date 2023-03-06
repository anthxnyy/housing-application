import customtkinter as ct
import questions as q
from PIL import Image


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


class StudentData:
    credits = 0
    points = 0
    question_history = []
    points_history = []


class App(ct.CTk):
    def __init__(self):
        super().__init__()
        ct.set_appearance_mode("dark")
        ct.set_default_color_theme("dark-blue")
        self._page = None
        self.geometry(f"{800}x{600}")
        self.title("Mary Ward University - Housing Calculator")

        self.logo = ct.CTkImage(
            light_image=Image.open("housing_calc_new/assets/mw_logo.png"),
            dark_image=Image.open("housing_calc_new/assets/mw_logo.png"),
            size=(250, 250),
        )
        self.logo_label = ct.CTkLabel(self, text="", image=self.logo)
        self.logo_label.place(relx=0.5, rely=0.5, anchor="center")

        self.after(
            1000,
            lambda: [
                self.replace_frame(StartPage),
                self.logo_label.destroy(),
            ],
        )

    def replace_frame(self, page):
        new_page = page(self)
        if self._page is not None:
            self._page.destroy()
        self._page = new_page
        self._page.pack()


class StartPage(ct.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(fg_color="transparent")
        self.grid_rowconfigure((0, 1, 2, 3), weight=1)
        self.grid_columnconfigure((0, 1, 2), weight=1)

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
        self.logo_label.grid(row=2, column=0, columnspan=3, pady=57)
        self.title_text_top.grid(row=0, column=0, columnspan=3, pady=(50, 0))
        self.title_text_under.grid(row=1, column=0, columnspan=3, pady=(10, 0))
        self.start_button.grid(row=3, column=0, columnspan=3, pady=10)


class CreditInputPage(ct.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(fg_color="transparent")

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
                self.input_verify(self.input_box.get()),
            ],
        )
        self.question_title.grid(row=0, column=0, columnspan=3, pady=(50, 0))
        self.input_box_title.grid(
            row=1, column=0, columnspan=3, sticky="S", pady=(50, 10)
        )
        self.input_box.grid(row=2, column=0, columnspan=3, pady=(0, 10))
        self.input_button.grid(row=3, column=0, columnspan=3, pady=10)

    def input_verify(self, user_entry):
        try:
            if (1 <= float(user_entry) <= 40) and (
                float(user_entry) % 0.5 == 0
            ):
                self.input_box_error.grid_forget()
                StudentData.credits = user_entry
                self.master.replace_frame(QuestionPage)
            else:
                self.input_box_error.grid(row=4, column=0, columnspan=3)
        except ValueError:
            self.input_box_error.grid(row=4, column=0, columnspan=3)


class QuestionPage(ct.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(fg_color="transparent")

        self.title = ct.CTkLabel(
            self,
            text="text for title",
            font=Fonts.get_font("QUESTION_TEXT_FONT"),
        )

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

        self.back_button = ct.CTkButton(
            self,
            text="Back",
            hover_color="#001B4B",
            font=Fonts.get_font("TITLE_TEXT_FONT_S15"),
            command=lambda: [back_button()],
        )

        self.change_question("q1p1")

        def back_button():
            self.forget_widgets("all")
            if len(StudentData.points_history) >= 2:
                StudentData.points -= StudentData.points_history[-1]
                StudentData.points_history.pop()
            else:
                StudentData.points -= StudentData.points_history[0]
                StudentData.points_history = []
            StudentData.question_history.pop()
            self.change_question(StudentData.question_history[-1])
            StudentData.question_history.pop()

    def change_question(self, question_name):
        if question_name != "END":
            StudentData.question_history.append(question_name)
            self.config_questions(question_name)
            self.display_questions(question_name)
            self.display_back_button(question_name)
        else:
            self.master.replace_frame(ResultsPage)

    def forget_widgets(self, button_cnt):
        widgets = [self.title]
        match button_cnt:
            case 2:
                widgets.extend(
                    [
                        self.b_left_half,
                        self.b_right_half,
                    ]
                )
            case 3:
                widgets.extend(
                    [
                        self.b_left_third,
                        self.b_middle_third,
                        self.b_right_third,
                    ]
                )
            case 4:
                widgets = [
                    self.title,
                    self.b_top_left,
                    self.b_top_right,
                    self.b_bot_left,
                    self.b_bot_right,
                ]
            case "all":
                widgets = [
                    self.title,
                    self.back_button,
                    self.b_left_half,
                    self.b_right_half,
                    self.b_left_third,
                    self.b_middle_third,
                    self.b_right_third,
                    self.b_top_left,
                    self.b_top_right,
                    self.b_bot_left,
                    self.b_bot_right,
                ]
        for widget in widgets:
            widget.grid_forget()

    def change_points(self, value):
        StudentData.points_history.append(value)
        StudentData.points += value

    def display_questions(self, question_name):
        match q.questions[question_name]["button_cnt"]:
            case 2:
                self.b_left_half.grid(row=1, column=0, pady=10)
                self.b_right_half.grid(row=1, column=2, pady=10)
            case 3:
                self.b_left_third.grid(row=1, column=0, pady=10)
                self.b_middle_third.grid(row=1, column=1, pady=10)
                self.b_right_third.grid(row=1, column=2, pady=10)
            case 4:
                self.b_top_left.grid(row=1, column=0, pady=10)
                self.b_top_right.grid(row=1, column=2, pady=10)
                self.b_bot_left.grid(row=2, column=0, pady=10)
                self.b_bot_right.grid(row=2, column=2, pady=10)

    def display_back_button(self, question_name):
        if (question_name == "q1p1") or (question_name == "END"):
            self.back_button.grid_forget()
        else:
            self.back_button.grid(row=3, column=0, pady=10)

    def config_questions(self, question_name):
        self.title.configure(text=q.questions[question_name]["prompt"])
        self.title.grid(row=0, column=0, columnspan=3, pady=(50, 0))
        match q.questions[question_name]["button_cnt"]:
            case 2:
                self.b_left_half.configure(
                    text=q.questions[question_name]["button_text"][0],
                    command=lambda: [
                        self.forget_widgets(2),
                        self.change_points(
                            q.questions[question_name]["button_values"][0]
                        ),
                        self.change_question(
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
                        self.change_question(
                            q.questions[question_name]["next_question"][1]
                        ),
                    ],
                )
            case 3:
                self.b_left_third.configure(
                    text=q.questions[question_name]["button_text"][0],
                    command=lambda: [
                        self.forget_widgets(3),
                        self.change_points(
                            q.questions[question_name]["button_values"][0]
                        ),
                        self.change_question(
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
                        self.change_question(
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
                        self.change_question(
                            q.questions[question_name]["next_question"][2]
                        ),
                    ],
                )
            case 4:
                self.b_top_left.configure(
                    text=q.questions[question_name]["button_text"][0],
                    command=lambda: [
                        self.forget_widgets(4),
                        self.change_points(
                            q.questions[question_name]["button_values"][0]
                        ),
                        self.change_question(
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
                        self.change_question(
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
                        self.change_question(
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
                        self.change_question(
                            q.questions[question_name]["next_question"][3]
                        ),
                    ],
                )


class ResultsPage(ct.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(fg_color="transparent")


# MAIN PROGRAM #


if __name__ == "__main__":
    app = App()
    app.mainloop()
