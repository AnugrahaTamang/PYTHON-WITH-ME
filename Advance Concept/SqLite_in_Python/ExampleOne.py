import sqlite3
con = sqlite3.connect("youtube.db")
cursor = con.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS videos
               (id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL)''')
def list_video():
    cursor.execute('''SELECT * FROM videos ''')
    for row in cursor.fetchall():
        print(row)
def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    con.commit()
def update_video(video_id, name, time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (name, time, video_id))
    con.commit()
def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    con.commit()    
def main():
    while True:
        print("\n Youtube Manager app with sqlite3")
        print("1. List videos")
        print("2. Add Videos")
        print("3. Update videos")
        print("4. Delete Videos")
        print("5. exit")
        choice = input("Enter your Choice: ")
        if choice == "1":
            list_video()
        elif choice == "2":
            name = input("Enter your video name: ")
            time = input("Enter your time: ")
            add_video(name, time)
        elif choice == "3":
            video_id = input("Enter your video id: ")
            name = input("Enter your video name: ")
            time = input("Enter your video time: ")
            update_video(video_id, name, time)
        elif choice == "4":
            video_id = input("Enter your video id: ")
            delete_video(video_id)
        elif choice == "5":
            break
        else:
            print("Invalid choice")
    con.close()

if __name__ == "__main__":
    main()