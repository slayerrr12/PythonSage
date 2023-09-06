x = [(1,"inbox"),(2,"div"),(8,"long"),(19,"sick"),(3,"long")]

y = list ( filter(lambda a : a[0] > 10 , x))

print(y)