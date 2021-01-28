
class Population():

    def __init__(self,name,size):
        self.name=name
        self.size=size
        self.growth_rate=1#default
        print(self.name+" population of size",self.size)

    def set_growth_rate(self,growth_rate):
        self.growth_rate=growth_rate
        print("growth rate is set to",self.growth_rate)
    
    def calc_growth(self,numberOfYears):
        if numberOfYears==0:
            return self.size
        else:
            return self.calc_growth(numberOfYears-1)

    def grow(self,years):
        
        if years==0:
            print(self.name+" population of size ",self.size)
            return self.size
            
        else:
            self.size=self.size*self.growth_rate
            return self.grow(years-1)
            


    def shrink(self,decrease):
        self.size=self.size-decrease
        print(self.size)
        
        


 

my_pop=Population("bear",100)
my_pop.set_growth_rate(2)
my_pop.grow(3)
my_pop.shrink(300)



