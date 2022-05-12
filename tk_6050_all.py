from tkinter import *
from mpu6050 import mpu6050

sensor = mpu6050(0x68)

def update():
    data = sensor.get_all_data()
    ax_data = data[0]['x']
    ax.delete(0,END)
    ax.insert(0, '%.1f'%ax_data)
    root.after(300, update)

root = Tk()
root.title('MPU6050')
Label(root, text = 'Accel X: ').grid(row=0, column=0)

ax = Entry(root)
ax.grid(row=0, column=1)

Button(root, text='Quit', comman=root.destroy).grid(row=1, column=0)

update()
root.mainloop()