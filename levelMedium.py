def tebak_angka_medium():
    import random

    while True: 
        print("\t\n=== SELAMAT DATANG DI LEVEL (MEDIUM) ===")
        print("=== ANDA MEMILIKI 6 KESEMPATAN ===\t\n")
        real_number = random.randint(1,15)
        kesempatan = 0
        # print(real_number)
        while kesempatan < 6:
            try:
                user_number = int(input("Masukkan angka 1-15: ")) 
            except ValueError:
                print("Masukkan Angka!\t\n")
                continue
            # Melihat jika input kurang dari 1 dan lebih dari 15
            if user_number < 1 or user_number > 15:
                    print("Masukkan Angka Yang Sesuai!\t\n")
                    continue
            
            # Program Utama                
            else:
                
                # Melihat jika input lebih dari real number    
                if user_number > real_number:
                    print("\t\nAngka tebakan anda lebih besar dari Real Number!")
                    print(f"Kesempatan anda = {6 - (kesempatan+1)}")
                    kesempatan += 1
                    
                # Melihat jika input kurang dari real number
                elif user_number < real_number:
                    print("\t\nAngka tebakan anda lebih kecil dari Real Number!")
                    print(f"Kesempatan anda = {6 - (kesempatan+1)}")
                    kesempatan += 1
                    
                # Melihat jika input sama dengan real number (Benar)
                elif user_number == real_number:
                    print(f"\t\nSelamat anda benar, Real Number = {real_number}")
                    break
                
            # Clue
            if kesempatan == 3 or kesempatan == 5:
                if real_number % 2 == 0:
                    print("Clue: Real Number adalah Genap\t\n")
                    continue
                else:
                    print("Clue: Real Number adalah Ganjil\t\n")
                    continue    
            
        # Reveal Real Number        
        if kesempatan == 6:
            print(f"\t\nYah, kamu kalah. Angka sebenarnya = {real_number}")

        # Ajakan Untuk Bermain Lagi
        play_again = input("Main Lagi? Y/N: ").lower()
        if play_again != "y":
            print("Terima Kasih!!")
            break
    