from tkinter import *


from QuizLogic import QuizLogic
from PIL import Image, ImageTk
THEME_COLOR = "#2D033B"


class Interface:
    def __init__(self, quiz_brain: QuizLogic):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quiz Game")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=350, height=300, bg="white")
        self.questions_text = self.canvas.create_text(175, 150, text="Title", font=("Arial", 20, "italic"),
                                                      width=320, fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=50)

        self.label = Label(text="Score 0", font=("Arial", 14), fg="white", highlightthickness=0,
                           background=THEME_COLOR)
        self.label.grid(row=0, column=1)

        self.image_right = Image.open("img.png")
        self.resized_image_right = self.image_right.resize((100, 97), Image.NEAREST)
        self.right = ImageTk.PhotoImage(self.resized_image_right)
        self.button1 = Button(image=self.right, bg=THEME_COLOR, highlightthickness=0, command=self.true_button)
        self.button1.grid(row=2, column=0)

        self.image_wrong = Image.open("img_1.png")
        self.resized_image_wrong = self.image_wrong.resize((100, 97), Image.NEAREST)
        self.wrong = ImageTk.PhotoImage(self.resized_image_wrong)
        self.button2 = Button(image=self.wrong, bg=THEME_COLOR, highlightthickness=0, command=self.false_button)
        self.button2.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.label.config(text=f"Score {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.questions_text, text=q_text)
        else:
            self.canvas.itemconfig(self.questions_text, text="You have reached the end of the quiz.")
            self.button1['state'] = "disabled"
            self.button2['state'] = "disabled"

    def true_button(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_button(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
