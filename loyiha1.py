import os

# 1. Shifrlash va Deshifrlash Moduli
class Cipher:
    @staticmethod
    def encrypt(text, shift):
        result = ""
        for char in text:
            if char.isalpha():
                start = ord('a') if char.islower() else ord('A')
                result += chr((ord(char) - start + shift) % 26 + start)
            else:
                result += char
        return result

    @staticmethod
    def decrypt(text, shift):
        return Cipher.encrypt(text, -shift)

# 2. Ma'lumotlar bilan ishlash (File Management)
class NoteManager:
    def __init__(self, filename="secret_notes.txt"):
        self.filename = filename

    def save_note(self, encrypted_text):
        with open(self.filename, "a") as file:
            file.write(encrypted_text + "\n")
        print("✅ Eslatma shifrlanib saqlandi!")

    def read_all_notes(self, shift):
        if not os.path.exists(self.filename):
            print("📭 Hali eslatmalar yo'q.")
            return

        print("\n--- Sizning barcha eslatmalaringiz (Deshifrlangan) ---")
        with open(self.filename, "r") as file:
            for line in file:
                decrypted = Cipher.decrypt(line.strip(), shift)
                print(f"📌 {decrypted}")

# 3. Asosiy Interfeys
def main():
    manager = NoteManager()
    shift_key = 5  # Bu bizning maxfiy kalitimiz

    while True:
        print("\n--- SecureNotes Terminal V1.0 ---")
        print("1. Yangi eslatma yozish")
        print("2. Eslatmalarni ko'rish")
        print("3. Faylni tozalash")
        print("4. Chiqish")
        
        choice = input("Tanlang (1-4): ")

        if choice == '1':
            note = input("Eslatmani kiriting: ")
            encrypted = Cipher.encrypt(note, shift_key)
            manager.save_note(encrypted)
        
        elif choice == '2':
            manager.read_all_notes(shift_key)
            
        elif choice == '3':
            if os.path.exists(manager.filename):
                os.remove(manager.filename)
                print("🗑 Barcha eslatmalar o'chirildi.")
            
        elif choice == '4':
            print("Xayr! Xavfsizligingizga e'tiborli bo'ling.")
            break
        else:
            print("⚠️ Noto'g'ri buyruq!")

if __name__ == "__main__":
    main()