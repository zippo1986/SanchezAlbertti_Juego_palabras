import json
import pygame

nivel_uno_uno=[
        {
            "imagen":"letras_nivel_uno/letra_I.png",
            "etiqueta":"i",
            
            "pos_x": 200, 
            "pos_y": 150,
            
            "ancho": 30, 
            "alto": 30,
            "seleccionada": False,
            
        },
        {
            "imagen": "letras_nivel_uno/letra_T.png",
            "etiqueta":"t",
            "pos_x": 300, 
            "pos_y": 150,
            "ancho": 30, 
            "alto": 30,
            "seleccionada": False,
            

        },

        {"imagen": "letras_nivel_uno/letra_E.png",
            "etiqueta":"e",
            "pos_x": 400, 
            "pos_y": 150,
            "ancho": 30, 
            "alto": 30,
            "seleccionada": False,
            
        },
        {"imagen": "letras_nivel_uno/letra_M.png",
            "etiqueta":"m",
            "pos_x": 500, 
            "pos_y": 150,
            "ancho": 30, 
            "alto": 30,
            "seleccionada":False,
            
        },
        {"imagen": "letras_nivel_uno/letra_O.png",
            "etiqueta":"o",
            "pos_x": 600, 
            "pos_y": 150,
            "ancho": 30, 
            "alto": 30,
            "seleccionada":False,
            
        },
        {"imagen": "letras_nivel_uno/letra_P.png",
            "etiqueta":"p",
            "pos_x": 700, 
            "pos_y": 150,
            "ancho": 30, 
            "alto": 30,
            "seleccionada": False,
            
        }         

        ]   
palabras_uno_nivel =[{"palabra": "pie",
        "es_visible":False,
        "pos_x":400, 
        "pos_y":400, 
        "ancho":50, 
        "alto": 50
},
{"palabra": "miope",
        "es_visible":False,
        "pos_x":400, 
        "pos_y":400, 
        "ancho":50, 
        "alto": 50
},
{"palabra": "tiempo",
        "es_visible":False,
        "pos_x":400, 
        "pos_y":400, 
        "ancho":50, 
        "alto": 50
},
{"palabra": "tipo",
        "es_visible":False,
        "pos_x":400, 
        "pos_y":400, 
        "ancho":50, 
        "alto": 50
},
{"palabra": "mito",
        "es_visible":False,
        "pos_x":400, 
        "pos_y":400, 
        "ancho":50, 
        "alto": 50
},
{"palabra": "item",
        "es_visible":False,
        "pos_x":400, 
        "pos_y":400, 
        "ancho":50, 
        "alto": 50
}
]
nivel_dos_dos=[
        {
            "imagen":"letras_nivel_dos/letra_A.png",
            "etiqueta":"A",
            
            "pos_x": 200, 
            "pos_y": 150,
            
            "ancho": 30, 
            "alto": 30,
            "seleccionada": False,
            
        },
        {
            "imagen": "letras_nivel_dos/letra_T.png",
            "etiqueta":"t",
            "pos_x": 300, 
            "pos_y": 150,
            "ancho": 30, 
            "alto": 30,
            "seleccionada": False,
            

        },

        {"imagen": "letras_nivel_dos/letra_E.png",
            "etiqueta":"e",
            "pos_x": 400, 
            "pos_y": 150,
            "ancho": 30, 
            "alto": 30,
            "seleccionada": False,
            
        },
        {"imagen": "letras_nivel_dos/letra_M.png",
            "etiqueta":"m",
            "pos_x": 500, 
            "pos_y": 150,
            "ancho": 30, 
            "alto": 30,
            "seleccionada":False,
            
        },
        {"imagen": "letras_nivel_dos/letra_R.png",
            "etiqueta":"r",
            "pos_x": 600, 
            "pos_y": 150,
            "ancho": 30, 
            "alto": 30,
            "seleccionada":False,
            
        },
        {"imagen": "letras_nivel_dos/letra_N.png",
            "etiqueta":"n",
            "pos_x": 700, 
            "pos_y": 150,
            "ancho": 30, 
            "alto": 30,
            "seleccionada": False,
            
        }         

        ]   
