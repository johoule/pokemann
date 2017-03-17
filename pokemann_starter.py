import random

'''look at his github to get completed code up to this point'''

class Pokemann:

    def __init__(self, name, kind, attack, defense, speed, health, catch_rate, moves, image):

        self.name = name
        self.kind = kind
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.health = health
        self.catch_rate = catch_rate
        self.moves = moves # this is a list of Move objects
        self.image = image # path to image file

        self.fainted = False
        self.current_health = health

    def get_available_moves(self):
        result = []

        for m in self.moves:
            if m.remaining_power > 0:
                result.append(m)

        return result

    def execute_move(self, move, target):
        available = self.get_available_moves()

        if self.fainted:
            print("Error: " + self.name + " is fainted!")
        elif move not in available:
            print("Error: " + move.name + " is not available.")
        else:
            r = random.randint(1, 100)

            if r <= move.accuracy:
                damage = move.calculate_damage(self, target)
                print(self.name + " hits " + target.name + " with " + move.name + " for " + str(damage) + ".")
                target.take_damage(damage)
            else:
                print("you missed")

            move.remaining_power -= 1

        

    def take_damage(self, amount):
        self.current_health -= amount

        if self.current_health <= 0:
            self.faint()

    def faint(self):
        self.current_health = 0
        print(self.name + " fainted!")
        self.fainted = True
        
    def heal(self, amount):
        '''
        Restores all health and resets powerpoint for all moves.
        '''
        self.current_health += amount

        if self.current_health > self.health:
            self.current_health = self.health

        self.fainted = False

    def restore(self):
        '''
        restores all health and resets powerpoint for all moves.
        '''
        self.current_health = self.health

        for m in self.moves:
            m.restore()

        self.fainted = False

    def draw(self):
        pass


class Move:

    STRONG = 2.0
    NORMAL = 1.0
    WEAK = 0.5

    effectiveness = {
        ('student', 'admin'): WEAK,
        ('student', 'student'): NORMAL,
        ('student', 'teacher'): STRONG,
        ('teacher', 'student'): WEAK,
        ('teacher', 'teacher'): NORMAL,
        ('teacher', 'admin'): STRONG,
        ('admin', 'teacher'): WEAK,
        ('admin', 'admin'): NORMAL,
        ('admin', 'student'): STRONG
        }


    def __init__(self, name, kind, powerpoint, power, accuracy):

        self.name = name
        self.kind = kind
        self.powerpoint = powerpoint
        self.power = power
        self.accuracy = accuracy

        self.remaining_power = powerpoint


    

    def calculate_damage(self, attacker, target):
        
        p = self.power
        a = attacker.attack
        d = target.defense
        e = self.effectiveness[(self.kind, target.kind)]

        return p * a / d * e

    def restore(self):
        '''
        Resets remaing_power to starting powerpoint.
        '''

        self.remaining_power = self.powerpoint

            

class Character:

    def __init__(self, name, pokemann, image):
        self.name = name
        self.pokemann = pokemann
        self.image = image

    def get_available_pokemann(self):
        '''Returns a list of all unfainted pokemann belonging to a character.'''
        result = []

        for p in self.pokemann:
            if p.fainted == False:
                result.append(p)

        return result

    def get_active_pokemann(self):
        '''Returns the first [0] unfainted character in the pokemann list'''
        available = self.get_available_pokemann()

        if len(available) > 0:
            return pokemann[0]
        else:
            return none

    def set_first_pokemann(self, swap_pos):
        '''Moves pokemann to first position [0] in the pokemann list by exchanging
           it with pokemann located at swap_pos. '''
        pass

    def restore(self):

        for p in self.pokemann:
            p.restore()

    def draw(self):
        pass


