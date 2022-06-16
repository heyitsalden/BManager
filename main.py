import pandas as pd

def budReader():

    budgetData = pd.read_csv(r'C:\\Users\\isayu\\OneDrive\\Desktop\aldenCode\\BManager-main\\alden-test.csv')

    counter = 0

    for i in range(len(budgetData.columns)):
        counter +=1

    col = range(4,counter)

    expenses = (budgetData.columns[col])
    # print(budgetData)

    maxBud = budgetData[expenses].max()

    print(budgetData)

    return budReader

budReader()

#
# #Creates GUI display for the max and min values
# title = Tk()
# title.title('Stock Max and Stock Min')
# title.geometry('320x220')
# frm = ttk.Frame(title, padding=10)
# frm.grid()
# ttk.Label(frm, text="Max").grid(column=0, row=0)
# ttk.Label(frm, text="Min").grid(column=3, row=0)
#
# # for i in range(len(budReader())):
# #     x = budReader()
#
# ttk.Button(frm, text="Quit", command=title.destroy).grid(column=2, row=10)
# title.mainloop()
