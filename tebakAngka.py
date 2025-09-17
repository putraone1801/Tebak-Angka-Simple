import levelEasy
import levelMedium
import levelHard


while True:
    print("\t\nSelamat Datang Di Tebak Game Angka")
    difficulty = input("Pilih lah Kesulitan Easy/Medium/Hard: ").lower()
    if difficulty != "easy" and difficulty != "medium" and difficulty != "hard":
        print("Pilih Kesulitan Yang Tersedia!\t\n")
        continue 
    while True:
        if difficulty == "easy":
            levelEasy.tebak_angka_easy()
            break
            
        elif difficulty == "medium":
            levelMedium.tebak_angka_medium()
            break
        
        elif difficulty == "hard":
            levelHard.tebak_angka_hard()
            break
    confirmation = input("Apakah Kamu Ingin Merubah Kesulitan? Y/N: ").lower()
    if confirmation != "y":
        break
print("Terima Kasih Sudah Bermain 😊")