class Player(Character):

    def __init__(self, name, pokemann, image):
        Character.__init__(self, name, pokemann, image)
        
        self.collection = []
        self.pokeballs = 0

    def catch(self, target):
        '''
        Can only be applied to a wild pokemann. determine a catch b generating a random value and camparing
        it to the catch_rate. if a catch is successfull, append the target to the palyer's pokemann list.
        however, if the pokemann list already contains 6 pokemann, add the caught target to the players computer
        instead. pokemann sent to the computer will be fully restored, but other caught pokemann will remain at the
        strength they were caught. decrease the player's pokeball count by 1 regardless of success.

        return true if the catch is successfull and false otherwise
        '''

        r = random.randint(1, 100)
        
        if r <= target.catch_rate:
            pass
        else:
            print("It got away!")
            return False

    def run(self, target):
        '''
        can only be applied in the presence of a wild pokemann. success is determined by coparing speeds
        of the player's active pokemann and the wild pokemann. incoroportate randomness so that speed is
        not the only factor determining success.

        return true if the escape is successful and false otherwise.
        '''
        pass

class NPC(Character):

    def __init__(self, name, pokemann, image):
        Character.__init__(self, name, pokemann, image)


class Game:

    def __init__(self):
        pass

    def select_pokemann(self, character):
        '''
        1) Generate a menu which shows a numbered list of all characters along
           with status (health)
        2) Have the player select a character
        3) Move the selected character to position [0] in the characters list
        '''
        pass

    def select_random_pokemann(self, pokemann):
        '''
        Returns a random available move from the pokemann. this will probably
        only be used by computer controlled pokemann.
        '''
        available_moves = Pokemann.get_available_moves()
        return random.choice(available_moves)

    def select_move(self, pokemann):
        '''
        1) Generate a menu which shows a numbered list of all available moves
           for a pokemann.
        2) Have the player select a move.
        3) Return the selected move.
        '''

        available = pokemann.get_available_moves()

        print("Select a move:")

        for i, move in enumberate(available):
            print(str(i) + ") " + move.name)

        n = input("Your choice: ")
        n = int(n)

        return available[n]

    def select_random_move(self, pokemann):
        '''
        Returns a random available move from the pokemann. this will probably
        only be used by computer controlled pokemann.
        '''
        pass

    def fight(self, player_pokemann, target_pokemann):
        '''
        This controls the logic for a single round in a fight whether in context
        of a battle of with a wild pokemann.

        1. select player move ( use select_move)
        2. select target_move ( use select_random_move)
        3. compare speeds of player_pokemann and target_pokemann
             if player_pokemann.speed > target_pokemann.speed, set
             first = player_pokemann, second = target_pokemann. otherwise, set
             first = target_pokemann, second = player_pokemann. if speed is
             equal, assign first and second randomly
        4.call
             first.exevute_move(move, second)
        5. if second is still unfainted, call
             second.exevute_move(move, first)

        (once we have an actual game, we'll need to devise a way to remove fainted targets)
        '''
        pass

    def catch(self, target):
        '''
        Can only be applied to wild pokemann. Determine a catch by generatin a
        random value based on the target health. if a catch is successful, add
        the target to the player's collection. decrease the palyer's pokeball
        count by 1 regardless of success. (perhaps pokeballs kind could be
        incorporated into the probability at some point.)
        '''
        pass

    def encounter(self, player, target):
        '''
        this function controls all logic when encountering a wild pokemann.
        options are to fight, catch, or ignore.

        use a loop so that this continues until a pokemann is fainted, caught,
        or the target is ignored.
        '''
        pass

    def battle(self, player, opponent):
        '''
        function contals all battle logic including decisions to reorder
        pokemann, fight, use potions, and whatever else happens in pokebattles

        use a loop so that this continues until all characters for either the player
        of opponent are fainted.
        '''
        pass

    def loop(self):
        pass

        #get input

        # do logic stuff

        # draw stuff

        
        
   

