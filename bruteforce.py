import tkinter as tk
from tkinter import messagebox, simpledialog
import time
import random

class NQueenGUI:
    def __init__(self, root, n):
        self.root = root
        self.n = n
        self.board = [[0 for _ in range(n)] for _ in range(n)]
        self.cells = [[None for _ in range(n)] for _ in range(n)]

        self.create_widgets()
        self.solve_n_queens_brute_force()

    def create_widgets(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack()

        for i in range(self.n):
            for j in range(self.n):
                cell = tk.Label(self.frame, text='', width=4, height=2, borderwidth=1, relief="solid", font=("Helvetica", 16))
                cell.grid(row=i, column=j)
                self.cells[i][j] = cell

    def update_board(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.board[i][j] == 1:
                    self.cells[i][j].config(text='Q', bg='lightblue')
                else:
                    self.cells[i][j].config(text='', bg='white')

    def is_safe(self, perm):
        for i in range(self.n):
            for j in range(i + 1, self.n):
                if abs(perm[i] - perm[j]) == abs(i - j):
                    return False
        return True

    def solve_n_queens_brute_force(self):
        def generate_permutations(perm, l, r, solutions):
            if l == r:
                if self.is_safe(perm):
                    solutions.append(perm.copy())
            else:
                for i in range(l, r + 1):
                    perm[l], perm[i] = perm[i], perm[l]
                    generate_permutations(perm, l + 1, r, solutions)
                    perm[l], perm[i] = perm[i], perm[l]

        start_time = time.time()
        solutions = []
        perm = list(range(self.n))
        generate_permutations(perm, 0, self.n - 1, solutions)

        if solutions:
            chosen_solution = random.choice(solutions)  # Pilih solusi secara acak
            for i in range(self.n):
                self.board[i][chosen_solution[i]] = 1
            self.update_board()
            self.root.update_idletasks()
            end_time = time.time()
            elapsed_time = end_time - start_time
            messagebox.showinfo("Berhasil menemukan solusi", f"Solusi berhasil ditemukan dalam {elapsed_time:.4f} detik")
        else:
            end_time = time.time()
            elapsed_time = end_time - start_time
            messagebox.showinfo("Tidak ada solusi", f"Tidak ada solusi. Waktu pengerjaan: {elapsed_time:.4f} detik")

def main():
    root = tk.Tk()
    root.title("Papan Catur N-Queen Problem")

    n = 0
    while n < 1 or n > 8:
        try:
            n = int(simpledialog.askstring("Input", "Masukkan banyak queen (1-8):", parent=root))
        except (ValueError, TypeError):
            pass
    
    app = NQueenGUI(root, n)
    root.mainloop()

if __name__ == "__main__":
    main()
