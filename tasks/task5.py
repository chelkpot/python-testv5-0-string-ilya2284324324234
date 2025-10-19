# tasks/task5.py

def solve():
# Ниже пишите решение задачи
    a, b, t = map(str, input().split())
    z=(ord(a))
    x=(ord(b))
    c=(ord(t))
    q=a 
    w=b
    e=t
    print("Код символа " + str(q)+ "равен" + str(z) + '\n' "Код символа " + str(w)+ "равен" + str(x) + '\n' "Код символа " + str(e)+ "равен" + str(c))
    
   
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()