class SuperHero:
    people = "people"
    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase
    def names(self):
        print("Name:", self.name)
    
    def hitpoints(self):
        self.health_points = self.health_points * 2 
        print(self.health_points, "HP")    
        
    def __str__(self) -> str:
        return f"Nickname: {self.nickname} \n"\
            f"Superpower: {self.superpower}\n"\
            f"HP: {self.health_points} "    
    
    def __len__(self):
        return len(self.catchphrase)
    
    
a = SuperHero("Ei","Raiden Shogun","Secret Art: Musou Shinsetsu",15460,"You will be inlaid upon this statue.")
# a.names()
# a.hitpoints()
# print(a)
# print(len(a))