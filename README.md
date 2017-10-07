# Tamagotchi
Simple python implementation of Tamagotchi

#Install
```pip install -r requirements.txt```

#Play
Change directory to game, run ```python game.py```, you will enter an IPython interactive interface. The game starts here.

##Basic pet
The basic pet has only one metric, hunger. By feeding it, the hunger metric will increase. This pet will not die even if the hunger became negative.

* create a basic pet: in IPython interface, enter:
```pokemon = BasicPet()```
  a basic pet called pokemon is created.

* to start playing the game, type in: 
 ```start_play(pokemon)```

By this time, a figure generated by Matplotlib will come to your screen, the big blue bar indicate the hunger metric, the lower the bar, the hungery your pet.

* feeding will increase the hunger value, go back to command line:
```pokemon.feed()```

Basic pet is the only type supported in 1st release which contains only 4 files. This version is a minimal workable product.