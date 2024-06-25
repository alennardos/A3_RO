# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import axes3d  # Fonction pour la 3D
# from matplotlib import cm
# from matplotlib.ticker import LinearLocator, FormatStrFormatter
# import numpy as np
    
# import warnings
# warnings.filterwarnings('ignore')
# # Tableau pour les 3 axes
     
# xx, yy = np.meshgrid(range(6), range(6))
# z = (59 - 10*xx - 12*yy) / 7 

# # Tracé du résultat en 3D
# fig = plt.figure()
# ax = fig.add_subplot(projection = '3d')  # Affichage en 3D
# ax.plot_surface(xx,yy,z, linewidth=0,alpha=0.5)  # Tracé d'une surface
# plt.title("Tracé d'une surface")
# ax.set_xlabel('x1')
# ax.set_ylabel('x2')
# ax.set_zlabel('x3')
# ax.set_zbound(lower=0, upper=6)
# plt.tight_layout()
# xx, yy,z = np.meshgrid(range(6), range(6),range(10))
# Xblue = xx[10*xx+12*yy+7*z <= 59]
# Yblue = yy[10*xx+12*yy+7*z <= 59]
# Zblue = z[10*xx+12*yy+7*z <= 59]
# Xred = xx[10*xx+12*yy+7*z > 59]
# Yred = yy[10*xx+12*yy+7*z > 59]
# Zred = z[10*xx+12*yy+7*z > 59]
# ax.scatter(Xred,Yred,Zred, marker='o', s=30, color='red')
# ax.scatter(Xblue,Yblue,Zblue, marker='o', s=30, color='blue')
# ax.set_zlim3d(0,9)
# plt.show()

a = ["A", "B", "C", "D", "E", "F"]
b = [1,2,3,4,5,6]