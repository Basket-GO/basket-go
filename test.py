import interface.test as Interface

a = Interface.Interface(
    button={
        "x": 0,
        "y": 0,
        "img": "./img/Logo.png",
        "img_hover": "./img/Logo.png",
        "hover": False
    },
    background="./img/Logo.png",
    text={
        "x": 0,
        "y": 0,
        "text": "test",
        "font": "test",
        "size": 0,
        "color": (0, 0, 0)
    }
)

a.setup()
