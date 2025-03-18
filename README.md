# NoOffense

Güncel Yargıtay kararlarına göre hakaret sayılmayan kelimelerle rastgele tweetler üreten basit bir Python scripti. `#SözünÖzgürHali` ile paylaşımı yayalım!

## Genel Bakış

NoOffense, Yargıtay tarafından hakaret sayılmayan kelimeleri çeşitli ifadelerle birleştirerek 280 karakter sınırına uygun tweetler oluşturur. Alan izin verdiğinde tweetlere `#SözünÖzgürHali` hashtag’ini ekler, böylece X’te paylaşım için ideal hale gelir.

### Örnek Tweetler
- `Bu zalim her şeye karışıyor! #SözünÖzgürHali` (46 karakter)
- `Tam bir çapsız çıktı karşımıza.` (32 karakter)
- `Sen bir bunak değil misin? #SözünÖzgürHali` (43 karakter)

## Özellikler
- Hakaret sayılmayan kelimelerle rastgele tweetler üretir.
- Tweetlerin 280 karakter sınırını aşmamasını sağlar.
- Mümkün olduğunda `#SözünÖzgürHali` hashtag’ini ekler.

## Kurulum
1. Depoyu klonlayın:
   ```bash
   git clone https://github.com/makalin/NoOffense.git
   cd NoOffense
   ```
2. Python 3.x’in yüklü olduğundan emin olun:
   ```bash
   python --version
   ```
3. Scripti çalıştırın:
   ```bash
   python nooffense.py
   ```

## Kullanım
- Scripti çalıştırarak 5 örnek tweet üretin.
- `nooffense.py` dosyasındaki `words` veya `phrases` listelerini özelleştirerek çıktıları kişiselleştirin.
- Favori tweetlerinizi `#SözünÖzgürHali` ile paylaşın!

## Kelime Listesi
Script, şu kelimeleri kullanır (Yargıtay kararlarına dayanarak):
- zalim, münafık, çapsız, çirkef, bunak, lavuk, cahil, sevimsiz, ahlaksız, terbiyesiz, adam değilsin, eşkıya, suratsız, nankör, karaktersiz, imansız, dinsiz, zavallı, ezik, Allah belanı versin, kukla

## Katkıda Bulunun
Bu repoyu forklayın, yeni özellikler ekleyin veya pull request ile geliştirmeler önerin!

## Lisans
Bu proje MIT Lisansı ile lisanslanmıştır - detaylar için [LICENSE](LICENSE) dosyasına bakın.

## Teşekkür
Bu proje, Av. Cemil Çiçek’in paylaştığı https://x.com/avcemilcicek08/status/1901225876982837321 twitinden esinlenerek “özgür” kelimeleri yayma fikrinden ilham alınarak oluşturuldu.
