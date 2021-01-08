def on_button_pressed():
    global projectile2
    projectile2 = sprites.create_projectile_from_sprite(img("""
            . . . . . . 6 2 6 . . . . . . . 
                    . . . . . . 6 2 6 . . . . . . . 
                    . . . . . . 3 2 5 . . . . . . . 
                    . . . . . . 3 2 5 . . . . . . . 
                    . . . . . . 3 2 5 . . . . . . . 
                    . . . . . . 3 2 2 . . . . . . . 
                    . . . . . . 3 2 2 . . . . . . . 
                    . . . . . . 2 2 2 . . . . . . . 
                    . . . . . . 2 2 2 . . . . . . . 
                    . . . . . . 2 2 2 . . . . . . . 
                    . . . . . . 2 2 2 . . . . . . . 
                    . . . . . . 2 2 2 . . . . . . . 
                    . . . . . . 2 2 2 . . . . . . . 
                    . . . . . . 6 2 6 . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        mySprite,
        0,
        -140)
controller.any_button.on_event(ControllerButtonEvent.PRESSED, on_button_pressed)

def on_on_overlap(sprite, otherSprite):
    otherSprite.destroy(effects.disintegrate, 500)
    info.change_score_by(1)
    if True:
        pass
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap)

def on_on_overlap2(sprite, otherSprite):
    otherSprite.destroy(effects.disintegrate, 500)
    info.change_life_by(-1)
    music.stop_all_sounds()
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

mySprite2: Sprite = None
projectile2: Sprite = None
mySprite: Sprite = None
effects.confetti.start_screen_effect()
info.set_life(1)
mySprite = sprites.create(img("""
        . . . . . . . c d . . . . . . . 
            . . . . . . . c d . . . . . . . 
            . . . . . . . c d . . . . . . . 
            . . . . . . . c b . . . . . . . 
            . . . . . . . f f . . . . . . . 
            . . . . . . . c 6 . . . . . . . 
            . . . . . . . f f . . . . . . . 
            . . . . . . . 8 6 . . . . . . . 
            . . . . . . 8 8 9 8 . . . . . . 
            . . . . . . 8 6 9 8 . . . . . . 
            . . . . . c c c 8 8 8 . . . . . 
            . . . . 8 8 6 6 6 9 8 8 . . . . 
            . . 8 f f f c c e e f f 8 8 . . 
            . 8 8 8 8 8 8 6 6 6 6 9 6 8 8 . 
            8 8 8 8 8 8 8 8 6 6 6 9 6 6 8 8 
            8 8 8 8 8 8 8 8 6 6 6 6 9 6 8 8
    """),
    SpriteKind.player)
mySprite.set_flag(SpriteFlag.STAY_IN_SCREEN, True)
mySprite.top = 120
controller.move_sprite(mySprite)
message = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . 8 8 . . . . 8 8 . . . . 
            . . . 8 8 . 8 . . 8 . 8 8 . . . 
            . . 8 . . . . 8 8 . . . . 8 . . 
            . . 8 . . 8 . . . . 8 . . 8 . . 
            . . 8 . . 8 8 8 8 8 8 . . 8 . . 
            . . 8 . . . . . . . . . . 8 . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.projectile)
message.top = 0
message.say("Level:HARD")
print("Shown message")

def on_update_interval():
    global mySprite2
    mySprite2 = sprites.create(img("""
            . . 2 2 b b b b b . . . . . . . 
                    . 2 b 4 4 4 4 4 4 b . . . . . . 
                    2 2 4 4 4 4 d d 4 4 b . . . . . 
                    2 b 4 4 4 4 4 4 d 4 b . . . . . 
                    2 b 4 4 4 4 4 4 4 d 4 b . . . . 
                    2 b 4 4 4 4 4 4 4 4 4 b . . . . 
                    2 b 4 4 4 4 4 4 4 4 4 e . . . . 
                    2 2 b 4 4 4 4 4 4 4 b e . . . . 
                    . 2 b b b 4 4 4 b b b e . . . . 
                    . . e b b b b b b b e e . . . . 
                    . . . e e b 4 4 b e e e b . . . 
                    . . . . . e e e e e e b d b b . 
                    . . . . . . . . . . . b 1 1 1 b 
                    . . . . . . . . . . . c 1 d d b 
                    . . . . . . . . . . . c 1 b c . 
                    . . . . . . . . . . . . c c . .
        """),
        SpriteKind.enemy)
    mySprite2.set_position(randint(0, 160), 0)
    mySprite2.set_velocity(0, 50)
game.on_update_interval(1000, on_update_interval)
