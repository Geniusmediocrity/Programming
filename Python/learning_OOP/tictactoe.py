import tkinter as tk


root = tk.Tk()

b_code = (b'iVBORw0KGgoAAAANSUhEUgAAAEwAAABMCAIAAABI9cZ8AAAACXBIWXMAAAsTAAALEwEAmpwYAAAGoElEQVR42uVcW2wUZR'
              b'Q+55/Z6V66ve32BmwpLSBCqQFBMAQRIQgxGpWY6IN4iY8mPqgv3sIDPhljTEx4MJEXSUBjQogSQqICcpOgIDcBF1paaOmF'
              b'7tJuu5e5HB92d3Zmdma7YCu7P//DpvNfzv7ff85/brOnAA9AQ6cByVMTCD0abHu8Mtjm9tULksc0F4EsC5gzYcw9ENpOMP'
              b'TbUSDbnSKoSiIVG4kNdUWunoxc+zMe7SsWpOStDXU827ZiS01Th+T2A2NkmYu5T6ehvH60nk4eWrKj73g0hlVEpCRj44PX'
              b'ek98d/3It4k7A5OArG5etHjjx7PmbzCxznlnmSHMI2ldgndBLR+nUXCcTgdBU5VI+MS57z+5Hf6dNFVfIRgRBkJLV738TW'
              b'Pbaia6LDtG5+9ALNhvxKl/OHPG6Q+0O8fcU3oOY95gS2PH+titcGwgrMtZDqSvbs7aN36oaphfYNMIReLJIbJSyx4YOsg/F'
              b'kMtt4RylLJDLm9V/cInotfPjA91m8iIUuWa13Y3z3/KKBualhoIH+67tD9y85yciv0nRYZ3pw+puOWCy+2fsaC5c2PDwrWi'
              b'12+cfKf33JHPX4iP3MgeAbL25VtWvPgVClnGIsVGek7tfX8gfFBJjhNpJWwfUHR56tof69i8tW7eytwd1tR/9n95dveHQCQ'
              b'AgLsyuGTTp77aFv0Yxm53Hdv11q0rP2tKKv9YS61pqjw+3D3496G61qXeQCgDkzF/49yu4zvVxDgDgNrmR+qaO3VBkZOxv/'
              b'ZvHeo6Vl4Wf3yo6/TOd+VYBCkDRPIHZ3ZuypjwYGiZKHmBMjwb7j5x4+JP5ejZRLvP9J3aQ6Rh1hA1LFrHRIkBgK8mZJx66'
              b'9pvSipeng4c9V85REpKf65smMMEFwMAb1UTECAAAqhyItp3vvTvoVO7039JiccyxgXAUzMD0yCRSRm1TaDJCTk5Wr6+OMVG'
              b'FTme5hESCJIXEZl1ElH5stHGwAIC6CDLGNfkcJmpl3iBRyaczMpG4pSTyBe2fD+X5Xxa/nBm5TYnrhzz06RdkTP1Y69d7zr'
              b'uK2l4mOWnWbtSboAnK8KjM0AO2pUrZwAMbCQLSO6dAeSIjWi0k7aKhzc2WsQV+fIHkGydAe6iLWc7ybO4Eo9R5YMXNHPcHM'
              b'WVD6VKXAfNhZwBNNuWsg+aySFo5iwcQTNIvgItsvKT5QcmXOE0i2sWIj84yc4ZmDqIiHh/Af4fmQEiuu+MzIinfifNlmOKm'
              b'MnEUsGZcwamWuuQptyrwp8mZwCmyxko9nIiTvUZm3BanYGpZSkRMUEqPIcJLpiOO0xWZwBM1nJKm6amAMDl9ucPCaIbADRV'
              b'nr6I2TEzMB3qX06M5XeqSuI+ZQb4iiTTdnHaxfV+OgPGDDpymXfNf+HDE04E60+QmSlxwFEiCyH/dTo3b2AtdtL+rRZnmha'
              b'nLQopHa2D+eLKm4J1dOu4YSM4ZdA5fj+JfOO0cQbK3o4Y6mCM4pou+0ACJBAEFxM95QtRFN1MkPQgS1OTABoDgOTEiGGSp7'
              b'J6dvmCrKwNiRWVujOQjN0mTWUAcCdy1eD0sJb2p9PhbPlJKmLTgg2iLokEowOXVSXFAGB44LSqJnUhbg6tntGypizZGGhvX'
              b'fISItNTdUPhw5qSZAAQHb4Qi/bo6KWKqkXL3vb46ssLoavCv3DNOxW+gA5ElRP94YOQLi1U5Am3r74ptErnur9mdm1wwWDf'
              b'STk1BkQlL6XMU93Uuf6DuSvfzOR7EYCo99K+8JGvc3W0Pv+sZ1454K9uNZYsjkauXTm742b3z9HbV1QlWYLGBZngD7Q3znu'
              b'ybfmrwRlLdAtIAImxwUM7Ng/3nDJZxVmt69Y9v0t0+Sx1pooST6VGSZNNRhRBA7A3rphvbhGYuQbaskofQpsYAsBc1m2kj4'
              b'LkrhIlnylSRlDk+OkfP7p8dLuVKiJ7aPHry9Zsq/DUFPsdziXVZO3JVQwT2JQsAzhWM9tRKzSkyPGLB7+48MtnejbQWNNMI'
              b'8PnY6M3agIPuz11mcpap9LcyYYQHKrwnWqGMcsMJ2rFDcVjA+cObLt0dLsq52rqTIXbRFp0+OKt3iOC6Pb5Z4qiR4eCtjJZ'
              b'YMh+03h3m87vB6eKakolRvvDv/6x972e83s0JWl7LUyNCVJdsKN1/nNNLWv91S2iqyJd1VW0cBaU28lWTfJvDYwzSdOU1ES'
              b'sf+Dq4d6L+4auH7fAK9Ydlyqq3J6A6PJSwRTDPWQl7m2VcRuqkkhNRJLxSGE79y/Vn68dLIUm2AAAAABJRU5ErkJggg==')
field_cell = tk.PhotoImage(data=b_code)
root.iconphoto(False, field_cell)
window = tk.Frame(borderwidth=0, relief=tk.GROOVE, bg='gray10')  # Создаём фрейм игрового поля
window.pack(anchor='center', fill=tk.BOTH, padx=20, pady=20)
for r in range(3):
    for c in range(3):
        cell_image = tk.Label(window, bg='black', image=field_cell)
        cell_image.grid(row=r, column=c, padx=2, pady=2)

root.mainloop()