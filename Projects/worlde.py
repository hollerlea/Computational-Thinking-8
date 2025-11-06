import random

# Pick a word at random
word_list = ["loopy","heart","audio","laugh","trial", "mason", "athel", "bathe", "ethel", "ether", "hithe", "ither", "kithe", "kythe", "lathe", "lethe", "lithe", "lythe" "apple", "chair", "table", "house", "river", "light", "bread", "plant", "beach", "laugh", "crisp", "blaze", "froth", "minty", "swirl", "grain", "knoll", "quilt", "prism", "storm", "tiger", "zebra", "goose", "shark", "otter", "black", "white", "green", "mauve", "coral", "climb", "smile", "break", "write", "dream", "clock", "phone", "brush", "glass", "couch", "flame", "sugar", "world", "peace", "heart", "stone", "sweet", "music", "spice", "bloom", "fancy", "gleam", "honey", "lunar", "ocean", "pearl", "royal", "sheep", "vivid", "wheat", "youth", "angel", "berry", "cloud", "dance", "ember", "fairy", "grape", "hover", "jelly", "karma", "lemon", "magic", "nylon", "oasis", "piano", "queen", "raven", "silky", "tulip", "unity", "vapor", "whale", "xenon", "yield", "zesty""apple", "chair", "table", "house", "river", "light", "bread", "plant", "beach", "laugh", "crisp", "blaze", "froth", "minty", "swirl", "grain", "knoll", "quilt", "prism", "storm", "tiger", "zebra", "goose", "shark", "otter", "black", "white", "green", "mauve", "coral", "climb", "smile", "break", "write", "dream", "clock", "phone", "brush", "glass", "couch", "flame", "sugar", "world", "peace", "heart", "stone", "sweet", "music", "spice", "bloom", "fancy", "gleam", "honey", "lunar", "ocean", "pearl", "royal", "sheep", "vivid", "wheat", "youth", "angel", "berry", "cloud", "dance", "ember", "fairy", "grape", "hover", "jelly", "karma", "lemon", "magic", "nylon", "oasis", "piano", "queen", "raven", "silky", "tulip", "unity", "vapor", "whale", "xenon", "yield", "zesty", "amber", "blush", "cider", "daisy", "eager", "flint", "giddy", "hatch", "ivory", "joint", "kneel", "latch", "mirth", "noble", "olive", "perch", "quake", "rally", "scoop", "torch", "umbra", "vigor", "woven", "xerox", "young", "zonal", "acorn", "beech", "crown", "drove", "eagle", "flair", "glide", "haste", "inlet", "jazzy", "kayak", "lobby", "mango", "nudge", "orbit", "plume", "quirk", "roast", "shade", "thick", "udder", "vixen", "wrath", "xylem", "yacht", "zebra", "adore", "bloom", "clerk", "drift", "exile", "frost", "glare", "haunt", "irony", "jumbo", "koala", "lunar", "mimic", "ninth", "opine", "proud", "quake", "rider", "shiny", "tough", "urban", "vocal", "wrist", "xenon", "yeast", "zesty", "amber", "blink", "crave", "dwell", "elate", "fluke", "grind", "honey", "inbox", "joker", "knead", "linen", "mover", "naval", "ounce", "prawn", "quack", "raven", "siren", "tiger", "ultra", "viper", "widen", "xenon", "yield", "zonal", "alloy", "banjo", "cider", "dandy", "entry", "fable", "glint", "harsh", "icily", "juicy", "kiosk", "loyal", "mason", "nifty", "onion", "picky", "quilt", "risky", "shard", "trunk", "usage", "vivid", "wheat", "xerox", "young", "zippy", "amber", "beard", "crisp", "dairy", "empty", "faint", "giant", "hasty", "index", "jolly", "knack", "lapse", "moral", "nurse", "oxide", "plush", "quiet", "rugby", "stony", "tulip", "vague", "witty", "xenon", "yodel", "zebra", "annex", "bliss", "crane", "dodge", "easel", "finer", "grape", "haste", "inert", "jewel", "knelt", "leash", "mourn", "niche", "olive", "punch", "quest", "rusty", "swoop", "tamer", "vapor", "woven", "wrist", "xylem", "yeast", "zesty", "axial", "brave", "clash", "drape", "elate", "feast", "gloom", "hound", "irate", "joker", "kneel", "lumen", "mimic", "nerdy", "opium", "petal", "quail", "rough", "sneak", "throb", "vocal", "whisk", "xerox", "youth", "zonal", "awoke", "blaze", "cried", "drain", "eager", "flair", "grind", "harpy", "ideal", "jazzy", "knead", "lemon", "mourn", "nerve", "optic", "prawn", "quiet", "raven", "sheer", "tough", "unite", "viper", "widen", "xenon", "yield", "zippy""abide", "actor", "adorn", "affix", "agile", "alarm", "alien", "amend", "ample", "arena",
"argue", "arise", "audio", "avail", "awake", "badge", "baker", "banal", "barge", "basil",
"basin", "batch", "beady", "beard", "began", "begin", "belly", "berth", "bible", "binge",
"black", "blame", "blank", "bland", "blast", "blend", "bless", "blind", "blink", "block",
"blood", "bloom", "board", "boost", "brace", "braid", "brain", "brand", "brave", "brawl",
"bread", "break", "breed", "bribe", "brick", "bride", "bring", "broad", "broke", "brown",
"brush", "buddy", "build", "bunch", "burly", "cabin", "cable", "cactus", "calm", "camel",
"candy", "canal", "chant", "chaos", "chart", "chase", "cheap", "cheek", "cheer", "chess",
"chill", "choir", "choke", "chord", "chore", "civic", "claim", "clash", "clasp", "class",
"clean", "clear", "clerk", "click", "cliff", "cloak", "clock", "clone", "close", "cloth",
"cloud", "coach", "coast", "cough", "count", "cover", "crawl", "crazy", "cream", "creek",
"creep", "crime", "crisp", "crook", "cross", "crowd", "crown", "cruel", "crush", "crypt",
"cubic", "curse", "curve", "cycle", "daily", "dairy", "dance", "dealt", "death", "debug",
"delay", "demon", "dense", "depth", "devil", "diary", "digit", "diner", "dirty", "dolly",
"donor", "doubt", "dozen", "draft", "drain", "drama", "dream", "dress", "drift", "drink",
"drive", "drown", "drunk", "dryly", "druid", "eager", "early", "earth", "easel", "elder",
"elect", "elite", "empty", "enact", "enemy", "enjoy", "enter", "equal", "equip", "erase",
"error", "essay", "event", "every", "exact", "exalt", "excel", "exist", "expel", "extra",
"fable", "facet", "faint", "fairy", "faith", "fancy", " fatal", "favor", "feast", "feign",
"fella", "ferry", "fibre", "field", "fifth", "fifty", "fight", "final", "finch", "floor",
"flora", "floss", "fluid", "focus", "force", "forge", "forty", "found", "frame", "fraud",
"fresh", "fried", "front", "frost", "fruit", "fudge", "fully", "furry", "fused", "gamer",
"gamma", "gauge", "gears", "ghost", "giant", "girly", "given", "glade", "glare", "glass",
"glide", "gloom", "glory", "gloss", "godly", "grade", "grain", "grand", "grant", "grape",
"graph", "grasp", "grass", "grave", "gravy", "greed", "green", "greet", "grief", "grind",
"groan", "groom", "group", "growl", "guard", "guess", "guest", "guide", "guild", "habit",
"hairy", "halve", "happy", "harsh", "haste", "hatch", "haunt", "haven", "heavy", "hinge",
"hobby", "honey", "honor", "horse", "hostel", "hotel", "house", "human", "humid", "hurry",
"ideal", "image", "imply", "inbox", "inner", "input", "irony", "issue", "ivory", "jelly",
"jewel", "joint", "judge", "juice", "knife", "knock", "known", "label", "labor", "laser",
"later", "laugh", "layer", "learn", "least", "leave", "legal", "light", "limit", "linen",
"liver", "loyal", "lunge", "magic", "major", "maker", "march", "match", "mayor", "medal",
"meter", "micro", "might", "minor", "model", "moral", "moron", "motor", "mount", "mouth",
"movie", "music", "naive", "naked", "nasty", "naval", "nerve", "never", "noble", "noise",
"north", "notch", "novel", "nurse", "ocean", "offer", "often", "omega", "onion", "order",
"organ", "other", "ought", "ounce", "outer", "pause", "peace", "phase", "phone", "piano",
"pilot", "piper", "place", "plain", "plane", "plant", "plate", "point", "poker", "polar",
"power", "prank", "press", "price", "pride", "prime", "prize", "probe", "proud", "prove",
"queen", "quest", "queue", "quick", "quiet", "quilt", "radar", "radio", "raise", "range",
"rapid", "ratio", "reach", "react", "ready", "realm", "rebel", "refer", "reign", "relax",
"river", "robot", "rough", "round", "royal", "rural", "sadly", "saint", "salad", "sales",
"scale", "scare", "scene", "scent", "score", "scrub", "serum", "serve", "shady", "shake",
"shame", "shape", "share", "shark", "sharp", "sheep", "sheet", "shelf", "shine", "shiny",
"shock", "shoot", "shore", "short", "shout", "sight", "since", "skill", "skirt", "slave",
"sleep", "slice", "slide", "slope", "small", "smart", "smile", "smoke", "solar", "solid",
"solve", "sorry", "sound", "space", "spare", "speak", "speed", "spend", "spice", "spite",
"split", "spoil", "sport", "spray", "spurn", "squad", "stack", "staff", "stage", "stain",
"stamp", "stand", "start", "state", "steam", "steep", "stiff", "sting", "stock", "stone",
"storm", "story", "strip", "study", "stuff", "style", "sugar", "sunny", "super", "sweet",
"table", "taste", "teach", "teeth", "their", "theme", "there", "thick", "thief", "thing",
"third", "those", "throw", "tidal", "tight", "timid", "title", "today", "topic", "total",
"touch", "tough", "tower", "trace", "track", "trade", "trail", "train", "treat", "trend",
"trial", "troop", "truck", "truly", "trust", "truth", "twice", "uncle", "under", "union",
"unity", "upper", "urban", "usage", "usual", "valid", "value", "video", "virus", "vital",
"voice", "waste", "watch", "water", "whale", "where", "which", "while", "white", "whole",
"whose", "woman", "women", "world", "worry", "worse", "worth", "would", "wreck", "yield","abbey", "about", "abyss", "acorn", "actor", "acute", "adapt", "adder", "admit", "adore", "adorn", "adult", "affix", "after", "again", "agent", "aglow", "agree", "ahead", "aisle", "alarm", "album", "alert", "algae", "alien", "alley", "allow", "alone", "aloof", "altar", "amber", "amend", "amuse", "angel", "anger", "angle", "ankle", "apple", "apply", "apron", "arena", "argue", "arise", "armed", "arrow", "aside", "asset", "atlas", "attic", "audio", "avail", "award", "aware", "awoke", "babes", "badge", "baker", "balmy", "bandy", "barge", "basil", "basin", "batch", "beach", "beard", "beast", "begin", "belch", "belly", "bench", "berry", "birth", "bison", "blade", "blank", "blast", "blend", "blink", "bliss", "block", "blood", "bloom", "blown", "blues", "board", "boast", "bonus", "boost", "borax", "borne", "bound", "brace", "brain", "brake", "brand", "brave", "bread", "break", "brick", "bride", "brief", "bring", "brisk", "broad", "broom", "brown", "brush", "buddy", "build", "bunch", "burst", "cabin", "cable", "cache", "camel", "canal", "candy", "canoe", "carol", "carve", "catch", "cause", "cease", "chain", "chair", "chalk", "chant", "chaos", "charm", "chart", "chase", "cheap", "check", "cheek", "chess", "chill", "chirp", "choir", "choke", "chord", "chore", "claim", "class", "clean", "clear", "clerk", "click", "cliff", "cloak", "clock", "clone", "close", "cloth", "cloud", "clown", "coach", "coast", "color", "comic", "coral", "cough", "count", "court", "cover", "crack", "craft", "crane", "crash", "crawl", "crazy", "cream", "creek", "creep", "crest", "crime", "crisp", "crowd", "crown", "cruel", "crush", "curve", "cycle", "daily", "dairy", "dance", "dated", "dazed", "dealt", "death", "decay", "delay", "dense", "depth", "devil", "diary", "digit", "dirty", "donor", "doubt", "dozen", "draft", "drain", "drake", "drama", "drawn", "dream", "dress", "drift", "drink", "drive", "droid", "drown", "eager", "eagle", "early", "earth", "elbow", "elder", "elect", "elite", "empty", "enact", "enemy", "enjoy", "enter", "entry", "equal", "equip", "erase", "error", "essay", "event", "every", "exact", "exalt", "excel", "exist", "extra", "fable", "facet", "faith", "fancy", "fatal", "favor", "feast", "fence", "field", "fiery", "fifth", "fifty", "fight", "final", "finch", "flame", "flask", "fleet", "floor", "flora", "flute", "focus", "force", "forge", "forth", "found", "frame", "fresh", "fried", "frost", "fruit", "fully", "funny", "furry", "gauge", "gears", "ghost", "giant", "glade", "glass", "glide", "gloom", "glory", "glove", "gnome", "goose", "grace", "grade", "grain", "grand", "grant", "grape", "graph", "grass", "grave", "great", "greed", "green", "greet", "grief", "grind", "groan", "gross", "group", "guard", "guess", "guest", "guide", "habit", "happy", "harsh", "haste", "hatch", "haunt", "haven", "heavy", "hedge", "hinge", "hobby", "honey", "honor", "horse", "hotel", "house", "hover", "human", "humid", "humor", "hurry", "ideal", "image", "imply", "index", "inner", "input", "irony", "issue", "ivory", "jeans", "jelly", "jewel", "joint", "judge", "juice", "juicy", "kneel", "knife", "knock", "known", "label", "labor", "lance", "large", "laser", "later", "laugh", "layer", "learn", "lease", "least", "leave", "legal", "lemon", "light", "limit", "linen", "liver", "local", "logic", "loyal", "lucky", "lunar", "lunch", "magic", "major", "maker", "march", "match", "mayor", "medal", "metal", "meter", "micro", "minor", "model", "moral", "motor", "mount", "mouse", "mouth", "movie", "music", "naive", "naked", "nasty", "naval", "nerve", "never", "niche", "night", "noble", "noise", "north", "novel", "nurse", "oasis", "ocean", "offer", "often", "omega", "onion", "opera", "order", "organ", "other", "outer", "oxide", "panel", "panic", "paper", "party", "pause", "peace", "pearl", "phase", "phone", "piano", "pilot", "pivot", "place", "plain", "plane", "plant", "plate", "point", "polar", "porch", "power", "press", "price", "pride", "prime", "print", "prior", "prize", "probe", "proof", "proud", "prove", "pulse", "punch", "queen", "quest", "quick", "quiet", "quilt", "quote", "radar", "radio", "raise", "ranch", "range", "rapid", "ratio", "reach", "react", "ready", "realm", "rebel", "refer", "reign", "relax", "reply", "rhyme", "ridge", "right", "risky", "river", "robot", "rocky", "rough", "round", "royal", "ruler", "rural", "sadly", "safer", "saint", "salad", "scale", "scene", "scent", "score", "scout", "serve", "shade", "shake", "shall", "shame", "shape", "share", "shark", "sharp", "sheep", "sheet", "shelf", "shine", "shiny", "shock", "shoot", "shore", "short", "shout", "sight", "since", "skill", "skirt", "sleep", "slice", "slide", "slope", "smart", "smell", "smile", "smoke", "snail", "snake", "solar", "solid", "solve", "sorry", "sound", "space", "speak", "speed", "spend", "spice", "spine", "spite", "split", "spoil", "sport", "spray", "stack", "staff", "stage", "stamp", "stand", "stare", "start", "state", "steam", "steel", "steep", "stick", "still", "sting", "stock", "stone", "stool", "store", "storm", "story", "strap", "straw", "strip", "study", "stuff", "style", "sugar", "sunny", "super", "sweet", "sword", "table", "taste", "teach", "teeth", "theme", "there", "thick", "thief", "thing", "think", "third", "those", "throw", "tiger", "tight", "title", "toast", "today", "token", "topic", "total", "touch", "tough", "tower", "trace", "track", "trade", "trail", "train", "treat", "trend", "trial", "trick", "truck", "truly", "trust", "truth", "tulip", "twice", "uncle", "under", "union", "unity", "upper", "urban", "usage", "usual", "vague", "valid", "value", "vapor", "vital", "vivid", "vocal", "voice", "waste", "watch", "water", "weary", "whale", "wheat", "wheel", "where", "which", "while", "white", "whole", "whose", "woman", "women", "world", "worry", "wound", "wrist", "wrong", "young", "youth", "zebra", "zonal",
"young", "youth", "zebra", "zonal"]
hidden_word = random.choice(word_list)

print("WORDLE:")

# Repeat for 6 guesses
for i in range(6):
    # Guess a word
    guess_word = input()
    output = ""

    # First letter (in python, counting starts at 0 not 1)
    if guess_word[0] == hidden_word[0]:
        output += "🟩"
    elif guess_word[0] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"

    if guess_word[1] == hidden_word[1]:
        output += "🟩"
    elif guess_word[1] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"

    if guess_word[2] == hidden_word[2]:
        output += "🟩"
    elif guess_word[2] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"

    if guess_word[3] == hidden_word[3]:
        output += "🟩"
    elif guess_word[3] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"

    if guess_word[4] == hidden_word[4]:
        output += "🟩"
    elif guess_word[4] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"
        
    

    # Result
    print(output)
    if output == "🟩🟩🟩🟩🟩":
        print("You win")
        break

print(f"You used {i+1} guesses")