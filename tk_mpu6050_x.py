from tkinter import *
from mpu6050 import mpu6050

sensor = mpu6050(0x68)

def update():
    ax.delete(0,END)
    ay.delete(0,END)
    az.delete(0,END)
    gx.delete(0,END)
    gy.delete(0,END)
    gz.delete(0,END)
    data = sensor.get_all_data()
    ax_data = data[0]['x']
    ay_data = data[0]['y']
    az_data = data[0]['z']
    gx_data = data[1]['x']
    gy_data = data[1]['y']
    gz_data = data[1]['z']
    ax.insert(0, '%.1f'%ax_data)
    ay.insert(0, '%.1f'%ay_data)
    az.insert(0, '%.1f'%az_data)
    gx.insert(0, '%.1f'%gx_data)
    gy.insert(0, '%.1f'%gy_data)
    gz.insert(0, '%.1f'%gz_data)
    root.after(300, update)

root = Tk()
root.title('MPU6050')
Label(root, text = 'Accel X: ').grid(row=0, column=0)
Label(root, text = 'Accel Y: ').grid(row=1, column=0)
Label(root, text = 'Accel Z: ').grid(row=2, column=0)
Label(root, text = 'Accel X: ').grid(row=3, column=0)
Label(root, text = 'Accel Y: ').grid(row=4, column=0)
Label(root, text = 'Accel Z: ').grid(row=5, column=0)

ax = Entry(root)
ay = Entry(root)
az = Entry(root)
gx = Entry(root)
gy = Entry(root)
gz = Entry(root)

ax.grid(row=0, column=1)
ay.grid(row=1, column=1)
az.grid(row=2, column=1)
gx.grid(row=3, column=1)
gy.grid(row=4, column=1)
gz.grid(row=5, column=1)

Button(root, text='Quit', comman=root.destroy).grid(row=6, column=0)

update()
root.mainloop()