if __name__ == '__main__':

    '''change the moves and the pokemann to be revelant to your game'''

    # Make some moves
    homework = Move("Homework", "teacher", 30, 40, 100)
    pop_quiz = Move("Pop quiz", "teacher", 30, 40, 100)
    lecture = Move("Lecture", "teacher", 30, 40, 100)
    nonsense_notes = Move("Nonsense Notes", "teacher", 30, 40, 100)
    smart_remarks = Move("Smart Remarks", "teacher", 5, 40, 100)
    student_news = Move("Student News", "teacher", 5, 40, 100)
    complicated_project = Move("Complicated Project", "teacher", 30, 40, 100)
    poke_fun = Move("Poke Fun", "teacher", 30, 40, 100)
    memes = Move("Memes", "teacher", 30, 40, 100)
    
    dress_code = Move("Dress Code", "admin", 30, 50, 95)
    id_violation = Move("ID Violation", "admin", 30, 50, 95)
    nonsense = Move("Makes No Sense", "admin", 30, 50, 100)
    lack_info = Move("Lacks Needed Important Info", "admin", 30, 50, 100)
    no_tech = Move("Is Terrible at the technologies", "admin", 30, 50, 100)
    tackle = Move("Tackle", "admin", 30, 50, 100)
    take_down = Move("Take Down", "admin", 30, 50, 100)
    body_slam = Move("Body Slam", "admin", 30, 50, 100)
    
    
    excessive_talking = Move("Excessive Talking", "student", 30, 40, 100)
    disruptive_behavior = Move("Disruptive Behavior", "student", 30, 40, 100)
    dabbing = Move("Excessive Dabbing", "student", 30, 40, 100)
    un_still = Move("Unable to Sit Still", "student", 30, 40, 100)


    # Create some Pokemann(s)
    coopasaur = Pokemann("coopasaur", "teacher", 30, 20, 50, 30, 90,[homework, pop_quiz, id_violation], "coopasaur.png")#
    cookmander = Pokemann("Cookmander", "teacher", 30, 20, 50, 100, 90, [lecture, id_violation, homework], "cookmander.png")#
    vincolairy = Pokemann("Vincolairy", "teacher", 30, 20, 50, 120, 90, [lecture, id_violation, homework], "vincolairy.png")#
    cooper = Pokemann("Cooper", "teacher", 30, 20, 50, 120, 90, [complicated_project, poke_fun, memes], "cooper.png")
    linn = Pokemann("Linn", "teacher", 30, 20, 50, 30, 90, [nonsense_notes, smart_remarks, student_news], "linn.png")

    holland = Pokemann("Holland", "admin", 30, 20, 30, 50, 90, [tackle, take_down, body_slam], "holland.png")
    downs = Pokemann("Downs", "admin", 30, 20, 50, 30, 90, [nonsense, lack_info, no_tech], "downs.png")
    mayfieldarow = Pokemann("mayfieldarow", "admin", 30, 20, 50, 30, 90, [dress_code, id_violation, lecture], "mayfieldarow.png")#
    
    andrewag = Pokemann("andrewag", "student", 30, 20, 50, 30, 90, [excessive_talking, disruptive_behavior, homework], "andrewag.png")#
    caseypuff = Pokemann("Caseypuff", "student", 30, 20, 50, 170, 90, [excessive_talking, disruptive_behavior, homework], "caseypuff.png")#
    colboreon = Pokemann("Colboreon", "student", 30, 20, 50, 80, 90, [excessive_talking, disruptive_behavior, homework], "colboreon.png")#
    blakachu = Pokemann("Blakachu", "student", 30, 20, 50, 130, 90, [excessive_talking, disruptive_behavior, homework], "blakachu.png")#
    zoeotto = Pokemann("Zoeotto", "student", 30, 20, 50, 100, 90, [excessive_talking, disruptive_behavior, homework], "zoeotto.png")#
    morganyta = Pokemann("Morganyta", "student", 30, 20, 50, 160, 90, [excessive_talking, disruptive_behavior, homework], "morganyta.png")#
    katlevee = Pokemann("Katlevee", "student", 30, 20, 50, 140, 90,[excessive_talking, disruptive_behavior, homework], "katlevee.png")#
    marcelax = Pokemann("Marcelax", "student", 30, 20, 50, 30, 90, [excessive_talking, disruptive_behavior, homework], "marcelax.png")#
    chriskyle = Pokemann("ChrisKyle", "student", 30, 20, 50, 30, 90, [excessive_talking], "chriskyle.png")
    river = Pokemann("River", "student", 30, 20, 50, 30, 90, [excessive_talking, dabbing, un_still], "river.png")
    

    #Create Player

    pat = Player("Pat riotum", [coopasaur, andrewag, caseypuff, blakachu], "pat.png")

    #creat Opponents
    rocket = NPC("Team Rocket", [zoeotto, morganyta, cookmander], "rocket.png")
    jessie = NPC("Jessie", [vincolairy, mayfieldarow, katlevee, marcelax], "jessie.png")

    # create a game

    #g = Game()
