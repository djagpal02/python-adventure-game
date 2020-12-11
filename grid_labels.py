
for i in range(22):
            for j in range(22):
                x = 'img' + str(i)+ str(j)
                print(f"self.{x} = tk.Label(self.frame1,text='a')\nself.{x}.grid(row={i},column={j})")


for i in range(22):
    for j in range(22):
        x = 'img' + str(i)+ str(j)
        print(f"self.{x}.configure(text = 'b')")