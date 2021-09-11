import matplotlib.pyplot as plt


steps=[]
error=[]
xrroot=[]

# İnput tanımlama
xl = input('İlk tahmin ')
xu = input('İkinci tahmin ')
e = input('Hata toleransı ')

# Floata çevirme
xl = float(xl)
xu = float(xu)
e = float(e)



# Fonksiyon tanımlama
def f(x)
    return 5760x-480

# False position methodu
def FalsepositionMethode(xl,xu,e)
    step = 1

    print('nn False Position Methodu')

    condition = True

    while condition
        
        xr = xl - (xu-xl)  f(xl)( f(xu) - f(xl) )
        print('Iteration-%d, xl = %0.6f,xu = %0.6f,xr = %0.6f,f(xl) = %0.6f,f(xu) = %0.6f , f(xr) = %0.6f, Ea = %0.6f' % (step, xl,xu,xr, f(xl),f(xu),f(xr),abs(f(xr))))

        if f(xl)  f(xr)  0
            xu = xr
        else
            xl = xr
       
        step = step + 1
        xrroot.append(xr)
        steps.append(step)
        error.append(abs(f(xr)))
        
        condition = abs(f(xr))  e
        

    print('nGerekli kök %0.8f' % xr)



if f(xl)  f(xu)  0.0
    print('Verilen değerler ile False Position methodu uygulanamaz.')
    print('Başka değerlerle yeniden deneyin.')
else
    FalsepositionMethod(xl,xu,e)

plt.plot(steps, error)
plt.title(Hata İterasyon Grafiği)
plt.xlabel(steps)
plt.ylabel(error)
plt.show()


plt.plot(steps, xrroot)
plt.title(Kök İteresyon Grafiği)

plt.xlabel(steps)
plt.ylabel(xrroot)
plt.show()
