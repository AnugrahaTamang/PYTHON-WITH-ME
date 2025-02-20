import sqlite3
con = sqlite3.connect("data.db")
cursor = con.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS videos(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL )''')
def list_videos():
    cursor.execute('''SELECT  * FROM  videos''')
    for row in cursor.fetchall():
        print(row)
def add_videos(name, time):
    cursor.execute("INSERT INTO  videos(name, time) VALUES (?, ?)",(name, time))
    con.commit()
def update_videos(name, time, video_id):
    cursor.execute("UPDATE videos SET name = ?, time = ?, id = ?",(name, time, video_id))
    con.close()
    
def delete_videos():
    cursor.execute("DELETE videos ")
def main():
    while True:
        print("Youtube Manager Appp")
        print("1. List videos")
        print("2. Add videos")
        print("3. Update videos")
        print("4. Delete vidoes")
        print("5. exit")
        choice = input("Enter your choice ")
        if choice == "1":
            list_videos()
        elif choice == "2":
            name = input("Enter your video  name: ")
            time = input("ENter your video name: ")
            add_videos(name, time)
        elif choice == "3":
            video_id = input("Enter your video id: ")
            name = input("Enter your video name")
            time = input("Enter your video  time: ")
            update_videos(video_id, name, time)
        elif choice == "4":
            video_id = input("Enter your video id : ")
            delete_videos(video_id)
        elif choice == "5":
            break
        else:
            print("Invalid choice ")


if __name__ == "__main__":
    main()
