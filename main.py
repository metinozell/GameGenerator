import random
import torch
import os
from diffusers import StableDiffusionPipeline

HF_TOKEN = open("hugtoken.txt", "r")

pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float32,
    use_auth_token=HF_TOKEN
).to("cpu")

turler = [
    "Bilim Kurgu",
    "Fantezi",
    "Macera",
    "Korku",
    "Gizem",
    "Post-Apokaliptik"
]

temalar = [
    "Kahramanlık",
    "İhanet",
    "Keşif",
    "Hayatta Kalma",
    "Zaman Yolculuğu"
]

elemanlar = {
    "Bilim Kurgu": [
        "uzak bir gezegen",
        "gelişmiş bir yapay zeka",
        "arızalanan bir uzay gemisi",
        "bir uzaylı istilası",
        "gizli bir deney"
    ],
    "Fantezi": [
        "mistik bir orman",
        "kadim bir kehanet",
        "güçlü bir büyücü",
        "gizli bir krallık",
        "efsanevi bir eser"
    ],
    "Macera": [
        "kaybolmuş bir hazine",
        "tehlikeli bir orman",
        "cesur bir keşif",
        "keşfedilmemiş bir ada",
        "unutulmuş bir tapınak"
    ],
    "Korku": [
        "perili bir konak",
        "lanetli bir eser",
        "küçük, ürkütücü bir kasaba",
        "karanlık bir orman",
        "kadim bir kötülük"
    ],
    "Gizem": [
        "kaybolan bir kişi",
        "şifreli bir mesaj",
        "şüpheli bir yabancı",
        "gizli bir sır",
        "çözülemeyen bir suç"
    ],
    "Post-Apokaliptik": [
        "harabe bir şehir",
        "kaynaklar için bir mücadele",
        "küçük bir hayatta kalma grubu",
        "tehlikeli bir çorak arazi",
        "terk edilmiş bir sığınak"
    ]
}

character_traits = {
    "isim": ["Arin", "Borin", "Clea", "Dara", "Eron"],
    "ırk": ["human", "elf", "dwarf", "orc", "half-elf"],
    "sınıf": ["warrior", "wizard", "archer", "thief", "healer"],
    "özellikler": ["brave", "wise", "merciful", "cunning", "ambitious"]
}

def hikaye_uret():
    tur = random.choice(turler)
    tema = random.choice(temalar)

    mekan = random.choice(elemanlar[tur])
    catisma = random.choice(elemanlar[tur])

    while catisma == mekan: 
        catisma = random.choice(elemanlar[tur])

    hikaye = (
        f"{tema.lower()} ile şekillenen bir dünyada, "
        f"hikayemiz {mekan}da başlar. "
        f"Ana karakterimiz, kendi halindeyken aniden kendini bir maceranın içinde bulur. "
        f"Her şey {catisma} ile başladığında, karakterimizin tüm hayatı değişir. "
        f"Karakter, karşılaştığı bu zorlukları aşmak için hem fiziksel hem de zihinsel sınırlarını zorlar. "
        f"Bu süreçte yeni dostluklar kurar, beklenmedik düşmanlarla yüzleşir ve kendi içindeki gücü keşfeder. "
        f"Ancak zaman ilerledikçe, karşılaştığı çatışmanın yalnızca yüzeydeki bir problem olduğunu fark eder. "
        f"Gerçek tehlike, derinlerde saklıdır ve çözülmesi gereken çok daha büyük bir gizem ortaya çıkar. "
        f"Sonunda, karakterimizin aldığı kararlar hem kendi kaderini hem de çevresindeki dünyanın kaderini belirleyecektir."       
    )

    return tur, tema, hikaye

def karakter_olustur():
    karakter = {
        "isim": random.choice(character_traits["isim"]),
        "ırk": random.choice(character_traits["ırk"]),
        "sınıf": random.choice(character_traits["sınıf"]),
        "özellik": random.choice(character_traits["özellikler"])
    }
    return karakter

def karakter_gorsellestir(karakter):
    prompt = (
    f"A detailed fantasy illustration of a {karakter['özellik']} {karakter['ırk']} {karakter['sınıf']} "
    f"named '{karakter['isim']}'. The character is depicted in a vibrant and dynamic pose, set in a mystical and atmospheric environment. "
    "The artwork features intricate details in the character's clothing and equipment, emphasizing their unique traits and role."
    )

    print(f"Visualization Prompt: {prompt}")

    image = pipe(prompt).images[0]
    image.save(f"{karakter['isim']}_character_card.png")
    print(f"{karakter['isim']}_character_card.png dosyasına kaydedildi.")

def main():
    print("Rastgele Hikaye ve Karakter Oluşturucu'ya Hoş Geldiniz!")
    input("Yeni bir hikaye ve karakter oluşturmak için Enter'a basın...")

    tur, tema, hikaye = hikaye_uret()
    print("\n--- Rastgele Hikayeniz ---")
    print(f"Tür: {tur}")
    print(f"Tema: {tema}")
    print(f"Hikaye: {hikaye}")
    print("\n--------------------------")
    
    hikaye_txt=open("story.txt","w")
    hikaye_dizayn = f"Tür: {tur} \n Tema: {tema} \n Hikaye: {hikaye}"
    hikaye_txt.write(hikaye_dizayn)

    print("Karakter oluşturuluyor...")
    karakter = karakter_olustur()
    print("Oluşturulan Karakter:")
    print(karakter)

    print("\nKarakter görselleştiriliyor...")
    karakter_gorsellestir(karakter)

if __name__ == "__main__":
    main()