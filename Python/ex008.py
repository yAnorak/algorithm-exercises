n = float(input('Insira uma distancia em metros: '))
print('A distância de {}M corresponde a:'.format(n))
km = n / 1000
hm = n / 100
dam = n / 10
dm = n * 10
cm = n * 100
mm = n * 1000
print('{}Km --- {}dm'.format(km, dm))
print('{}Hm --- {}cm'.format(hm, cm))
print('{}Dam --- {}mm'.format(dam, mm))