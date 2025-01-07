import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import random

class Character:
    def __init__(self, name):
        self.name = name
        self.strength = 100
        self.health = 1000
        
    def attack(self):
        return self.strength
    
    def hit(self, points):
        self.health -= points
        
    def is_alive(self):
        return self.health > 0

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name)
        self.health += 100
        self.strength += 100

class Archer(Character):
    def __init__(self, name):
        super().__init__(name)
        self.health -= 100
        self.strength += 250
        
class Wizard(Character):
    def __init__(self, name):
        super().__init__(name)
        self.health -= 200
        self.strength += 300

class BattleSimulator:
    def __init__(self, character1, character2):
        self.character1 = character1
        self.character2 = character2
        self.log = []

    def battle(self):
        round_number = 1
        while self.character1.is_alive() and self.character2.is_alive():
            self.log.append(f"--- Round {round_number} ---")

            damage = self.character1.attack()
            self.character2.hit(damage)
            self.log.append(f"{self.character1.name} attacks {self.character2.name} dealing {damage} damage.")
            self.log.append(f"{self.character2.name} health: {max(0, self.character2.health)}")

            if not self.character2.is_alive():
                self.log.append(f"\n{self.character2.name} has fallen! {self.character1.name} wins!")
                break

            damage = self.character2.attack()
            self.character1.hit(damage)
            self.log.append(f"{self.character2.name} attacks {self.character1.name} dealing {damage} damage.")
            self.log.append(f"{self.character1.name} health: {max(0, self.character1.health)}")

            if not self.character1.is_alive():
                self.log.append(f"\n{self.character1.name} has fallen! {self.character2.name} wins!")
                break

            round_number += 1

        self.log.append("\nThe battle is over!")

class BattleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("2 vs 2 Battle Simulator")

        self.character1 = None
        self.character2 = None

        self.setup_input_frame()

    def setup_input_frame(self):
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(pady=10)

        tk.Label(self.input_frame, text="Player 1 Name:").grid(row=0, column=0)
        self.name1_entry = tk.Entry(self.input_frame)
        self.name1_entry.grid(row=0, column=1)

        tk.Label(self.input_frame, text="Player 1 Class:").grid(row=1, column=0)
        self.class1 = ttk.Combobox(self.input_frame, values=["Warrior", "Archer", "Wizard"], state="readonly")
        self.class1.grid(row=1, column=1)

        tk.Label(self.input_frame, text="Player 2 Name:").grid(row=2, column=0)
        self.name2_entry = tk.Entry(self.input_frame)
        self.name2_entry.grid(row=2, column=1)

        tk.Label(self.input_frame, text="Player 2 Class:").grid(row=3, column=0)
        self.class2 = ttk.Combobox(self.input_frame, values=["Warrior", "Archer", "Wizard"], state="readonly")
        self.class2.grid(row=3, column=1)

        tk.Button(self.input_frame, text="Start Battle", command=self.start_battle).grid(row=4, columnspan=2, pady=10)

    def start_battle(self):
        name1 = self.name1_entry.get()
        class1 = self.class1.get()
        name2 = self.name2_entry.get()
        class2 = self.class2.get()

        if not name1 or not class1 or not name2 or not class2:
            showinfo("Error", "Please fill all fields.")
            return

        self.character1 = self.create_character(name1, class1)
        self.character2 = self.create_character(name2, class2)

        simulator = BattleSimulator(self.character1, self.character2)
        simulator.battle()

        self.show_results(simulator.log)

    def create_character(self, name, char_class):
        if char_class == "Warrior":
            return Warrior(name)
        elif char_class == "Archer":
            return Archer(name)
        elif char_class == "Wizard":
            return Wizard(name)

    def show_results(self, log):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Battle Results", font=("Arial", 16)).pack(pady=10)
        result_text = tk.Text(self.root, width=60, height=20)
        result_text.pack(pady=10)
        for line in log:
            result_text.insert(tk.END, line + "\n")
        result_text.config(state="disabled")

        tk.Button(self.root, text="Restart", command=self.restart).pack(pady=10)

    def restart(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.setup_input_frame()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x400")
    app = BattleApp(root)
    root.mainloop()
