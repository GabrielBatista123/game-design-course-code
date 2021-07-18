from GameController import GameController


class Runner:


    def __init__(self):
        self.number_of_games_played = 0
        self.maximum_number_of_days_survided = 0
        self.playing = True

    def play(self):
        print('welcome to Escape Island! ')
        while(self.playing):
            newGame = GameController()
            newGame.play()
            self.save_max_number_of_days(newGame.days)
            self.number_of_games_played += 1
            self.playing = self.ask_to_play_again()

    def ask_to_play_again(self):
        while(True):
            play_again = input('play again? (Y/N)')
            if play_again == 'Y':
                return True
            if play_again == 'N':
                return False
            else:
                print('Invalid input')
        
    def save_max_number_of_days(self, days_survived):
        if days_survived > self.maximum_number_of_days_survided:
            self.maximum_number_of_days_survided = days_survived
        print('you have survived a maximum number of'+str(self.maximum_number_of_days_survided)+'days')
        

