i = 0
while True:
   num = i%3
   print("To qwite to type q")
   q = ["How is the wather today?\n",
         "How old are you?\n",
         "How are you?\n"]
   
   ans = input(q[num])
   if ans == "q":
       print("終了します。")
       break
   else:
        with open("ans_list.txt", "a", encoding="utf-8") as f:
            f.write(ans)
            f.write("\n")
        i += 1
