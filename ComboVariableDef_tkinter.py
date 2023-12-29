from tools import *

frm =form()
combobox(frm,["ahmed","amr"],True).pack()
combobox(frm,["ahmed","amr"]).pack()
combobox(frm).pack()
frm.mainloop()
