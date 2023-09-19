da=[
    (2212,123),(123,123)
]
def log(us,pas):
    for i in da:
        if(i[0]==us and i[1]==pas):
            print("YES")

log(123,123)