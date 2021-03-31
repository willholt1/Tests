def look(self, food):
        if ((self.center_y <= food.center_y <= (self.center_y + self.viewDistance)) and ((self.center_x - 5) <= food.center_x <= (self.center_x + 5))):
            self.direction = 'U'
            self.foraging = True
        elif (((self.center_y - self.viewDistance) <= food.center_y <= self.center_y) and ((self.center_x - 5) <= food.center_x <= (self.center_x + 5))):
            self.direction = 'D'
            self.foraging = True
        elif (((self.center_x - self.viewDistance) <= food.center_x <= self.center_x) and ((self.center_y - 5) <= food.center_y <= (self.center_y + 5))):
            self.direction = 'L'
            self.foraging = True
        elif ((self.center_x <= food.center_x <= (self.center_x + self.viewDistance)) and ((self.center_y - 5) <= food.center_y <= (self.center_y + 5))):
            self.direction = 'R'
            self.foraging = True
        else:
            self.foraging = False


    def checkEat(self, food):
        #check if can eat any food
        for i in range (len(food)):
            distance = math.sqrt( (food[i].center_x - self.center_x)**2 + (food[i].center_y - self.center_y)**2 )
            #if food is close, eat
            if (distance <= 10):
                self.eat(food[i])
                food.remove(food[i])
                self.foraging = False
                break
            #if no food spotted, look for food                
            elif (self.foraging == False):
                self.look(food[i])
        return food