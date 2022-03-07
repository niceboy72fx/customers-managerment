class Customer:
    def __int__(self,name, address,px):
        self.name = name
        self.address = address
        self.px = px

    def getname(self):
        return self.name
    def getaddress(self):
        return self.address
    def getpx(self):
        return self.px * 1234
    def insert(self):
        print("type customer's name :")
        self.name=str(input())
        print("type customer's address: ")
        self.address=str(input())
        print("type number of ampere hour metter ")
        self.px =  int(input())
    def show(self):
        print ("name :" + self.name)
        print ("address : " + self.address)
        print ("price :" , self.getpx())
class NewCustomer (Customer):
    def __int__(self):
        super(Customer,self).__init__()
    def insert(self):
        super(Customer, self).insert()
    def show(self):
        super(Customer, self).show()
if __name__ == "__main__":
    cs = Customer()
    nc = NewCustomer()
    cus_list = []
    new_list = []
    n = int(input())
    i = int(input())
    while True:
      print("\n 1. insert old customer")
      print("\n 2. insert new customer")
      print("\n 3. view old customer")
      print("\n 4. view new customer")
      match  i:
          case 1 :
            for i in range (n):
                  cs.insert()
                  cus_list.append(cs)
                  print("\n ------------------------ \n")

            break
          case 2:
            for i in range(n):
                   nc.insert()
                   new_list.append(nc)
                   print("\n ------------------------ \n")
                   i = 0
            break
          case 3:
              if (len(cus_list) == 0):
                  print("array not set please return")
                  break
              else:
                 for i in range(len(cus_list)):
                      cs.show()
                      print("\n ------------------------ \n")
                      print("\n type 0 to return ")
              i = int(input())
              break
          case 4:
              if (len(new_list) == 0):
                  print("array not set please return")
                  break
              else:
                  for i in range(len(new_list)):
                       nc.show()
                       print("\n ------------------------ \n")
                       print("\n type 0 to return ")
              i = int(input())
              break
      if (i<0 or i >5):
          print("choose another one")
          break
