class Race:

    def __init__(self, race_name, race_subcategory, scores_increase, age, size, speed, languages, abilities, proficiencies):
        self.race_name = race_name
        self.race_subcategory = race_subcategory
        self.scores_increase = scores_increase
        self.age = age
        self.size = size
        self.speed = speed
        self.languages = languages
        self.abilities = abilities
        self.proficiencies = proficiencies

dragonborn = [
    {"Race Name" : "Dragonborn"},
    {"Race Subcategory" : ["Black", "Blue", "Brass", "Bronze", "Copper", "Gold", "Green", "Red", "Silver", "White"]},
    {"Scores Increase" : [{"strength" : 1}, {"charisma" : 1}]},
    {"Age" : 15},
    {"Size" : "Medium"},
    {"Speed" : 30},
    {"Languages" : ["Common", "Draconic"]},
    {"Abilities" :  
                    [
                        {"Damage Resistance" : 
                            [
                                {"Black" : "Acid"},
                                {"Blue" : "Lightning"},
                                {"Brass" : "Fire"},
                                {"Bronze" : "Lightning"},
                                {"Copper" : "Acid"},
                                {"Gold" : "Fire"},
                                {"Green" : "Poison"},
                                {"Red" : "Fire"},
                                {"Silver" : "Cold"},
                                {"White" : "Cold"}
                            ]
                        },

                        {"Breath Weapon" :
                            [
                                {"Black" : "5 by 30 ft. line (Dex. save)"},
                                {"Blue" : "5 by 30 ft. line (Dex. save)"},
                                {"Brass" : "5 by 30 ft. line (Dex. save)"},
                                {"Bronze" : "5 by 30 ft. line (Dex. save)"},
                                {"Copper" : "5 by 30 ft. line (Dex. save)"},
                                {"Gold" : "15 ft. cone (Dex. save)"},
                                {"Green" : "15 ft. cone (Con. save)"},
                                {"Red" : "15 ft. cone (Dex. save)"},
                                {"Silver" : "15 ft. cone (Con. save)"},
                                {"White" : "15 ft. cone (Con. save)"}
                            ]
                        }
                    ]
    }
]

dwarf = [
    {"Race Name" : "Dwarf"},
    {"Race Subcategory" : ["Hill Dwarf", "Mountain Dwarf"]},
    {"Scores Increase" : 
        [
            {"Hill Dwarf" :
                [
                    {"constitution" : 2}, 
                    {"charisma" : 1},
                    {"strength" : 1}
                ]
            },
            {"Mountain Dwarf" :
                [
                    {"constitution" : 2}, 
                    {"charisma" : 1},
                    {"wisdom" : 1},
                    {"toughness" : 1}
                ] 
            },
        ]
    },
    {"Age" : 15},
    {"Size" : "Medium"},
    {"Speed" : 30},
    {"Languages" : 
        ["Common", "Dwarvish"]},
    {"Abilities" :  
        [
            "Darkvision",
            "Dwarven Resilience"
            "Stonecunning"
        ]
    },
    {"Proficiencies" : 
        [
            {"Weapons" : ["battleaxe", "handaxe", "light hammer", "war hammer"]},
            {"Tools" : ["smith", "brewer", "mason"]}
        ]

    }
]

elf = [
    {"Race Name" : "Elf"},
    {"Race Subcategory" : ["High Elf", "Wood Elf"]},
    {"Scores Increase" : 
        [
            {"High Elf" :
                [
                    {"dexterity" : 1}, 
                    {"intelligence" : 1},
                ]
            },
            {"Wood Elf" :
                [
                    {"dexterity" : 1}, 
                    {"wisdom" : 1},
                ] 
            },
        ]
    },
    {"Age" : 15},
    {"Size" : "Medium"},
    {"Speed" : 
        [
            {"High Elf" : 30},
            {"Wood Elf" : 35}
        ] 
    },
    {"Languages" : 
        [
            {"High Elf" : ["Common", "Elvish", "Undecided"]},
            {"Wood Elf" : ["Common", "Elvish"]}
        ] 
    },
    {"Abilities" :  
        [
            "Darkvision",
            "Fey Ancestry"
            "Trance"
        ]
    },
    {"Proficiencies" : 
        [
            {"Weapons" : ["longsword", "shortsword", "shortbow", "longbow"]},
            {"Skills" : ["perception"]}
        ]

    }
]
