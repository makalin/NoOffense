import random

words = [
    "zalim", "münafık", "çapsız", "çirkef", "bunak", "lavuk", "cahil", 
    "sevimsiz", "ahlaksız", "terbiyesiz", "adam değilsin", "eşkıya", 
    "suratsız", "nankör", "karaktersiz", "imansız", "dinsiz", "zavallı", 
    "ezik", "Allah belanı versin", "kukla"
]

phrases = [
    "Bu {word} her şeye karışıyor!",
    "Tam bir {word} çıktı karşımıza.",
    "Böyle {word} birini görmedim.",
    "{word} tavırları bıktırdı artık.",
    "Sen bir {word} değil misin?",
    "Ne kadar {word} bir tip bu!",
    "Bu {word} yüzünden çıldıracağım.",
    "{word} biriyle uğraşmak zorundayım.",
    "Herkes bu {word} kişiden şikayetçi.",
    "Yine {word} birini bulduk!",
    "{word} halleri çekilmez oldu.",
    "Bu {word} gibiler hep aynı.",
    "Karşımda tam bir {word} var.",
    "{word} olmak da bir yetenek!",
    "Bu {word} resmen baş belası.",
]

HASHTAG = "#SözünÖzgürHali"

def generate_twit():
    phrase = random.choice(phrases)
    word = random.choice(words)
    
    tweet = phrase.format(word=word)
    
    tweet_with_hashtag = f"{tweet} {HASHTAG}"
    if len(tweet_with_hashtag) <= 280:
        return tweet_with_hashtag
    elif len(tweet) <= 280:
        return tweet
    else:
        return f"Bu {word} çok sinir bozucu!"

for i in range(5):
    tweet = generate_twit()
    print(f"Tweet {i+1} ({len(tweet)} chars): {tweet}")