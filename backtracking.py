import tkinter as tk
from tkinter import messagebox, simpledialog
import time

class NQueenGUI:
    def __init__(self, root, n, algorithm='backtracking'):
        self.root = root
        self.n = n
        self.board = [[0 for _ in range(n)] for _ in range(n)]
        self.cells = [[None for _ in range(n)] for _ in range(n)]
        self.algorithm = algorithm

        self.create_widgets()
        if self.algorithm == 'backtracking':
            self.solve_n_queens_backtracking()

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
                    self.cells[i][j].config(text='Q', bg='darkgrey')
                else:
                    self.cells[i][j].config(text='', bg='white')
    
    def display_positions(self):
        positions = []
        for i in range(self.n):
            for j in range(self.n):
                if self.board[i][j] == 1:
                    positions.append((i, j))
        print(f"Current positions: {positions}")

    def is_safe(self, row, col): 
        for i in range(col): # Untuk Cek Vertikal (atas bawah)
            if self.board[row][i] == 1:
                return False 

        for i, j in zip(range(row, -1, -1), range(col, -1, -1)): # Untuk cek horizontal (kiri kanan)
            if self.board[i][j] == 1:
                return False

        for i, j in zip(range(row, self.n, 1), range(col, -1, -1)): #untuk cek diagonal (miring)
            if self.board[i][j] == 1:
                return False

        return True

    def solve_n_queens_backtracking_util(self, col): #cek sampai kolom ke n
        if col >= self.n:
            return True

        for i in range(self.n):
            if self.is_safe(i, col):
                self.board[i][col] = 1
                self.update_board()
                self.display_positions()
                self.root.update_idletasks()
                time.sleep(0.5) 

                if self.solve_n_queens_backtracking_util(col + 1):
                    return True

                self.board[i][col] = 0
                self.update_board()
                self.display_positions()
                self.root.update_idletasks()
                time.sleep(0.5)

        return False

    def solve_n_queens_backtracking(self):
        start_time = time.time()
        if not self.solve_n_queens_backtracking_util(0):
            end_time = time.time()
            elapsed_time = end_time - start_time
            messagebox.showinfo("Tidak ada solusi", f"Tidak ada solusi. Waktu pengerjaan: {elapsed_time:.4f} detik")
        else:
            end_time = time.time()
            elapsed_time = end_time - start_time
            messagebox.showinfo("Berhasil menemukan solusi", f"Solusi berhasil ditemukan dalam {elapsed_time:.4f} detik")

def main():
    root = tk.Tk()
    root.title("Papan Catur N-Queen Problem")

    n = 0
    while n < 1 or n > 8:
        try:
            n = int(simpledialog.askstring("Input", "Masukkan banyak queen (1-8):", parent=root))
        except (ValueError, TypeError):
            pass
    
    app = NQueenGUI(root, n, algorithm='backtracking')  
    root.mainloop()

if __name__ == "__main__":
    main()
