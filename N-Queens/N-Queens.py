import tkinter as tk
import customtkinter as ct
from tkinter import StringVar,PhotoImage,ttk


class NQueen :

    def __init__(self) :
        self.root = tk.Tk()
        self.root.geometry("700x500+500+100")
        self.bgColor = "#222831"
        self.root.configure(bg=self.bgColor)
        self.allSet = []
        self.soln = []
        self.root.title("N-Queen")
        self.root.resizable(False,False)

        
        self.image_icon = PhotoImage(file="images/crown_1.png")
        self.root.iconphoto(False,self.image_icon)

        self.data()

        self.root.mainloop()

    def data(self) :

        self.number = ct.CTkLabel(self.root,text="Enter number of Queens : ",font=('Arial',18),text_color='white',width=200)
        self.number.place(x=20,y=30)
        self.numberAvability = ct.CTkLabel(self.root,text="",anchor='w',font=('Arial',15),text_color='white',width=200)
        self.numberAvability.place(x=20,y=50)

        self.n_test = StringVar()

        self.input_number = ct.CTkEntry(self.root,textvariable=self.n_test,height=30,width=150)
        self.input_number.place(x=240,y=30)


        self.number_right = ct.CTkLabel(self.root,text="N-Queen Matrix",font=('Arial',18),text_color='white',width=60)
        self.number_right.place(x=530,y=10)


        self.number_right_value = ct.CTkLabel(self.root,text="None",font=('Arial',18),text_color='white',width=60,height=20)
        self.number_right_value.place(x=552,y=33)

        self.search_button = ct.CTkButton(self.root,text="Search",width=50,command=self.change_number_right_value,font=("Helvetica",14,"bold"),fg_color="#E3E1D9",text_color="black")
        self.search_button.place(x=400,y=30)

        self.displayIntro()

# About N-Queens on Home Page
    def displayIntro(self) :
        
        self.intro_frame_bottom = ct.CTkFrame(self.root,width=700,height=400,corner_radius=0,fg_color="#31363F")
        self.intro_frame_bottom.place(y=100)

        
        self.intro_number_right = ct.CTkLabel(self.intro_frame_bottom,text="About N-Queens Problem",font=('Arial',27,'bold'),text_color='white',width=700,height=50)
        self.intro_number_right.place(y=20)

        t = "The N-Queens problem is a classic puzzle that challenges you to place N queens on an NxN chessboard so that no two queens threaten each other. Backtracking is a common algorithmic technique used to solve such problems efficiently by exploring potential solutions incrementally and abandoning paths that are determined to be invalid. In the context of the N-Queens problem, backtracking involves recursively placing queens on the board, backtracking when a conflict arises, and exploring alternative placements. This process continues until a valid solution is found or all possible configurations are exhausted. It's a powerful method for solving combinatorial optimization problems like the N-Queens puzzle."        
        self.intro_number_right1 = tk.Text(self.intro_frame_bottom,fg='white',bg="#31363F", wrap=tk.WORD,borderwidth=0,font=('Helvetica',13),spacing2=9)
        self.intro_number_right1.insert(tk.END,t)
        self.intro_number_right1.place(x=50,y=100,width=600)

    
    def isSafe(self,k,i):
        for j in range(k):
            if ( self.soln[j] == i or abs(self.soln[j]-i) == abs(j-k)):
                return False
        return True
    
    def NQueen_sol(self,k,n):
        for i in range(n):
            
            if (self.isSafe(k,i)):
                self.soln[k] = i
                if k == n-1:
                    self.allSet.append(list(self.soln))
                else:
                    self.NQueen_sol(k+1,n)


# Change Value of matrix n X n
    def change_number_right_value(self) :
        self.soln = []
        self.allSet = []
        value = self.n_test.get()
        self.number_right_value.configure(text=(value+" X "+value))        
        self.soln = [0 for i in range(int(value))]
            
        self.NQueen_sol(0,int(value))
        if len(self.allSet) == 0:
            self.numberAvability.configure(text="No Solution Available")
        else :
            print(int(value))
            self.intro_frame_bottom.destroy()
            self.numberAvability.configure(text="")
            self.display_NQueenData()

# Display All possible Solutions
    def display_NQueenData(self) :
        
        self.frame_bottom = ct.CTkFrame(self.root,width=700,height=400,corner_radius=0,fg_color=self.bgColor)
        self.frame_bottom.place(y=100)

        self.total_number = ct.CTkLabel(self.frame_bottom,text="Total no of solutions : "+str(len(self.allSet)),font=('Arial',21),text_color='white',width=60)
        self.total_number.place(x=50,y=150)
        
        self.number_right = ct.CTkLabel(self.frame_bottom,text="All Possible Combinations",font=('Arial',21),text_color='white',width=60)
        self.number_right.place(x=210,y=20)

        
        self.matrix_values = ct.CTkScrollableFrame(self.frame_bottom,width=350,height=270,fg_color=self.bgColor)
        self.matrix_values.place(x=300,y=90)

        self.selected_size = tk.StringVar()

        style = ttk.Style()
        style.configure("Custom.TRadiobutton",foreground="white",background=self.bgColor,font=('Arial',12))

        for size in self.allSet:

            r = ttk.Radiobutton(self.matrix_values, text=str(size), value=size, variable=self.selected_size,style="Custom.TRadiobutton")
            r.pack(fill='x', padx=5, pady=5)

        
        self.total_number1 = ct.CTkLabel(self.frame_bottom,text="",font=('Arial',15),text_color='white',width=60)
        self.total_number1.place(x=50,y=175)

        button = ct.CTkButton(self.frame_bottom, text="Get Selected Data", command=self.selected_display_data ,font=("Helvetica",14,"bold"),fg_color="#E3E1D9",text_color="black")
        button.place(x=75,y=210)

# Display N-Queens Board 
    def selected_display_data(self):

        if self.selected_size.get() :
            self.total_number1.configure(text="")
            temp = self.selected_size.get().strip().split(" ")
            solution = [int(i) for i in temp]
            root = tk.Tk()
            root.title(str(solution))
            n = int(self.n_test.get())

            # Calculate canvas size based on the number of queens
            canvas_size = 50 * n

            # Create a canvas to draw the chessboard
            canvas = tk.Canvas(root, width=canvas_size, height=canvas_size)
            canvas.pack()

            # Draw the chessboard
            for i in range(n):
                for j in range(n):
                    color = "white" if (i+j) % 2 == 0 else "#B4B4B8"
                    canvas.create_rectangle(j*canvas_size//n, i*canvas_size//n, (j+1)*canvas_size//n, (i+1)*canvas_size//n, fill=color)

            # Place queens on the chessboard according to the solution
            for i, column in enumerate(solution):
                canvas.create_text(column*canvas_size//n + canvas_size//n//2, i*canvas_size//n + canvas_size//n//2, text="Q", font=("Arial", canvas_size//n//2))

            root.mainloop()
        else :
            self.total_number1.configure(text="Please Select a data first!!!")
    
NQueen()