palabras_dos_nivel =[
{"palabra": "mar",
        "es_visible":False,
        "pos_x":400, 
        "pos_y":400, 
        "ancho":50, 
        "alto": 50
},
{"palabra": "renta",
        "es_visible":False,
        "pos_x":400, 
        "pos_y":400, 
        "ancho":50, 
        "alto": 50
},
{"palabra": "arme",
        "es_visible":False,
        "pos_x":400, 
        "pos_y":400, 
        "ancho":50, 
        "alto": 50
},
{"palabra": "tren",
        "es_visible":False,
        "pos_x":400, 
        "pos_y":400, 
        "ancho":50, 
        "alto": 50
}
]
botones = [
    {
        "imagen": "botones/submit.png",
        "etiqueta": "submit",
        "pos_x":300, 
        "pos_y":400, 
        "ancho":50, 
        "alto": 50

    },
    {
        "imagen": "botones/shaffle.png",
        "etiqueta": "shuffle",
        "pos_x":400, 
        "pos_y":400, 
        "ancho":50, 
        "alto": 50
    },
    {
        "imagen": "botones/clear.png",
        "etiqueta": "clear",
        "pos_x":500, 
        "pos_y":400, 
        "ancho":50, 
        "alto": 50
    }

]
nivel_tres_tres=[
        {
            "imagen":"letras_nivel_tres/letra_C.png",
            "etiqueta":"c",
            
            "pos_x": 200, 
            "pos_y": 150,
            
            "ancho": 30, 
            "alto": 30,
            "seleccionada": False,
            
        },
        {
            "imagen": "letras_nivel_tres/letra_A.png",
            "etiqueta":"a",
            "pos_x": 300, 
            "pos_y": 150,
            "ancho": 30, 
            "alto": 30,
            "seleccionada": False,
            

        },

        {"imagen": "letras_nivel_tres/letra_S.png",
            "etiqueta":"s",
            "pos_x": 400, 
            "pos_y": 150,
            "ancho": 30, 
            "alto": 30,
            "seleccionada": False,
            
        },
        {"imagen": "letras_nivel_tres/letra_O.png",
            "etiqueta":"o",
            "pos_x": 500, 
            "pos_y": 150,
            "ancho": 30, 
            "alto": 30,
            "seleccionada":False,
            
        },
        {"imagen": "letras_nivel_tres/letra_R.png",
            "etiqueta":"r",
            "pos_x": 600, 
            "pos_y": 150,
            "ancho": 30, 
            "alto": 30,
            "seleccionada":False,
            
        },
        {"imagen": "letras_nivel_tres/letra_N.png",
            "etiqueta":"n",
            "pos_x": 700, 
            "pos_y": 150,
            "ancho": 30, 
            "alto": 30,
            "seleccionada": False,
            
        }         

        ]
palabras_tres_nivel =[
{"palabra": "caros",
        "es_visible":False,
        "pos_x":400, 
        "pos_y":400, 
        "ancho":50, 
        "alto": 50
},
{"palabra": "sonar",
        "es_visible":False,
        "pos_x":400, 
        "pos_y":400, 
        "ancho":50, 
        "alto": 50
},
{"palabra": "rosca",
        "es_visible":False,
        "pos_x":400, 
        "pos_y":400, 
        "ancho":50, 
        "alto": 50
},
{"palabra": "sacro",
        "es_visible":False,
        "pos_x":400, 
        "pos_y":400, 
        "ancho":50, 
        "alto": 50
},
{"palabra": "asno",
        "es_visible":False,
        "pos_x":400, 
        "pos_y":400, 
        "ancho":50, 
        "alto": 50
},
{"palabra": "coran",
        "es_visible":False,
        "pos_x":400, 
        "pos_y":400, 
        "ancho":50, 
        "alto": 50
}
]
   





            
                    #// ... otras letras para el nivel 1
                




        # Escribir los datos en un archivo JSON
