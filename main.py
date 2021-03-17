naim = sprites.create(img("""
        . . . . . . 5 . 5 . . . . . . . 
            . . . . . f 5 5 5 f f . . . . . 
            . . . . f 1 5 2 5 1 6 f . . . . 
            . . . f 1 6 6 6 6 6 1 6 f . . . 
            . . . f 6 6 f f f f 6 1 f . . . 
            . . . f 6 f f d d f f 6 f . . . 
            . . f 6 f d f d d f d f 6 f . . 
            . . f 6 f d 3 d d 3 d f 6 f . . 
            . . f 6 6 f d d d d f 6 6 f . . 
            . f 6 6 f 3 f f f f 3 f 6 6 f . 
            . . f f d 3 5 3 3 5 3 3 f f . . 
            . . f d f f 3 5 5 3 f d f . . . 
            . . . f f 3 3 3 3 3 f d f . . . 
            . . . f 3 3 5 3 3 5 3 f f . . . 
            . . . f f f f f f f f f . . . . 
            . . . . . f f . . . . . . . . .
    """),
    SpriteKind.player)
controller.move_sprite(naim, 100, 100)
scene.set_background_image(assets.image("""
    idk
"""))
tiles.set_tilemap(tilemap("""
    level1
"""))