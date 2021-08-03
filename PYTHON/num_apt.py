import optical_fibre
x = float(input("Enter the diameter of the spot: "))
y = int(input("Enter the distance between screen and output: "))
s = optical_fibre.num_apt(x,y)
print("The numerical aperture is : %f"%(s))
