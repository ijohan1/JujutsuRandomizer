import random as rd
import csv, os, pandas as pd


def statb(): #стать мага
	sex=None
	sexn=rd.randint(0,1)
	if sexn == 1: 
		sex = 'female'
		return sex
	else: 
		sex = 'male'
		return sex

def name(sex):
    namesm = ["Haruto", "Ren", "Yuto", "Sota", "Yuki",
    "Kaito", "Akira", "Hiroto", "Takumi", "Ryota",
    "Daiki", "Shota", "Tsubasa", "Kazuki", "Hayato",
    "Naoki", "Hikaru", "Kenta", "Riku", "Minato",
    "Itsuki", "Shinji", "Takeru", "Yuma", "Koji",
    "Masato", "Jun", "Makoto", "Tomoya", "Yuji",
    "Kei", "Haruki", "Satoshi", "Kenji", "Noboru",
    "Taichi", "Ryusei", "Sho", "Koki", "Atsushi",
    "Fumio", "Genki", "Isamu", "Jiro", "Ryo",
    "Seiji", "Toru", "Yasuo", "Zen", "Ichiro", "Yuji", "Suguru", "Satoru", "Noritoshi", "Toge", "Yuta"]
    namesf = ["Yui", "Aoi", "Sakura", "Hana", "Mei",
    "Rin", "Yuna", "Akari", "Hina", "Mio",
    "Nanami", "Nao", "Haruka", "Rina", "Kaori",
    "Ayaka", "Misaki", "Chihiro", "Emi", "Kana",
    "Saki", "Yoko", "Tomomi", "Nozomi", "Asuka",
    "Ayumi", "Koharu", "Miku", "Natsuki", "Reina",
    "Satomi", "Sayaka", "Shiori", "Suzuka", "Wakana",
    "Yurika", "Yuri", "Momoka", "Madoka", "Keiko",
    "Eri", "Fumika", "Hotaru", "Izumi", "Kanna",
    "Megumi", "Riko", "Tamaki", "Yuzuki", "Chiaki", "Nobara", "Maki", "Tsumiki", "Haru", "Hana"]
    surnames = ["Geto", "Sato", "Suzuki", "Takahashi", "Tanaka", "Watanabe",
    "Ito", "Yamamoto", "Nakamura", "Kobayashi", "Kato",
    "Yoshida", "Yamada", "Sasaki", "Yamaguchi", "Matsumoto",
    "Inoue", "Kimura", "Hayashi", "Shimizu", "Yamazaki",
    "Mori", "Abe", "Ikeda", "Hashimoto", "Ishikawa",
    "Yamashita", "Ogawa", "Ishii", "Hasegawa", "Goto",
    "Okada", "Kondo", "Maeda", "Fujita", "Endo",
    "Aoki", "Sakamoto", "Murakami", "Ota", "Kaneko",
    "Fujii", "Fukuda", "Nishimura", "Miura", "Takeuchi",
    "Nakajima", "Okamoto", "Matsuda", "Harada", "Nakano",
    "Ono", "Tamura", "Shibata", "Sakai", "Takagi",
    "Ando", "Imai", "Ishida", "Ueda", "Morita",
    "Hara", "Shinohara", "Sugiyama", "Masuda", "Ogata",
    "Hattori", "Kikuchi", "Arakawa", "Kawasaki", "Nakata",
    "Kurosawa", "Miyazaki", "Noguchi", "Oshima", "Tsuchiya",
    "Kojima", "Asano", "Kurata", "Matsui", "Hoshino",
    "Tsuji", "Furukawa", "Iwasaki", "Katayama", "Nagata",
    "Miyamoto", "Uchida", "Nakagawa", "Kanda", "Kubo",
    "Fujimoto", "Okabe", "Kawamura", "Miyasaki", "Tachibana",
    "Nagai", "Kusunoki", "Tokugawa", "Saionji", "Minamoto", "Gojo", "Kamo", "Zenin"]
    if sex == 'female':
        fullname=rd.choice(namesf) + rd.choice(surnames)
        return fullname
    else:
        fullname=rd.choice(namesm) + rd.choice(surnames)
        return fullname
	
