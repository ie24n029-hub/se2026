tasks = []

while True:
    print("\n=== ToDo管理システム ===")
    print("1. タスク追加")
    print("2. タスク一覧")
    print("3. タスク削除")
    print("4. 終了")

    choice = input("選択してください: ")

    # タスク追加
    if choice == "1":
        task = input("タスク名を入力してください: ")
        tasks.append(task)
        print("タスクを追加しました")

    # タスク一覧表示
    elif choice == "2":
        print("\n--- タスク一覧 ---")

        if len(tasks) == 0:
            print("タスクがありません")
        else:
            for i, task in enumerate(tasks):
                print(f"{i}: {task}")

    # タスク削除
    elif choice == "3":
        if len(tasks) == 0:
            print("削除できるタスクがありません")
        else:
            number = int(input("削除する番号を入力してください: "))

            if 0 <= number < len(tasks):
                deleted = tasks.pop(number)
                print(f"{deleted} を削除しました")
            else:
                print("番号が正しくありません")

    # 終了
    elif choice == "4":
        print("終了します")
        break

    # その他
    else:
        print("無効な入力です")
