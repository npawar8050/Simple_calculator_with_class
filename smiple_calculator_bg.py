class Mathss:
    def __init__(self):
        pass

    def cals(self,s):
        for i in s:
          if i == "+":
            t = s.partition(i)
            return (float(t[0]) + float(t[2]))
          elif i == "-":
            t = s.partition(i)
            return (float(t[0]) - float(t[2]))
          elif i == "*":
            t = s.partition(i)
            return (float(t[0]) * float(t[2]))
          elif i == "/":
            t = s.partition(i)
            return (float(t[0]) / float(t[2]))


if __name__=="__main__":
    while(True):
        Rodger = Mathss()
        s1 = input("Simple calculator : ")
        print(Rodger.cals(s1))
        break